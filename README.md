# Transcriptor de Insumos

Repositorio canónico reconstruido desde Google Drive. El proyecto automatiza la carga de una transcripción y un prompt de instrucciones en ChatGPT mediante Selenium con Microsoft Edge.

## Origen
- Google Drive: `Transcriptor de Insumos`
- Variante histórica relacionada: `Robot2`

## Tecnologías observadas
- Python
- Selenium WebDriver
- Microsoft Edge / Selenium Manager
- pyperclip

## Estructura
- `main.py`: CLI y flujo principal.
- `config.py`: configuración portable; las rutas locales originales se sustituyeron por variables de entorno.
- `src/selenium_runner.py`: automatización del navegador y carga de archivos.
- `legacy/robot2/`: documentación de la variante histórica.

## Configuración
Definir opcionalmente `TRANSCRIPTOR_INSTRUCCIONES` y `TRANSCRIPTOR_WHISPER`; si no se definen, se usan rutas relativas bajo `inputs/`.

## Archivos excluidos
Perfiles del navegador, ejecutables de driver, datos locales, caches y rutas privadas de la estación de trabajo.
