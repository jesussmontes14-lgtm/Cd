#!/usr/bin/env python3
"""Video de texto animado · SIN PENA Black November (concepto H).

Genera 3 versiones de gancho (H1, H2, H3) en 9:16 (1080x1920) y 4:5 (1080x1350),
con el estilo de la landing: fondo oscuro, rojo #CC1111, tipografía en negrita.

Uso:  python3 scripts/video/bn_kinetic.py SALIDA_DIR [--solo H2] [--formato 916|45]
"""
import math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FPS = 30
DUR = 27.5
FONT_DIR = "/usr/share/fonts/opentype/inter"
BG = (11, 11, 12)
CARD = (22, 22, 25)
CARD_BORDER = (44, 44, 50)
RED = (204, 17, 17)
RED_SOFT = (60, 14, 16)
WHITE = (255, 255, 255)
SLATE = (203, 213, 225)
MUTED = (140, 148, 160)

_fonts = {}
def F(weight, size):
    key = (weight, size)
    if key not in _fonts:
        name = {"black": "InterDisplay-Black", "xb": "InterDisplay-ExtraBold", "b": "InterDisplay-Bold",
                "sb": "InterDisplay-SemiBold", "m": "InterDisplay-Medium", "r": "InterDisplay-Regular"}[weight]
        _fonts[key] = ImageFont.truetype(f"{FONT_DIR}/{name}.otf", size)
    return _fonts[key]

# ---------- easing ----------
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease_out(x): x = clamp(x); return 1 - (1 - x) ** 3
def ease_in_out(x): x = clamp(x); return 3 * x * x - 2 * x * x * x
def prog(t, start, dur): return clamp((t - start) / dur)

# ---------- drawing helpers (all on an RGBA layer, alpha 0-1) ----------
def rgba(c, a): return (c[0], c[1], c[2], int(255 * clamp(a)))

def text_size(d, s, font):
    b = d.textbbox((0, 0), s, font=font)
    return b[2] - b[0], b[3] - b[1], b[1]

