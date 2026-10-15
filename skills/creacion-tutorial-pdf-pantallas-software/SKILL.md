---
name: creacion-tutorial-pdf-pantallas-software
description: Crear tutoriales PDF de software a partir de capturas y pasos del usuario, con portada y encabezados de Punilla Digital y cuadrados, rectángulos, círculos o textos rojos sobre los controles. Usar para guías paso a paso, manuales de pantallas y tutoriales visuales en PDF.
---

# Creación de tutorial PDF - Pantalla de softwares

Crear guías para usuarios finales en español rioplatense. Aplicar la habilidad PDF disponible y sus requisitos de creación y revisión.

## Recursos obligatorios
- Leer [marca.md](references/marca.md) para identidad y datos comerciales.
- Leer [formato.md](references/formato.md) antes de usar el generador.
- Usar assets/punilla-digital-logo.png en portada y encabezados.
- Mantener agents/openai.yaml y sus iconos como metadatos de interfaz. No afirmar instalación sin confirmación del sistema.

## Flujo
1. Abrir e inspeccionar todas las capturas. Resolver adjuntos con las herramientas disponibles; usar rutas locales si el usuario las indicó. Si falla la descarga, probar otra vía disponible y explicar el bloqueo sin pedir repetidamente los mismos adjuntos.
2. Ordenar las capturas por su contenido y relacionarlas con las acciones. No depender solo del nombre del archivo. Pedir aclaración solo cuando cambie el procedimiento.
3. Escribir instrucciones breves que coincidan con los controles visibles. Consultar documentación oficial si se necesita validar la interfaz actual. Diferenciar agregar un recurso, seleccionarlo como principal y eliminar uno anterior.
4. No inventar pantallas ni botones faltantes. Describir los pasos sin captura como texto, indicándolo discretamente. No ejecutar acciones en cuentas reales por el solo hecho de crear una guía.
5. Crear SIEMPRE una primera página de presentación independiente: logo de Punilla Digital, título y resumen específicos del tutorial, software y datos comerciales confirmados de marca.md. Nunca empezar con el paso 1.
6. Incluir en TODAS las páginas interiores un encabezado con el logo completo de Punilla Digital. Agregar título corto del tutorial y numeración de pasos/páginas.
7. Recortar y ampliar las capturas cuando ayude a identificar el control; mantener contexto y proporciones. Preferir un paso por página y A4 apaisado para pantallas horizontales.
8. Dibujar las marcas como vectores sobre la captura en el PDF. Usar rojo #E32636: cuadrados/rectángulos alrededor de botones o campos; círculos alrededor de iconos; textos cortos rojos para explicar acciones. Admitir combinaciones, flechas y números. No regenerar las interfaces con IA.
9. Usar bordes de 2 a 3 puntos sin relleno opaco. No tapar las etiquetas de los controles. Poner textos en zonas libres o fuera de la captura. Transformar las coordenadas de la imagen original al recortar/escalar.
10. Redactar irreversiblemente los datos sensibles innecesarios en una copia antes de insertarla: contraseñas, tarjetas, correos e identificadores ajenos. No usar una simple anotación PDF removible para ocultarlos. Preservar originales.
11. Generar con scripts/create_tutorial.py o una composición equivalente. Usar fuentes con acentos, sin depender de rutas de una máquina. Si falta una captura, crear un paso textual, nunca una interfaz inventada.
12. Renderizar y revisar TODAS las páginas. Verificar portada, logo en encabezados, encuadres, precisión de marcas, texto legible, saltos y ausencia de desbordes. Comprobar enlaces de contacto y texto seleccionable.
13. Terminar con guardar/confirmar y una comprobación del resultado cuando corresponda. No prometer éxito sin observarlo.
14. Guardar el PDF mediante el mecanismo persistente disponible y entregar enlace al PDF. No entregar scripts, JSON ni capturas de revisión salvo pedido. Informar con claridad si falla guardar o instalar.

Reservar el texto comercial extenso para la portada. Priorizar el tutorial en el resto de páginas. No incluir precios o promociones sin una consulta actual.
