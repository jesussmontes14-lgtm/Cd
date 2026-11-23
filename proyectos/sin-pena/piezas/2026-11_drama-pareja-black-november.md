# Pieza · Drama de pareja "Volví a sentirme yo" · Black November (pauta en frío)

Carril CONVERSIÓN · 44 s · 9:16 + 4:5 · Riesgo objetivo: BAJO · Estado: guion entregado 2026-11-23.
Producción: Gemini (fotogramas) → Google Flow (animación) · narradora con TTS femenino ·
cierre con voz IA de Jesús · cierre animado y pantalla real de la landing ya renderizados
(scripts/video/bn_cierre_drama.py; S9 = captura real de la landing con el párrafo difuminado).

## Ganchos (0-3 s)
- D1 · "Me dejó cuando ya no era yo." · maleta en la puerta, ella al fondo en el sofá
- D2 · "Seis meses después, quiso volver." · él de noche en el carro mirando la historia de ella
- D3 · "Ya no tenía ganas de nada. Nada." · alarma sonando, ella no se levanta

## Dolores → escenas (sin cuerpo, sin sexo, sin hablarle al espectador)
Cap 01 cansancio (S1) · Cap 04 hinchazón (S2) · Cap 06 antojos (S3) · Cap 09 3 a. m. (S4) ·
Cap 02 "sin ganas" como rechazo a salir, nunca en la cama (S5) · Cap 10 los 40 (S6) ·
Bonus 2 emociones (S8). Fuera: panza, celulitis, "pechos" en hombres (imagen corporal).

## Narración (Laura, 1.ª persona)
S1 "Dormía ocho horas y despertaba agotada." · S2 "Comía poco y me hinchaba igual." ·
S3 "De noche, el dulce me llamaba." · S4 "Y a las tres, despierta otra vez." ·
S6 "Desde los cuarenta, mi cuerpo era otro." · S8 "Esa noche busqué respuestas." ·
S9 "Y encontré SIN PENA." · S10 "Entendí qué me pasaba. Y volví a sentirme yo."
Diálogos en escena: S5 Laura "Estoy cansada." · S7 Andrés "Ya no eres la de antes."
Cierre (voz Jesús): "Eso tiene explicación. Está en SIN PENA. De regalo por Black November:
Mi plan 21 días. Y Lo que como yo, a 4,90 dólares. Hasta el 30 de noviembre. Garantía de 7 días."


## Prompts (Gemini → Google Flow)

Bloque de estilo (pegar al final de cada prompt de Gemini en lugar de [BLOQUE DE ESTILO]):
```
Photorealistic candid smartphone photo, shot on iPhone main camera, natural colors, realistic skin texture with visible pores, no makeup look, slight grain, modest Latin American apartment, vertical 9:16 composition, no text, no logos, no watermark.
```

Referencias de personaje (generar primero; subirlas en cada plano donde aparezcan; en Flow usar Ingredients to Video):
- LAURA: `Character reference portrait of LAURA: Latin American woman, 38 years old, shoulder-length dark wavy hair, light olive skin, natural face without makeup, wearing a loose grey cotton t-shirt, neutral tired expression, plain apartment background, soft window light. [BLOQUE DE ESTILO]`
- ANDRÉS: `Character reference portrait of ANDRÉS: Latin American man, 40 years old, short black hair, light stubble, wearing a navy blue t-shirt, neutral serious expression, plain apartment background, natural daylight. [BLOQUE DE ESTILO]`

