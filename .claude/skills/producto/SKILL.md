---
name: producto
description: Convierte la información de un producto o infoproducto (link de Hotmart u otra página de venta, texto, PDF o notas sueltas) en su carpeta de proyecto lista para crear contenido y anuncios — oferta, avatar, dolores, deseos, objeciones, niveles de consciencia y mapa de ángulos. Úsala cuando el creador presente un producto nuevo, pase un link de venta, cambie precio/oferta/bonos, o cuando PRODUCTO.md esté incompleto.
---

# Skill: producto

Objetivo: que el creador solo tenga que pasar el producto. De aquí sale todo lo que las demás
skills necesitan para trabajar sin volver a preguntar.

## 1. Captura

1. Si hay link: descárgalo (curl con User-Agent de navegador) y extrae el texto visible.
   Si el host está bloqueado por la red de la sesión, sigue el proceso del entorno para
   pedir acceso a ese host exacto; no inventes el contenido.
2. Si hay texto, PDF o notas: úsalos tal cual.
3. Copia LITERAL todo lo verificable: nombre, precio, moneda, formato, contenido, bonos,
   order bumps, garantía, credenciales, cifras, testimonios, CTA, disclaimers.
   Literal significa literal: no redondees cifras ni mejores frases.

## 2. Análisis (lo que la página no dice explícitamente)

Deriva, marcando cada punto como **[derivado]** para distinguirlo de lo literal:
- **Avatar**: 1-3 perfiles concretos (edad, situación, momento del día en que sufre el problema).
- **Dolores**: en palabras del avatar, no del vendedor ("me hincho aunque coma poco").
- **Deseos**: el estado B que compra, llevado hasta la emoción.
- **Objeciones**: precio, tiempo, "ya lo intenté", desconfianza, vergüenza, "eso no es para mí".
- **Niveles de consciencia** (Schwartz): qué le dices a quien no sabe que tiene el problema,
  a quien lo sabe, a quien conoce soluciones y a quien conoce este producto.
- **Mecanismo**: por qué este producto funciona distinto (solo con lo que el producto
  realmente ofrece).
- **Mapa de ángulos**: cada módulo/capítulo/beneficio convertido en 1-2 ángulos de contenido,
  con su carril sugerido y su nivel de riesgo de compliance (bajo / medio / alto).
- **Economía de la pauta**: precio, order bumps y la fórmula del CPA de equilibrio
  (ver skill `anuncio-meta` §5), con los datos que falten como placeholder.
- **Riesgos de compliance** del producto y de su página de venta (pasa por skill `compliance`).

## 3. Escritura

1. Crea `proyectos/<slug>/` copiando `proyectos/_plantilla/` y rellena PRODUCTO.md.
2. VOZ.md: si solo hay copy escrito de la página, extrae registro, vocabulario y frases y
   márcalo como **provisional — sacado del copy, no de su habla**. Se reemplaza en cuanto
   haya transcripciones o videos suyos.
3. Lista en UN bloque lo que falta y que cambia el trabajo (países, presupuesto, comisión,
   si sale a cámara, testimonios con permiso…).
4. Commit + push: "Añade proyecto <slug>" (o "Actualiza oferta de <slug>").

## 4. Actualizaciones

Si cambia precio, bonos, garantía o contenido: actualiza PRODUCTO.md, revisa el mapa de
ángulos y anota el cambio con fecha en APRENDIZAJES.md (los resultados previos al cambio
dejan de ser comparables 1:1).

## Lecciones aprendidas
<!-- La skill `aprender` añade aquí lo confirmado. Formato: - AAAA-MM-DD · lección · evidencia -->
