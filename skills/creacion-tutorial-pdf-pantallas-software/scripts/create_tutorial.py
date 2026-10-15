"""Build a branded tutorial from inspected screenshots and original-pixel marks."""
import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
W, H = 841.89, 595.28
RED = HexColor('#E32636')
INK = HexColor('#21133D')
GRAY = HexColor('#566174')

def fonts():
    candidates = [
        ('C:/Windows/Fonts/segoeui.ttf', 'C:/Windows/Fonts/segoeuib.ttf'),
        ('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'),
        ('/Library/Fonts/Arial.ttf', '/Library/Fonts/Arial Bold.ttf'),
    ]
    for regular, bold in candidates:
        if Path(regular).is_file() and Path(bold).is_file():
            pdfmetrics.registerFont(TTFont('Body', regular))
            pdfmetrics.registerFont(TTFont('Strong', bold))
            return
    raise RuntimeError('Instalá una fuente Unicode (DejaVu Sans, Segoe UI o Arial).')

def paragraph(c, text, x, top, width, maxheight, size=13, color=INK):
    style = ParagraphStyle('p', fontName='Body', fontSize=size, leading=size*1.45, textColor=color)
    p = Paragraph(escape(str(text)), style)
    _, height = p.wrap(width, maxheight)
    if height > maxheight:
        raise ValueError('Texto demasiado largo: resumir o dividir el paso.')
    p.drawOn(c, x, top-height)

def logo(c, x, y, size):
    c.drawImage(str(ROOT/'assets/punilla-digital-logo.png'), x, y, size, size,
                preserveAspectRatio=True, mask='auto')

def header(c, number, total, title):
    c.setFillColor(HexColor('#F5F6FA')); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(INK); c.rect(0, H-6, W, 6, fill=1, stroke=0)
    logo(c, 34, H-66, 44)
    c.setFillColor(INK); c.setFont('Strong', 13); c.drawString(89, H-37, 'PUNILLA DIGITAL')
    paragraph(c, title, 89, H-44, W-155, 26, 9, GRAY)
    c.setStrokeColor(HexColor('#DCE1EA')); c.line(34, 39, W-34, 39)
    c.setFillColor(GRAY); c.setFont('Body', 9)
    c.drawString(34, 22, 'punilladigital.com.ar')
    c.drawRightString(W-34, 22, f'{number} / {total}')

def cover(c, data, total):
    header(c, 1, total, 'GUÍA DE USO · PANTALLAS DE SOFTWARE')
    logo(c, 36, 347, 115)
    paragraph(c, data['title'], 174, 450, 620, 105, 28)
    paragraph(c, data.get('software', ''), 174, 333, 620, 28, 12, GRAY)
    paragraph(c, data['summary'], 36, 285, W-72, 85, 16)
    c.setFillColor(INK); c.setFont('Strong', 12)
    c.drawString(36, 174, 'Soluciones tecnológicas para tu negocio')
    paragraph(c, 'Desarrollo web · Sistemas personalizados · Marketing digital · Automatizaciones con IA',
              36, 160, W-72, 38, 11, GRAY)
    contacts = [
        ('Web: punilladigital.com.ar', 'https://punilladigital.com.ar/'),
        ('Email: info@punilladigital.com.ar', 'mailto:info@punilladigital.com.ar'),
        ('WhatsApp: +54 3548 410415', 'https://wa.me/543548410415'),
        ('Av. Edén 405, La Falda, Córdoba', None),
    ]
    for i, (text, url) in enumerate(contacts):
        y = 112-i*15
        c.setFont('Body', 10); c.setFillColor(INK); c.drawString(36, y, text)
        if url: c.linkURL(url, (36, y-2, 360, y+11), relative=0)
    c.showPage()

def draw_screen(c, step, base):
    source = (base/step['image']).resolve()
    with Image.open(source) as original:
        original.load()
        im = original.convert('RGB')
    left, top, right, bottom = step.get('crop', [0, 0, im.width, im.height])
    if not (0 <= left < right <= im.width and 0 <= top < bottom <= im.height):
        raise ValueError('Recorte fuera de la captura.')
    im = im.crop((left, top, right, bottom))
    scale = min((W-80)/im.width, 305/im.height)
    width, height = im.width*scale, im.height*scale
    x, y = (W-width)/2, 102+(305-height)/2
    c.drawImage(ImageReader(im), x, y, width, height)
    def point(px, py):
        if not (left <= px <= right and top <= py <= bottom):
            raise ValueError('Marca fuera del recorte.')
        return x+(px-left)*scale, y+height-(py-top)*scale
    c.setStrokeColor(RED); c.setFillColor(RED); c.setLineWidth(2.5)
    for mark in step.get('marks', []):
        kind = mark['type']
        if kind == 'text':
            px, py = point(*mark['at']); text = mark['text']
            if len(text) > 65: raise ValueError('Etiqueta roja demasiado larga.')
            c.setFont('Strong', 11)
            if px+pdfmetrics.stringWidth(text, 'Strong', 11) > x+width:
                raise ValueError('Etiqueta excede el borde: moverla o usar caption.')
            if py-13 < y: raise ValueError('Etiqueta excede el borde inferior.')
            c.drawString(px, py-11, text)
        elif kind in ('rect', 'square', 'circle', 'ellipse'):
            bx, by, bw, bh = mark['box']
            if bw <= 0 or bh <= 0: raise ValueError('Marca sin tamaño positivo.')
            if kind in ('square', 'circle') and bw != bh:
                raise ValueError('Cuadrados y círculos requieren lados iguales.')
            px, py = point(bx, by); point(bx+bw, by+bh)
            if kind in ('circle', 'ellipse'):
                c.ellipse(px, py-bh*scale, px+bw*scale, py, fill=0, stroke=1)
            else:
                c.rect(px, py-bh*scale, bw*scale, bh*scale, fill=0, stroke=1)
        else: raise ValueError(f'Tipo de marca no admitido: {kind}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Path); parser.add_argument('output', type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding='utf-8-sig'))
    if not data.get('title') or not data.get('summary') or not data.get('steps'):
        raise ValueError('Se requieren title, summary y steps.')
    fonts(); args.output.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(args.output), pagesize=(W,H))
    c.setTitle(data['title']); c.setAuthor('Punilla Digital')
    count = len(data['steps'])+1
    cover(c, data, count)
    for i, step in enumerate(data['steps'], 1):
        header(c, i+1, count, data['title'])
        paragraph(c, f"{i}. {step['title']}", 36, 510, W-72, 42, 22)
        paragraph(c, step['instruction'], 36, 463, W-72, 48, 13)
        if step.get('image'):
            draw_screen(c, step, args.input.resolve().parent)
        else:
            paragraph(c, 'Paso sin captura', 36, 356, W-72, 30, 13, RED)
            paragraph(c, step.get('note', 'Seguí la indicación en el software y verificá el resultado.'),
                      36, 315, W-72, 150, 17)
        caption = step.get('caption', step.get('note', '') if step.get('image') else '')
        if caption: paragraph(c, caption, 36, 83, W-72, 38, 11, RED)
        c.showPage()
    c.save()
    print(args.output.resolve())

if __name__ == '__main__': main()
