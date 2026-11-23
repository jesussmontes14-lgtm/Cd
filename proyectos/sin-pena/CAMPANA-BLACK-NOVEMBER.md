# Campaña Meta · Black November 2026 (SIN PENA)

Estado: estructura definida · NO creada en Meta todavía · se crea PAUSADA y solo la activa el creador.

## Campaña
- Nombre: `SIN PENA · Ventas · Black November 2026`
- Objetivo: Ventas · Sin categoría especial
- Presupuesto a nivel conjunto (un solo conjunto)

## Conjunto
- Nombre: `BN · CO+MX · 25-55 · Inicio de pago`
- Optimización: conversiones en sitio web → evento **Inicio de pago** (píxel de la landing;
  la Compra aún no está validada)
- Presupuesto: COP 15.000/día · Fin: 30 nov 23:59 (Bogotá) → ≈ COP 120.000 en 8 días
- Público: Colombia + México, 25-55, sin Advantage+ audiencia (edad exacta)
- Ubicaciones: Advantage+

## Anuncios (se agregan cuando estén los creativos)
| Nombre | Creativo | Formato |
|--------|----------|---------|
| `SINPENA_BLACKNOV_H1_916_2026-11` | Concepto H · gancho "Esto es todo lo que te llevas" | Video 9:16 + 4:5 |
| `SINPENA_BLACKNOV_H2_916_2026-11` | Concepto H · gancho "Black November: SIN PENA trae regalo" | Video 9:16 + 4:5 |
| `SINPENA_BLACKNOV_H3_916_2026-11` | Concepto H · gancho "Último aviso: esto termina el 30 de noviembre" | Video 9:16 + 4:5 |
| `SINPENA_BLACKNOV_IMG_45_2026-11` | Imagen Black November 1080x1350 con la oferta real | Imagen 4:5 |
Destino: landing de SIN PENA · Botón: Comprar · Copys: los del concepto H (chat del 23 nov).

## Antes de activar (lo hace el creador)
- [ ] Landing con banner, contador y oferta real · "42 recetas"
- [ ] Hotmart: regalo MI PLAN 21 DÍAS en el área de miembros · LO QUE COMO YO a USD 4.90
- [ ] Compra de prueba con cupón 100 % para validar el evento Compra
- [ ] Revisar en el Administrador que presupuesto y fecha de fin se ven bien

## Cómo se crea
`scripts/meta/crear_campana_bn.py` (modo prueba por defecto; `--crear` la crea PAUSADA y lo
verifica). Necesita un token de la API de Marketing guardado en la sesión.
