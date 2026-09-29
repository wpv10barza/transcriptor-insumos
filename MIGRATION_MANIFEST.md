# Migration Manifest — Transcriptor de Insumos

- source: Google Drive
- source_folder: `Codigos_Antes_Exportados/Transcriptor de Insumos`
- project_family: `Transcriptor de Insumos / Robot2`
- version: snapshot auditado 2026-09-29
- github_repository: `wpv10barza/transcriptor-insumos`
- github_branch: `import/drive-2026-09-29`
- github_commit: pendiente hasta verificación final
- files_expected: 3 archivos fuente principales en Transcriptor de Insumos; Robot2 aporta una variante de configuración
- files_migrated: `main.py`, `config.py`, `src/selenium_runner.py`, documentación, dependencias y CI
- files_excluded: rutas locales privadas, perfiles de navegador, drivers generados, caches y datos locales
- verification_status: `PENDING_GITHUB_CI`
- verified_at: pendiente

## Genealogía Robot2

`main.py` y `src/selenium_runner.py` son idénticos entre Robot2 y Transcriptor de Insumos. `config.py` solo difiere en la ruta hardcodeada de `PATH_WHISPER_DEFAULT`. Por tanto, Robot2 se clasifica como variante histórica de la misma línea, no como proyecto independiente.

## SHA-256 de origen

| Archivo | Robot2 | Transcriptor de Insumos | Resultado |
|---|---|---|---|
| `main.py` | `ba523fd7f41938c1a5c1c4c95884d99195a74d2667a36cb02a7107c64fdf6822` | `ba523fd7f41938c1a5c1c4c95884d99195a74d2667a36cb02a7107c64fdf6822` | idéntico |
| `config.py` | `91a25aa1c1337c49021b1f1a4afd41b2dcfdb4e843a03371ad1b48a2ac0b4e6a` | `3cd4a726115c7d76f9d92a1428cfa275295328c4dd2086ca0bd0e1045156f3d6` | difiere solo la ruta local de Whisper |
| `src/selenium_runner.py` | `af4e5393a449159c94c7040c678e24a0459bfff32cf69aeabef485786059989f` | `af4e5393a449159c94c7040c678e24a0459bfff32cf69aeabef485786059989f` | idéntico |