def wrap(d, s, font, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if text_size(d, test, font)[0] <= maxw or not cur:
            cur = test
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def draw_center_text(d, cx, y, s, font, color, alpha, maxw=900, spacing=1.12, dy=0):
    """Draws wrapped, centered text starting at y. Returns the bottom y."""
    lines = wrap(d, s, font, maxw)
    lh = int(font.size * spacing)
    for i, ln in enumerate(lines):
        w, h, off = text_size(d, ln, font)
        d.text((cx - w / 2, y + i * lh - off + dy), ln, font=font, fill=rgba(color, alpha))
    return y + len(lines) * lh

def block_height(d, s, font, maxw=900, spacing=1.12):
    return len(wrap(d, s, font, maxw)) * int(font.size * spacing)

def pill(d, cx, y, s, font, alpha, fg=RED, bg=RED_SOFT, padx=26, pady=12):
    w, h, off = text_size(d, s, font)
    x0, y0 = cx - w / 2 - padx, y
    x1, y1 = cx + w / 2 + padx, y + h + 2 * pady
    d.rounded_rectangle((x0, y0, x1, y1), radius=(y1 - y0) / 2, fill=rgba(bg, alpha))
    d.text((cx - w / 2, y + pady - off), s, font=font, fill=rgba(fg, alpha))
    return y1

def gift(d, cx, cy, size, alpha, open_amt=0.0):
    w = size; h = size * 0.78
    x0, y0 = cx - w / 2, cy - h / 2 + size * 0.12
    d.rounded_rectangle((x0, y0, x0 + w, y0 + h), radius=size * 0.08, fill=rgba(CARD, alpha),
                        outline=rgba(CARD_BORDER, alpha), width=4)
    lid_y = y0 - size * 0.16 - open_amt * size * 0.25
    d.rounded_rectangle((x0 - size * 0.05, lid_y, x0 + w + size * 0.05, lid_y + size * 0.2),
                        radius=size * 0.05, fill=rgba((30, 30, 34), alpha), outline=rgba(CARD_BORDER, alpha), width=4)
    rw = size * 0.13
    d.rectangle((cx - rw / 2, y0, cx + rw / 2, y0 + h), fill=rgba(RED, alpha))
    d.rectangle((cx - rw / 2, lid_y, cx + rw / 2, lid_y + size * 0.2), fill=rgba(RED, alpha))
    bw = size * 0.3
    d.ellipse((cx - bw * 1.05, lid_y - bw * 0.62, cx - rw * 0.2, lid_y + bw * 0.08), outline=rgba(RED, alpha), width=int(size * 0.07))
    d.ellipse((cx + rw * 0.2, lid_y - bw * 0.62, cx + bw * 1.05, lid_y + bw * 0.08), outline=rgba(RED, alpha), width=int(size * 0.07))

def calendar(d, cx, cy, size, alpha, day="30", month="NOV"):
    w = size; h = size * 1.05
    x0, y0 = cx - w / 2, cy - h / 2
    d.rounded_rectangle((x0, y0, x0 + w, y0 + h), radius=size * 0.1, fill=rgba(CARD, alpha),
                        outline=rgba(CARD_BORDER, alpha), width=4)
    d.rounded_rectangle((x0, y0, x0 + w, y0 + h * 0.28), radius=size * 0.1, fill=rgba(RED, alpha))
    d.rectangle((x0, y0 + h * 0.18, x0 + w, y0 + h * 0.28), fill=rgba(RED, alpha))
    f = F("xb", int(size * 0.17)); tw, th, off = text_size(d, month, f)
    d.text((cx - tw / 2, y0 + h * 0.14 - th / 2 - off), month, font=f, fill=rgba(WHITE, alpha))
    f = F("black", int(size * 0.5)); tw, th, off = text_size(d, day, f)
    d.text((cx - tw / 2, y0 + h * 0.64 - th / 2 - off), day, font=f, fill=rgba(WHITE, alpha))

def chapter_card(d, cx, y, w, num, title, alpha, dx=0):
    x0 = cx - w / 2 + dx
    h = 205
    d.rounded_rectangle((x0, y, x0 + w, y + h), radius=36, fill=rgba(CARD, alpha), outline=rgba(CARD_BORDER, alpha), width=3)
    pf = F("b", 30); tw, th, off = text_size(d, f"Capítulo {num}", pf)
    d.rounded_rectangle((x0 + 40, y + 36, x0 + 40 + tw + 44, y + 36 + th + 26), radius=26, fill=rgba(RED_SOFT, alpha))
    d.text((x0 + 62, y + 49 - off), f"Capítulo {num}", font=pf, fill=rgba(RED, alpha))
    tf = F("b", 44)
    lines = wrap(d, title, tf, w - 80)[:1]
    for i, ln in enumerate(lines):
        _, _, off = text_size(d, ln, tf)
        d.text((x0 + 40, y + 112 + i * 56 - off), ln, font=tf, fill=rgba(WHITE, alpha))
    return y + h

def button(d, cx, y, s, alpha, scale=1.0):
    f = F("xb", int(48 * scale)); tw, th, off = text_size(d, s, f)
    w, h = tw + 120 * scale, th + 64 * scale
    d.rounded_rectangle((cx - w / 2, y, cx + w / 2, y + h), radius=28 * scale, fill=rgba(RED, alpha))
    d.text((cx - tw / 2, y + (h - th) / 2 - off), s, font=f, fill=rgba(WHITE, alpha))
    return y + h

# ---------- background ----------
def make_bg(W, H, cy):
    bg = Image.new("RGB", (W, H), BG)
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    r = int(W * 0.55)
    gd.ellipse((W / 2 - r, cy - r, W / 2 + r, cy + r), fill=70)
    glow = glow.filter(ImageFilter.GaussianBlur(220))
    red = Image.new("RGB", (W, H), (120, 10, 12))
    return Image.composite(red, bg, glow)

# ---------- scenes ----------
TIMES = [("7:00", "Cansancio después de dormir 8 horas"),
         ("14:00", "Hinchazón después de comer"),
         ("23:00", "Antojos de dulce de noche"),
         ("3:00", "Despertar sin razón")]

def scene_alpha(t, start, end, fin=0.25, fout=0.2):
    return min(ease_out(prog(t, start, fin)), 1 - ease_in_out(prog(t, end - fout, fout)))

def hook(d, W, cy, t, variant):
    a = scene_alpha(t, 0, 3.0, fin=0.01)
    if a <= 0: return
    cx = W / 2
    if variant == "H1":
        y = cy - 260
        pill(d, cx, y + 20 * (1 - ease_out(prog(t, 0, .4))), "BLACK NOVEMBER · SIN PENA", F("b", 34), a)
        f = F("black", 112)
        bh = block_height(d, "Esto es todo lo que te llevas.", f, 920, 1.05)
        draw_center_text(d, cx, y + 110, "Esto es todo lo que te llevas.", f, WHITE, a * ease_out(prog(t, .1, .4)), 920, 1.05,
                         dy=40 * (1 - ease_out(prog(t, .1, .5))))
        ay = y + 150 + bh + 18 * math.sin(t * 6)
        aa = a * ease_out(prog(t, .6, .3))
        d.polygon([(cx - 46, ay), (cx + 46, ay), (cx, ay + 56)], fill=rgba(RED, aa))
    elif variant == "H2":
        s = ease_out(prog(t, 0, .5))
        gift(d, cx, cy - 200, 250 * (0.85 + 0.15 * s), a * s, open_amt=0.35 * ease_out(prog(t, 1.6, .8)))
        f = F("black", 128)
        draw_center_text(d, cx, cy + 0, "BLACK NOVEMBER", f, RED, a * ease_out(prog(t, .2, .4)), 980, 1.0,
                         dy=30 * (1 - ease_out(prog(t, .2, .5))))
        draw_center_text(d, cx, cy + 290, "SIN PENA trae regalo", F("xb", 76), WHITE, a * ease_out(prog(t, .5, .4)), 940,
                         dy=30 * (1 - ease_out(prog(t, .5, .5))))
    else:  # H3
        pill(d, cx, cy - 400, "ÚLTIMO AVISO", F("b", 38), a * ease_out(prog(t, 0, .3)))
        s = ease_out(prog(t, .1, .5))
        calendar(d, cx, cy - 90, 380 * (0.85 + 0.15 * s), a * s)
        draw_center_text(d, cx, cy + 170, "Esto termina el 30 de noviembre.", F("black", 84), WHITE,
                         a * ease_out(prog(t, .45, .4)), 940, 1.08, dy=30 * (1 - ease_out(prog(t, .45, .5))))

def clocks(d, W, cy, t):
    start = 3.0
    for i, (hh, txt) in enumerate(TIMES):
        s0 = start + i * 2.0
        if not (s0 - 0.01 <= t < s0 + 2.0): continue
        lt = t - s0
        a = min(ease_out(prog(lt, 0, .2)), 1 - ease_in_out(prog(lt, 1.8, .2)))
        dx = 120 * (1 - ease_out(prog(lt, 0, .35)))
        cx = W / 2 + dx
        f = F("black", 260)
        tw, th, off = text_size(d, hh, f)
        d.text((cx - tw / 2, cy - 330 - off), hh, font=f, fill=rgba(RED, a))
        draw_center_text(d, cx, cy + 10, txt, F("xb", 92), WHITE, a * ease_out(prog(lt, .12, .3)), 900, 1.08)
        # dots progress
        for k in range(4):
            r = 11
            x = W / 2 - 75 + k * 50
            d.ellipse((x - r, cy + 330 - r, x + r, cy + 330 + r), fill=rgba(RED if k <= i else CARD_BORDER, a))

def explain(d, W, cy, t):
    a = scene_alpha(t, 11.0, 19.0)
    if a <= 0: return
    cx = W / 2
    lt = t - 11.0
    # headline
    hdr_a = a * ease_out(prog(lt, 0, .3))
    if lt < 2.6:
        draw_center_text(d, cx, cy - 220, "SIN PENA te explica por qué pasa.", F("black", 96), WHITE, hdr_a, 960, 1.06,
                         dy=30 * (1 - ease_out(prog(lt, 0, .4))))
        draw_center_text(d, cx, cy + 90, "En simple.", F("black", 100), RED, a * ease_out(prog(lt, .7, .3)), 920)
        return
    lt2 = lt - 2.6
    fade_in = ease_out(prog(lt2, 0, .25))
    draw_center_text(d, cx, cy - 470, "10 capítulos en video", F("black", 70), WHITE, a * fade_in, 940)
    caps = [("04", "Hinchazón y gases después de comer"), ("06", "Los antojos de dulce de noche"),
            ("09", "Despertar a las 3 a. m. sin razón")]
    y = cy - 375
    for i, (n, ttl) in enumerate(caps):
        ca = a * ease_out(prog(lt2, .15 + i * .3, .35))
        dx = 160 * (1 - ease_out(prog(lt2, .15 + i * .3, .45)))
        y = chapter_card(d, cx, y, 900, n, ttl, ca, dx) + 20
    draw_center_text(d, cx, y + 4, "+ 7 capítulos más", F("sb", 42), SLATE, a * ease_out(prog(lt2, 1.2, .3)), 900)
    ra = a * ease_out(prog(lt2, 1.8, .35))
    draw_center_text(d, cx, y + 70, "3 recetas de chef por capítulo", F("black", 56), RED, ra, 980,
                     dy=24 * (1 - ease_out(prog(lt2, 1.8, .4))))

def regalo(d, W, cy, t):
    a = scene_alpha(t, 19.0, 22.0)
    if a <= 0: return
    cx, lt = W / 2, t - 19.0
    pill(d, cx, cy - 470, "DE REGALO", F("b", 40), a * ease_out(prog(lt, 0, .3)))
    s = ease_out(prog(lt, .05, .45))
    gift(d, cx, cy - 130, 230 * (0.8 + 0.2 * s), a * s, open_amt=0.3 * ease_out(prog(lt, .8, .6)))
    draw_center_text(d, cx, cy + 70, "Mi plan 21 días", F("black", 120), WHITE, a * ease_out(prog(lt, .3, .35)), 960,
                     dy=30 * (1 - ease_out(prog(lt, .3, .45))))
    draw_center_text(d, cx, cy + 225, "por Black November", F("sb", 52), SLATE, a * ease_out(prog(lt, .6, .3)), 940)

def lqcy(d, W, cy, t):
    a = scene_alpha(t, 22.0, 24.5)
    if a <= 0: return
    cx, lt = W / 2, t - 22.0
    draw_center_text(d, cx, cy - 380, "Y además", F("sb", 52), SLATE, a * ease_out(prog(lt, 0, .25)), 900)
    draw_center_text(d, cx, cy - 290, "Lo que como yo", F("black", 112), WHITE, a * ease_out(prog(lt, .1, .3)), 960,
                     dy=30 * (1 - ease_out(prog(lt, .1, .4))))
    draw_center_text(d, cx, cy - 140, "42 recetas de chef", F("xb", 70), SLATE, a * ease_out(prog(lt, .3, .3)), 940)
    s = ease_out(prog(lt, .55, .35))
    f = F("black", int(210 * (0.8 + 0.2 * s)))
    tw, th, off = text_size(d, "USD 4.90", f)
    d.text((cx - tw / 2, cy + 20 - off), "USD 4.90", font=f, fill=rgba(RED, a * s))

def cierre(d, W, cy, t):
    a = ease_out(prog(t, 24.5, .3))
    if a <= 0: return
    cx, lt = W / 2, t - 24.5
    f = F("black", 92); tw, th, off = text_size(d, "SIN PENA", f)
    bx0, by0 = cx - tw / 2 - 44, cy - 430
    d.rounded_rectangle((bx0, by0, bx0 + tw + 88, by0 + th + 64), radius=30, fill=rgba((26, 10, 12), a),
                        outline=rgba((90, 20, 24), a), width=3)
    d.text((cx - tw / 2, by0 + 32 - off), "SIN PENA", font=f, fill=rgba(WHITE, a))
    y = by0 + th + 64 + 60
    y = draw_center_text(d, cx, y, "USD 14.90 · pago único", F("black", 76), WHITE, a * ease_out(prog(lt, .1, .3)), 960)
    y = draw_center_text(d, cx, y + 10, "Garantía de 7 días", F("sb", 54), SLATE, a * ease_out(prog(lt, .25, .3)), 940)
    y = draw_center_text(d, cx, y + 10, "Hasta el 30 de noviembre", F("xb", 60), RED, a * ease_out(prog(lt, .4, .3)), 940)
    pulse = 1 + 0.04 * math.sin(max(0, lt - .6) * 7)
    button(d, cx, y + 60, "Toca Comprar", a * ease_out(prog(lt, .6, .3)), pulse)

def render(variant, W, H, out):
    cy = 758 if H == 1920 else 700
    bg = make_bg(W, H, cy).convert("RGBA")
    scale_y = 1.0 if H == 1920 else 0.86
    cmd = ["ffmpeg", "-y", "-loglevel", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
           "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    n = int(DUR * FPS)
    for i in range(n):
        t = i / FPS
        layer = Image.new("RGBA", (W, int(H / scale_y)) if scale_y != 1 else (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        lcy = cy / scale_y if scale_y != 1 else cy
        hook(d, W, lcy, t, variant)
        clocks(d, W, lcy, t)
        explain(d, W, lcy, t)
        regalo(d, W, lcy, t)
        lqcy(d, W, lcy, t)
        cierre(d, W, lcy, t)
        if scale_y != 1:
            lw, lh = layer.size
            layer = layer.resize((int(lw * scale_y), H), Image.LANCZOS)
            pad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            pad.alpha_composite(layer, ((W - layer.size[0]) // 2, 0))
            layer = pad
        frame = Image.alpha_composite(bg, layer).convert("RGB")
        p.stdin.write(frame.tobytes())
    p.stdin.close()
    if p.wait() != 0:
        sys.exit(f"ffmpeg falló en {out}")

def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out_dir, exist_ok=True)
    variants = ["H1", "H2", "H3"]
    if "--solo" in sys.argv: variants = [sys.argv[sys.argv.index("--solo") + 1]]
    formats = {"916": (1080, 1920), "45": (1080, 1350)}
    if "--formato" in sys.argv: formats = {k: v for k, v in formats.items() if k == sys.argv[sys.argv.index("--formato") + 1]}
    for v in variants:
        for fk, (W, H) in formats.items():
            out = os.path.join(out_dir, f"SINPENA_BLACKNOV_{v}_{fk}_2026-11.mp4")
            render(v, W, H, out)
            print("listo:", out)

if __name__ == "__main__":
    main()
