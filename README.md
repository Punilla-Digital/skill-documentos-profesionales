# Documentos Profesionales

Este repositorio conserva la [skill general básica](SKILL.md) y agrega una especialidad completa:

## Creación de tutorial PDF — Pantallas de software

Tutoriales PDF con portada, marca de Punilla Digital, capturas reales e indicaciones rojas. Incluye generador Python, logo, iconos y referencias de formato.

- Instrucciones: [SKILL.md](skills/creacion-tutorial-pdf-pantallas-software/SKILL.md).
- Recursos e iconos: incluidos en `skills/creacion-tutorial-pdf-pantallas-software/assets/` y `skills/creacion-tutorial-pdf-pantallas-software/agents/`.
- Referencias: `skills/creacion-tutorial-pdf-pantallas-software/references/`.

## Requisitos

Python, reportlab, Pillow y una fuente Unicode compatible con el generador. Requiere capturas reales y herramientas para renderizar y revisar todas las páginas. El generador incluido utiliza A4 apaisado.

## Uso e instalación

1. Descargar el repositorio.
2. Usar la carpeta `skills/creacion-tutorial-pdf-pantallas-software` para esta especialidad. Para la versión general, usar el SKILL.md de la raíz.
3. En un agente compatible, copiar la carpeta completa con el nombre `creacion-tutorial-pdf-pantallas-software` a su directorio de skills. Conservar scripts, referencias y recursos junto al SKILL.md. Si el entorno ofrece importación, seguir su procedimiento; publicar en GitHub no instala automáticamente la skill en ChatGPT.
4. Resolver las rutas de recursos desde la carpeta de la skill. En otros asistentes, adjuntar solo SKILL.md no carga automáticamente scripts ni imágenes.

Las menciones a habilidades de PDF o generación de imágenes requieren herramientas equivalentes en el entorno; no se incluyen habilidades de terceros. Los iconos de agents/openai.yaml dependen del soporte del agente.

## Ejemplo

> Creá un tutorial PDF con estas capturas y señalá en rojo los botones que hay que pulsar.

## Identidad y recursos

Conservar los logos y las reglas incluidas. Aplicar los cambios de marca, colores o formato que admita la habilidad y solicite el usuario. No inventar un logo ni presentar archivos como generados antes de crearlos y verificarlos.

## Origen y alcance

Copia de la habilidad personal de Punilla Digital aprobada para este repositorio el 15/10/2026. Se preservan sus instrucciones y recursos funcionales; esta publicación no modifica la habilidad instalada en Complementos.

[Punilla Digital](https://punilladigital.com.ar/) · Consultar [LICENSE](LICENSE).
