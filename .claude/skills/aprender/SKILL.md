---
name: aprender
description: Cierra el ciclo de mejora — lee resultados (exportación CSV del Administrador de anuncios de Meta, estadísticas de Reels/TikTok, números pegados o capturas) y el feedback del creador, calcula métricas, diagnostica cada pieza, registra en REGISTRO.md, extrae lecciones a APRENDIZAJES.md y sube las confirmadas a las skills. Úsala cuando lleguen métricas, cuando el creador apruebe, rechace o corrija algo, cuando Meta rechace un anuncio, o cuando pidan "qué aprendimos", "analiza los resultados" o "qué funcionó".
---

# Skill: aprender

El sistema mejora solo si cada resultado y cada corrección se convierten en una regla escrita.
Esta skill es la única que edita las secciones "Lecciones aprendidas" de las demás.

## 1. Entradas posibles

- **Métricas de pauta**: CSV exportado del Administrador de anuncios (nivel anuncio) o números
  pegados. Columnas útiles: nombre del anuncio, importe gastado, impresiones, reproducciones de
  3 s, ThruPlay o reproducciones de 15 s, clics en el enlace, visitas a la página de destino,
  compras, valor de compras.
- **Métricas orgánicas**: visualizaciones, retención media, % que vio completo, guardados,
  compartidos, comentarios, visitas al perfil, clics.
- **Feedback del creador**: aprobó, rechazó, corrigió una frase, "así no hablo", "esto me gustó".
- **Rechazo o restricción de Meta**: motivo literal.

## 2. Proceso

1. **Registrar**: cada pieza en REGISTRO.md con su nomenclatura (ver `anuncio-meta` §2),
   ángulo, palanca y mecanismo del gancho, carril y métricas.
2. **Calcular** (con un script si hay CSV): hook rate, hold rate, CTR de enlace, conversión de
   página, CPA, ROAS. No inventes columnas que no vengan.
3. **Diagnosticar** cada pieza con la tabla de `anuncio-meta` §6: ¿falló el gancho, el cuerpo,
   la oferta o la página?
4. **Comparar** solo lo comparable: mismo producto, misma oferta, gasto suficiente
   (≥ ~1.000 impresiones por anuncio). Lo que no llegue a eso se anota como "sin datos
   suficientes", no como lección.
5. **Escribir lecciones** en APRENDIZAJES.md del proyecto:
   `- AAAA-MM-DD · [GANCHO|CUERPO|OFERTA|PÁGINA|FORMATO|VOZ|COMPLIANCE] · lección · evidencia (piezas y cifras)`
   Estado: **hipótesis** (1 pieza) → **confirmada** (≥ 2 piezas que coinciden) →
   **descartada** (datos en contra; se tacha, no se borra).
6. **Actualizar umbrales propios**: cuando haya ≥ 5 anuncios con datos suficientes, escribe en
   APRENDIZAJES.md los promedios propios de hook rate, hold rate, CTR y CPA. Desde ahí reemplazan
   los umbrales de partida de `anuncio-meta`.
7. **Subir a las skills** solo lo confirmado y general (válido para cualquier producto):
   añade una línea en la sección "Lecciones aprendidas" de la skill correspondiente
   (`ganchos`, `guion`, `anuncio-meta`, `compliance`, `producto`). Lo propio de un producto se
   queda en su APRENDIZAJES.md.
   Si una lección contradice una regla del cuerpo de una skill, NO edites el cuerpo: anota la
   contradicción y propónle el cambio al creador.
8. **Feedback de voz o estilo**: va directo a VOZ.md o a "Preferencias del creador" en
   APRENDIZAJES.md desde la primera vez. Una corrección nunca se repite.
9. **Próximo paso**: termina con 1-3 recomendaciones concretas (qué gancho reemplazar, qué
   concepto escalar, qué ángulo probar después).
10. **Commit + push** con un mensaje que diga qué se aprendió
    (ej. "Aprendizaje: ganchos de escena cotidiana superan a mitos en SIN PENA").

## 3. Entrega en el chat

- Tabla por pieza: nombre · gasto · hook · hold · CTR · CPA · diagnóstico.
- Lecciones nuevas (y su estado).
- Cambios hechos en skills y archivos.
- Recomendaciones.

## Lecciones aprendidas
<!-- Lecciones sobre cómo medir y aprender mejor. Formato: - AAAA-MM-DD · lección · evidencia -->
