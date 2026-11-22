---
name: anuncio-meta
description: Prepara todo lo creativo para pautar en Meta (Facebook e Instagram Ads) — plan de prueba, variantes de gancho, adaptación de formatos (9:16, 4:5, 1:1), texto principal, título, descripción, botón de CTA, nomenclatura, economía (CPA de equilibrio) y reglas para leer, escalar o apagar anuncios. Úsala siempre que el destino sea pauta, cuando pidan "anuncio", "ad", "pauta", "campaña", "creativo para Meta", "copy del anuncio" o al planear una prueba de creativos.
---

# Skill: anuncio-meta

El trabajo creativo es la palanca principal de la pauta: con segmentación amplia, el creativo
ES la segmentación. Esta skill decide qué se prueba, entrega el pack listo para subir y define
cómo leer el resultado.

## 1. Plan de prueba (Paso 2 del flujo)

Antes de escribir nada, propone:
- **Hipótesis**: qué ángulo de PRODUCTO.md y por qué (apóyate en APRENDIZAJES.md).
- **Qué varía**: lo primero que se prueba es el ÁNGULO; luego el GANCHO; al final el formato
  o el copy. Nunca varíes dos cosas en el mismo par de anuncios.
- **Pack estándar de prueba**: 2-3 conceptos (ángulos distintos) × 3 variantes de gancho
  sobre el mismo cuerpo. Una sola sesión de grabación por concepto.
- **Estructura sugerida** (el creador decide en el Administrador de anuncios):
  campaña de Ventas, conjunto con segmentación amplia en los países del brief (mayores de 18,
  obligatorio en salud), ubicaciones Advantage+, un conjunto por concepto, presupuesto del
  brief repartido entre conjuntos.
- **Qué se mide y cuándo se decide** (§6).

## 2. Pack creativo por anuncio

Para cada concepto aprobado:
1. **Video maestro 9:16** — guion completo vía skill `guion`, apto para Reels y Stories.
2. **Variantes de gancho** — 3 arranques distintos (0-3 s) que empalman con el mismo cuerpo.
   Cada uno de una palanca distinta de la skill `ganchos`.
3. **Adaptación 4:5 (Feed)** — qué se recorta o reencuadra; texto dentro de la zona central.
4. **Miniatura / primer frame** — debe funcionar como imagen estática sin sonido.
5. **Copy** (cada pieza en su bloque de código):
   - **Texto principal** — la primera línea (≈125 caracteres antes de "ver más") es otro
     gancho; luego 2-5 líneas: dolor en palabras del avatar → qué obtiene → prueba real si
     existe → oferta (precio, garantía) → CTA. Versión corta (1-2 líneas) y larga.
   - **Título** — ≤ 40 caracteres, beneficio u oferta.
   - **Descripción** — ≤ 30 caracteres, refuerzo (garantía, acceso inmediato, precio).
   - **Botón** — el que corresponda (Comprar / Más información / Registrarte).
6. **Nomenclatura** para subirlo: `PRODUCTO_ANGULO_GANCHO_FORMATO_FECHA`
   (ej. `SINPENA_HINCHAZON_G2_916_2026-11`). Esa misma etiqueta va al REGISTRO.md.
7. **Revisión de compliance** con la skill `compliance` — Meta revisa el anuncio Y la página
   de destino.

## 3. Reglas creativas propias de la pauta

- Los primeros 3 s cargan todo: el gancho tiene que funcionar sin sonido y sin contexto previo.
- El producto o la oferta aparecen antes del cierre en CONVERSIÓN: quien llega a la página ya
  sabe qué compra y cuánto cuesta (filtra clics vacíos).
- Lo que se ve nativo (celular, cocina real, cara real) suele superar a lo producido.
  Verifícalo con datos propios en APRENDIZAJES.md.
- Habla de la SITUACIÓN, nunca afirmes atributos personales del espectador (ver `compliance`).
- Un creativo ganador se explota con nuevos ganchos sobre el mismo cuerpo antes de buscar otro
  concepto: la fatiga se cura primero cambiando el arranque.

## 4. Formatos

| Ubicación | Relación | Notas |
|-----------|----------|-------|
| Reels / Stories | 9:16 | Video maestro. Zona segura de la skill `guion`. |
| Feed | 4:5 | Reencuadre del maestro. |
| Columna derecha / otros | 1:1 | Solo si el plan lo pide. |

## 5. Economía (con datos reales o placeholders, nunca supuestos)

- **Ingreso por venta** = precio − comisión de la plataforma de venta − impuestos [COMISIÓN REAL].
- **Ticket promedio** = ingreso por venta + (tasa de toma de cada order bump × su ingreso).
- **CPA de equilibrio** = ticket promedio. Por encima, cada venta pierde dinero.
- **CPA objetivo** = el que deje el margen que el creador quiera [MARGEN].
- En productos de ticket bajo el margen es estrecho: los order bumps y el upsell pesan mucho.
  Señálalo en el plan.

## 6. Lectura y decisiones

Métricas por anuncio (las calcula `aprender` con la exportación del Administrador):
- **Hook rate** = reproducciones de 3 s / impresiones → mide el gancho.
- **Hold rate** = reproducciones de 15 s (o ThruPlay) / reproducciones de 3 s → mide el cuerpo.
- **CTR de enlace** → mide si el video genera intención.
- **Conversión de página** = compras / visitas a la página → mide la página, no el video.
- **CPA** y **ROAS** → mide el negocio.

Diagnóstico:
- Hook rate bajo → cambia el gancho, conserva el cuerpo.
- Hook bueno, hold bajo → el cuerpo no paga la promesa del gancho.
- Hold bueno, CTR bajo → falta deseo, oferta o CTA.
- CTR bueno, pocas compras → problema de página, precio o coherencia video→página.

Umbrales de partida (solo hasta que APRENDIZAJES.md tenga cifras propias; entonces mandan
las propias): hook rate ≥ 25 %, hold rate ≥ 20 %, CTR de enlace ≥ 1 %.
Reglas de partida: no juzgar un anuncio antes de ~1.000 impresiones; apagar si gastó ~2× el
CPA objetivo sin venta; escalar en pasos de ~20 % del presupuesto cuando sostiene CPA ≤ objetivo
varios días.

## Lecciones aprendidas
<!-- La skill `aprender` añade aquí lo confirmado. Formato: - AAAA-MM-DD · lección · evidencia -->