| Plano | Gemini (fotograma) | Flow (movimiento y audio) |
|-------|--------------------|---------------------------|
| D1 | Apartment entrance at dusk, ANDRÉS from the reference standing at the open front door holding a packed suitcase, looking back with a sad serious face; in the soft-focus background LAURA from the reference sits alone on the sofa looking down, warm dim lamp light. [BLOQUE DE ESTILO] | He turns away and walks out, closing the door behind him; she stays still on the sofa. Static camera with slight handheld sway, real-time speed. Audio: door closing, quiet room, no dialogue. No subtitles. |
| D2 | ANDRÉS from the reference sitting in a parked car at night, face lit by his phone screen, staring at it with a regretful expression, city lights blurred through the windshield. [BLOQUE DE ESTILO] | He scrolls slowly, stops, and exhales looking at the screen. Slow push in, real-time speed. Audio: quiet car interior, distant traffic, no dialogue. No subtitles. |
| D3 | Dark bedroom early morning, phone alarm glowing on the nightstand, LAURA from the reference lying in bed with eyes open, not moving, staring blankly, cold blue light through curtains. [BLOQUE DE ESTILO] | The alarm keeps ringing; she slowly pulls the blanket over her face. Static camera, real-time speed. Audio: phone alarm ringing, no dialogue. No subtitles. |
| S1 | LAURA from the reference sitting on the edge of her bed at 6:30 am, shoulders slumped, rubbing her eyes, phone in hand, cold morning light, medium shot from the doorway. [BLOQUE DE ESTILO] | She turns off the alarm and stays sitting, exhausted, letting her head drop. Static camera with slight sway, real-time speed. Audio: morning silence, no dialogue. No subtitles. |
| S2 | Lunch at a small dining table, LAURA from the reference pushing away a half-eaten plate with an uncomfortable expression, ANDRÉS across the table eating and glancing at her, midday window light, medium shot at table height. [BLOQUE DE ESTILO] | She pushes the plate away and sighs, leaning back in the chair; he looks at her in silence. Static camera, real-time speed. Audio: cutlery sounds, no dialogue. No subtitles. (Sin manos en la barriga.) |
| S3 | View from inside an open refrigerator into a dark kitchen at night, a woman's hand reaching for a chocolate bar, only the cold fridge light illuminating the hand and shelves. [BLOQUE DE ESTILO] | The hand hesitates for a second, then grabs the chocolate bar. Static camera, real-time speed. Audio: fridge hum, wrapper crinkle, no dialogue. No subtitles. |
| S4 | Top-down shot of LAURA from the reference lying awake in bed in a dark bedroom at night, eyes open staring at the ceiling, face lit only by her phone screen. [BLOQUE DE ESTILO] | She blinks slowly, checks the phone and drops her arm on the bed. Very slow push in from above. Audio: silent night, faint clock ticking, no dialogue. No subtitles. |
| S5 | Living room evening, ANDRÉS from the reference sitting on the sofa hugging LAURA from the reference from the side with a hopeful smile, she looks tired and distant, warm lamp light, medium shot. [BLOQUE DE ESTILO] | She gently pulls away, stands up and walks out of frame; he stays on the sofa, disappointed. Static camera with slight sway, real-time speed. Audio: quiet room; she says softly in Latin American Spanish: "Estoy cansada." No subtitles, no on-screen text. |
| S6 | LAURA from the reference at a kitchen table in front of a small birthday cake with a single "40" candle lit, forced polite smile, a few people blurred in the background, warm evening light, close-up. [BLOQUE DE ESTILO] | She blows out the candle and her smile fades as she looks down. Static camera, real-time speed. Audio: soft distant clapping, no dialogue. No subtitles. |
| S7 | ANDRÉS from the reference standing at the front door with a suitcase, looking back toward the camera with a hurt, serious face, hallway light, medium close-up. [BLOQUE DE ESTILO] | He looks back and says calmly in Latin American Spanish: "Ya no eres la de antes." Then he leaves and the door closes. Static camera, real-time speed. Audio: door closing after the line. No subtitles, no on-screen text. (Generar 3-4 tomas.) |
| S8 | LAURA from the reference alone in a dark kitchen at night, sitting on the floor against the cabinets, tears on her face, picking up her phone, only the phone light on her face. [BLOQUE DE ESTILO] | She wipes her tears and starts typing on the phone, determined. Slow push in, real-time speed. Audio: quiet night, soft breathing, no dialogue. No subtitles. |
| S10a | LAURA from the reference, now wearing a mustard sweater, cooking a colorful healthy dish in a bright kitchen, focused and relaxed, morning sunlight, medium shot. [BLOQUE DE ESTILO] | She stirs the pan with natural continuous motion. Handheld follow, real-time speed. Audio: ambient sound only, no dialogue. No subtitles. |
| S10b | LAURA from the reference walking energetically on a quiet tree-lined street at sunrise, light jacket, earphones, natural smile, medium-wide shot from the front. [BLOQUE DE ESTILO] | She walks toward the camera with energy. Handheld follow, real-time speed. Audio: ambient sound only, no dialogue. No subtitles. |
| S10c | LAURA from the reference laughing at a café table with two female friends around 40, natural afternoon light, candid moment, medium shot. [BLOQUE DE ESTILO] | They laugh and gesture naturally. Handheld, real-time speed. Audio: ambient café sound only, no dialogue. No subtitles. |
| S11 | ANDRÉS from the reference alone on his sofa at night, looking at his phone screen showing a social media story, regretful expression, dim light. [BLOQUE DE ESTILO] | He watches, hesitates, then types a short message and sends it. Slow push in, real-time speed. Audio: quiet room, phone typing sounds, no dialogue. No subtitles. ("¿Podemos hablar?" va en edición.) |
| S12 | LAURA from the reference in her bright kitchen wearing the mustard sweater, a phone on the counter lighting up with a notification, she glances at it while cooking, calm, morning light, medium shot. [BLOQUE DE ESTILO] | She reads the notification, smiles calmly, turns the phone face down and keeps cooking. Static camera with slight sway, real-time speed. Audio: kitchen sounds, no dialogue. No subtitles. |

S9 (pantalla real de la landing) y el cierre de 11 s ya están renderizados: se regeneran con
`scripts/video/bn_cierre_drama.py` y una captura de la landing con el párrafo de "sin ganas" difuminado.

## Montaje
Orden y tiempos: tabla de planos de arriba (D# 0-3 · S1 3-5,5 · S2 -8 · S3 -10,5 · S4 -13 · S5 -15,5 ·
S6 -18 · S7 -20,5 · S8 -23 · S9 -25 · S10a/b/c -28,5 · S11 -31 · S12 -33 · cierre 33-44).
Narradora: TTS femenino en español latino. Cierre: voz IA de Jesús. Subtítulos quemados
palabra por palabra, mayúsculas, 62 % del alto. Música de piano suave que sube en S10.
Con D2 añadir el texto "6 MESES ANTES" en el segundo 3. Exportar 3 versiones (D1, D2, D3) en 9:16 y 4:5.
