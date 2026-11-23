---
name: visuales-ia
description: Escribe prompts listos para pegar en generadores de imagen y video con IA (Midjourney, Flux, Ideogram, DALL·E, Kling, Runway, Veo, Sora, Hailuo, Pika u otros) para B-roll, clips de apoyo, miniaturas, portadas de carrusel y metáforas visuales de un guion — y decide qué se graba de verdad y qué se genera. Úsala cuando pidan "prompts", "imágenes", "clips", "B-roll", "generar con IA", "miniatura" o al cerrar un guion que tenga planos sin grabar.
---

# Skill: visuales-ia

La IA rellena lo que no se puede o no conviene grabar. Nunca sustituye la prueba, la cara del
creador ni la comida real cuando el ángulo depende de que se vea real.

## 1. Qué se graba y qué se genera

Por cada plano de la tabla de `guion`, decide la fuente y anótala:
- **GRABAR** — el creador hablando, sus manos cocinando, el plato real, cualquier demostración
  o prueba. Lo real retiene más y genera confianza; en pauta suele rendir mejor.
- **IA** — metáforas visuales (lo que pasa "dentro" del cuerpo explicado de forma simbólica),
  escenas difíciles de producir (la cocina a las 3 a. m., una ciudad de noche), transiciones,
  texturas, fondos, miniaturas y portadas.
- **STOCK** — si existe y es más barato que generar.

Prohibido generar con IA: personas que parezcan clientes reales, testimonios, antes/después,
resultados, médicos o batas que sugieran respaldo médico, cuerpos con foco en grasa o partes
del cuerpo, e imágenes sexualizadas. Todo pasa por la skill `compliance`. Meta puede etiquetar
contenido generado con IA: el creador debe declararlo cuando la plataforma lo pida.

## 2. Estructura del prompt de IMAGEN

Un párrafo en inglés (los generadores rinden mejor así), con este orden:
1. **Sujeto + acción** concreta.
2. **Entorno** con 2-3 detalles específicos.
3. **Cámara**: plano, ángulo, lente (ej. "shot on iPhone, 26mm, eye level").
4. **Luz**: fuente y hora ("soft window light from the left", "fridge light in dark kitchen").
5. **Estilo**: nativo de celular por defecto ("candid smartphone photo, natural, unedited,
   slight grain") salvo que la pieza pida otra cosa. Evita "cinematic", "8k", "masterpiece":
   delatan IA y se ven a anuncio.
6. **Composición**: espacio libre para texto donde vaya, zona segura de `guion` §6.
7. **Relación de aspecto**: `--ar 9:16` (Reels/Stories) o `--ar 4:5` (Feed), o la sintaxis
   de la herramienta.
8. **Negativo** (si la herramienta lo admite): "no text, no logos, no watermark, no extra
   fingers, no distorted hands, no plastic skin".

Debajo, en español, una línea con qué se busca y cómo se usa en el montaje.

## 3. Estructura del prompt de CLIP (video)

1. **Escena inicial** (como en imagen: sujeto, entorno, luz, estilo).
2. **Movimiento del sujeto** — una sola acción, verbos simples.
3. **Movimiento de cámara** — uno solo: "slow push in", "handheld follow", "static with
   slight handheld sway", "top-down".
4. **Duración**: 3-5 s (un plano de la tabla dura ≤ 3 s; generar un poco más para cortar).
5. **Ritmo y física**: "real-time speed", "natural motion", nada de cámara lenta salvo que el
   guion la pida.
6. **Relación de aspecto** 9:16.
Si se parte de una imagen (image-to-video), el prompt describe SOLO el movimiento.

## 4. Continuidad

- Si varios planos de IA aparecen en el mismo video, fija un **bloque de estilo** (luz, paleta,
  lente, época) y repítelo literal en todos los prompts.
- Si sale una persona generada recurrente, descríbela igual en cada prompt o usa la función de
  referencia de personaje de la herramienta. Nunca la presentes como cliente.
- Los planos de IA se intercalan con planos reales; nunca dos de IA seguidos más de 3 s.

## 5. Entrega

Por cada plano marcado IA, en el chat:
- `# del plano · herramienta sugerida (imagen o clip)`
- prompt en su propio bloque de código
- una línea en español: qué debe verse y dónde va en el montaje
- 1 variante de respaldo si el plano es crítico

Y para cada pieza: **miniatura / primer frame** (prompt o indicación de foto real) y, si es
carrusel, **portada**.

## 6. Adaptación por herramienta

Si el creador dice qué herramienta usa, ajusta la sintaxis (parámetros, longitud, campo
negativo, image-to-video). Si no, entrega el prompt neutro de §2/§3, que funciona en casi
todas. Anota en APRENDIZAJES.md qué herramienta usa y qué prompts dieron buen resultado.

## 7. Flujo Gemini → Google Flow (ecosistema por defecto del creador)

1. **Personajes primero**: en Gemini se genera una imagen de referencia por personaje (cara,
   ropa, entorno). Se guarda y se reutiliza en TODOS los planos donde aparezca.
2. **Fotogramas**: cada plano se genera en Gemini como imagen ultra realista estilo celular
   (§2), en vertical. Si la herramienta no da 9:16, generar más alto y recortar.
3. **Animación en Flow**:
   - *Frames to Video*: la imagen de Gemini como primer fotograma + prompt SOLO de movimiento
     (§3). Opcional: fotograma final para controlar dónde termina.
   - *Ingredients to Video*: cuando el mismo personaje sale en varios planos, se suben sus
     referencias para mantener la consistencia.
   - Los clips salen más largos que el plano: se corta el mejor tramo de 2-3 s.
4. **Diálogo en Flow (Veo)**: si un personaje habla, la frase va entre comillas en el prompt,
   en español latino neutro, ≤ 6 palabras, y se pide "no subtitles, no on-screen text".
   Frases de personaje: solo situacionales, en primera persona, sin nombrar condiciones de
   salud, sin promesas y sin hablarle al espectador ("Otra vez las tres", no "¿Tú también te
   despiertas?"). Lo que vende lo dice la voz en off del creador, no los personajes.
5. **Texto**: nunca se le pide a la IA texto legible (precios, fechas, títulos): se deja
   espacio libre y se pone en edición.
6. **Pantallas**: lo que muestra el producto (plataforma del curso, PDFs) se graba de la
   pantalla real. Una pantalla inventada por IA sería engañosa.

## Lecciones aprendidas
<!-- La skill `aprender` añade aquí lo confirmado. Formato: - AAAA-MM-DD · lección · evidencia -->
- 2026-11-22 · Alternativa a Flow: Kling 4.0 Flash (clips de 5 s 720p con voz y lip sync en español). Los créditos son limitados: generar primero en imagen y animar solo los fotogramas aprobados. · ecosistema del creador
