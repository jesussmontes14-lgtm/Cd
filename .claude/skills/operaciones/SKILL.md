---
name: operaciones
description: Operar Hotmart, Hotmart Pages, el Administrador de anuncios de Meta y los PDF de presentación — crear productos, ofertas, combos y cupones, sacar links de pago, editar la landing, instalar o verificar el píxel, subir creativos y editar precios en PDF. Úsala cuando la tarea sea hacer cambios en esas plataformas o archivos (no para crear contenido).
---

# Skill: operaciones

## 0. Seguridad (no se rompe nunca)
- Nunca escribir contraseñas ni pedirlas en el chat.
- Nunca pulsar botones de compra o pago.
- Nunca aceptar términos o condiciones sin un "sí" explícito del creador en el chat
  (ej. "Finalizar registro" de un producto en Hotmart acepta el Término de Tratamiento de Datos).
- Este repo es público: IDs de cuentas, cupones, teléfonos, gasto y links privados no se
  commitean.

## 1. Hotmart
- **Campos de precio o porcentaje**: se llenan desde los centavos y pierden teclas si se
  escribe rápido. Funciona: clic, End, borrar, y teclear dígito por dígito con End entre
  teclas (7,0,0,0,0 → 700,00).
- **Formularios dentro de iframe** (combos): find/JS no alcanzan los inputs; usar clics y
  teclado. Guardan texto en caché entre creaciones: borrar antes de escribir.
- **Link de pago**: Fijación de precios y ofertas → menú ⋮ de la oferta → "Links de esta
  oferta" (formato `pay.hotmart.com/<código>?off=<oferta>`).
- **Combos**: solo admiten cursos, suscripciones o eventos con área de miembros; los ebooks
  no entran (se entregan por otro canal y se dice en la descripción).
- **Servicio Online** puede no estar habilitado en la cuenta: usar "Curso Online".
- **Checkout embebido** (`checkoutMode=10`) dispara eventos del píxel al cargar: usar links
  directos al checkout.

## 2. Hotmart Pages
- Editor IA: se edita escribiendo instrucciones en el chat del editor y luego
  Publicar → Publicar página.
- Tras publicar, verificar en la página pública (no en el editor) que el cambio está y que
  `fbq` existe si hay píxel.

## 3. Meta Ads
- Videos de más de ~3,8 MB pueden requerir subirse en trozos y reensamblarse.
- El diálogo "reemplazar medio" de un anuncio de imagen solo acepta imágenes: quitar el medio
  y usar "Agregar video".
- Publicaciones existentes creadas para un anuncio pueden no servir para Instagram.
- Antes de optimizar a un evento, verificar que se dispara con la acción real
  (Administrador de eventos + compra de prueba con cupón 100 %).

## 4. PDF de presentación (precios y links)
Método probado con pypdf + reportlab:
1. Borrar los strings de precio del content stream (`(texto) Tj` → `() Tj`) en las páginas
   afectadas.
2. Superponer el texto nuevo con la misma fuente (ej. Poppins Bold) y color, centrado en las
   tarjetas. Las versiones en otro idioma pueden tener las tarjetas desplazadas: medir.
3. Reemplazar las URI de las anotaciones de link por las nuevas.
4. Verificar con extracción de texto que no queda ningún precio ni link viejo.

## Lecciones aprendidas
<!-- La skill `aprender` añade aquí lo confirmado. Formato: - AAAA-MM-DD · lección · evidencia -->
