# Migration Manifest — Transcriptor de Insumos

- source: Google Drive
- source_folders:
  - `Proyectos_Exportados/Transcriptor de Insumos`
  - `Proyectos_Exportados/Robot2`
- project_family: `Transcriptor de Insumos / Robot2`
- version: snapshot auditado 2026-09-29
- github_repository: `wpv10barza/transcriptor-insumos`
- github_branch: `import/drive-2026-09-29`
- exact_source_commit: `e07c91903475813fe82b89bc24c97007421e6db1`
- files_expected: 3 archivos fuente principales en Transcriptor de Insumos; Robot2 aporta una variante histórica de configuración
- files_migrated: `main.py`, `config.py`, `src/selenium_runner.py`, documentación, dependencias y CI
- exact_bytes_preserved: `main.py`, `src/selenium_runner.py`
- sanitized_files: `config.py` (rutas locales del equipo sustituidas por variables de entorno/fallbacks relativos)
- files_excluded: rutas locales privadas, perfiles de navegador, drivers generados, caches y datos locales
- robot2_independent_repository: `false`
- robot2_classification: `VARIANTE_HISTORICA_MISMA_LINEA`
- verification_status: `PENDING_GITHUB_CI`
- verified_at: pendiente
- deletion_allowed: `false`

## Genealogía Robot2

`main.py` y `src/selenium_runner.py` son idénticos byte por byte entre Robot2 y Transcriptor de Insumos. `config.py` solo difiere en la ruta local usada como valor por defecto para la transcripción. La lógica, estructura y automatización son las mismas. Por tanto, Robot2 se conserva como rama histórica de esta familia y **no** justifica crear `robot2-chatgpt-uploader`.

## SHA-256 de origen

| Archivo | Robot2 | Transcriptor de Insumos | Resultado |
|---|---|---|---|
| `main.py` | `ba523fd7f41938c1a5c1c4c95884d99195a74d2667a36cb02a7107c64fdf6822` | `ba523fd7f41938c1a5c1c4c95884d99195a74d2667a36cb02a7107c64fdf6822` | idéntico |
| `config.py` | `91a25aa1c1337c49021b1f1a4afd41b2dcfdb4e843a03371ad1b48a2ac0b4e6a` | `3cd4a726115c7d76f9d92a1428cfa275295328c4dd2086ca0bd0e1045156f3d6` | misma configuración funcional; difiere ruta local por defecto |
| `src/selenium_runner.py` | `af4e5393a449159c94c7040c678e24a0459bfff32cf69aeabef485786059989f` | `af4e5393a449159c94c7040c678e24a0459bfff32cf69aeabef485786059989f` | idéntico |

## Git blob SHA de los archivos exactos importados

- `main.py`: `000a5fb10012dc62a38d9fe4bf9944f714b62c6b`
- `src/selenium_runner.py`: `7aae6c0df8c9aeeaa943c219983d380f3186caff`
