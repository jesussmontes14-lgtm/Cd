#!/usr/bin/env python3
"""Cierre de 11 s para el drama de pareja (SIN PENA · Black November).
Reutiliza las escenas de bn_kinetic: puente "Eso tiene explicación" + regalo + Lo que como yo + cierre.
Uso: python3 scripts/video/bn_cierre_drama.py SALIDA_DIR
"""
import os, subprocess, sys
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(__file__))
import bn_kinetic as K

DUR = 11.0
def puente(d, W, cy, t):
    a = K.scene_alpha(t, 0, 2.5, fin=0.2)
    if a <= 0: return
    K.draw_center_text(d, W / 2, cy - 240, "Eso tiene explicación.", K.F("black", 104), K.WHITE, a, 940, 1.06,
                       dy=30 * (1 - K.ease_out(K.prog(t, 0, .4))))
    f = K.F("black", 92); tw, th, off = K.text_size(d, "SIN PENA", f)
    a2 = a * K.ease_out(K.prog(t, .6, .3))
    x0, y0 = W / 2 - tw / 2 - 44, cy + 60
    d.rounded_rectangle((x0, y0, x0 + tw + 88, y0 + th + 64), radius=30, fill=K.rgba((26, 10, 12), a2), outline=K.rgba((90, 20, 24), a2), width=3)
    d.text((W / 2 - tw / 2, y0 + 32 - off), "SIN PENA", font=f, fill=K.rgba(K.WHITE, a2))

def frame(W, H, t, bg):
    cy = 758 if H == 1920 else 700
    sy = 1.0 if H == 1920 else 0.86
    layer = Image.new("RGBA", (W, int(H / sy)), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    lcy = cy / sy
    puente(d, W, lcy, t)
    if t >= 2.5: K.regalo(d, W, lcy, t - 2.5 + 19.0)
    if t >= 5.5: K.lqcy(d, W, lcy, t - 5.5 + 22.0)
    if t >= 8.0: K.cierre(d, W, lcy, t - 8.0 + 24.5)
    if sy != 1:
        layer = layer.resize((int(W * sy), H), Image.LANCZOS)
        pad = Image.new("RGBA", (W, H), (0, 0, 0, 0)); pad.alpha_composite(layer, ((W - layer.size[0]) // 2, 0)); layer = pad
    return Image.alpha_composite(bg, layer).convert("RGB")

def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out_dir, exist_ok=True)
    for fk, (W, H) in {"916": (1080, 1920), "45": (1080, 1350)}.items():
        bg = K.make_bg(W, H, 758 if H == 1920 else 700).convert("RGBA")
        out = os.path.join(out_dir, f"SINPENA_DRAMA_cierre_{fk}.mp4")
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                              "-r", str(K.FPS), "-i", "-", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-shortest",
                              "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart", out],
                             stdin=subprocess.PIPE)
        for i in range(int(DUR * K.FPS)):
            p.stdin.write(frame(W, H, i / K.FPS, bg).tobytes())
        p.stdin.close(); p.wait(); print("listo:", out)

if __name__ == "__main__":
    main()
