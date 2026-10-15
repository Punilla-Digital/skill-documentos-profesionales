# Generador
Requerir Python con reportlab y Pillow.
Ejecutar: `python scripts/create_tutorial.py entrada.json salida.pdf`
Resolver rutas de imágenes relativas al JSON. El logo se resuelve desde la habilidad.

Ejemplo:
```json
{"title":"Cómo cambiar un método de pago","summary":"Ingresá a la cuenta, agregá la tarjeta y revisá su configuración.","software":"Google Ads","steps":[{"title":"Abrí Facturación","instruction":"Hacé clic en Facturación.","image":"captura.png","crop":[0,0,900,600],"marks":[{"type":"rect","box":[10,220,80,55]},{"type":"circle","box":[20,225,35,35]},{"type":"text","at":[110,230],"text":"Hacé clic aquí"}],"caption":"El recuadro señala la opción."},{"title":"Guardá","instruction":"Revisá los datos y presioná Guardar.","note":"Comprobá que el método aparezca en el listado."}]}
```

Coordenadas en píxeles de la imagen original, origen arriba a la izquierda.
- crop: [izquierda, arriba, derecha, abajo]; omitir para imagen completa.
- box: [x, y, ancho, alto]. Marcas dentro del recorte.
- rect: rectángulo; square: cuadrado con lados iguales.
- circle: círculo con lados iguales; ellipse: óvalo.
- text: texto corto rojo desde at=[x,y].
- Sin image: mostrar un paso textual con la leyenda «Paso sin captura».
No simular una captura faltante. No usar imágenes de ejemplo con datos sensibles.
Si un texto excede el espacio, resumir/dividir el paso. Nunca reducirlo hasta ser ilegible.
Renderizar y revisar todas las páginas de salida: el script no sustituye el control visual.

