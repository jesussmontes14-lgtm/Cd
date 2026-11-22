# Cd

Agente creativo para vender productos e infoproductos con contenido vertical y anuncios en
Meta, trabajando con Claude Code.

## Cómo se usa

1. Abre una sesión de Claude Code sobre este repo.
2. Dale la información del producto (link de la página de venta o texto).
3. Pide lo que necesites: "plan de campaña para Meta", "un anuncio del capítulo 4",
   "un reel de anzuelo", "analiza estos resultados" (pegando la exportación del Administrador).

## Estructura

- `CLAUDE.md` — identidad, leyes y flujo del agente.
- `.claude/skills/` — métodos que crecen con lo aprendido: `producto`, `ganchos`, `guion`,
  `anuncio-meta`, `compliance`, `aprender`.
- `proyectos/<producto>/` — oferta y avatar (`PRODUCTO.md`), voz (`VOZ.md`), piezas y métricas
  (`REGISTRO.md`) y lecciones (`APRENDIZAJES.md`).
- `proyectos/_plantilla/` — base para un producto nuevo.
