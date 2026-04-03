"""
Generate Hellschreiber background image of SSA logo.

Feld-Hell (Hellschreiber) is a facsimile-based teleprinter system where
each character is transmitted column by column as a series of dots.
Characteristic appearance: columns of dots forming text, printed on a
moving paper tape with a double-strike effect (2-revolution motor cycle).

Run from the repository root:
    python3 images/generate_hellschreiber.py

Requires: Pillow, numpy, pdftoppm (poppler-utils)
"""
import numpy as np
from PIL import Image, ImageFilter
import subprocess, os

_HERE     = os.path.dirname(os.path.abspath(__file__))
LOGO_PDF  = os.path.join(_HERE, "ssa-logotyp.pdf")
OUT_PNG   = os.path.join(_HERE, "hellschreiber-ssa.png")

PAGE_W, PAGE_H = 1240, 1754   # A4 at 150 DPI
np.random.seed(1928)           # Year Hellschreiber was invented

# 1 ── Load logo ────────────────────────────────────────────────────────────
import tempfile
_tmpdir = tempfile.gettempdir()
ppm_base = os.path.join(_tmpdir, "ssa_hell_gen")
ppm = ppm_base + "-1.ppm"
if not os.path.exists(ppm):
    subprocess.run(["pdftoppm", "-r", "200", LOGO_PDF, ppm_base], check=True)
logo_gray = np.array(Image.open(ppm).convert("L"), dtype=np.float32)
logo_ink  = (logo_gray < 200).astype(np.float32)

# Crop to content
r = np.any(logo_ink, axis=1);  c = np.any(logo_ink, axis=0)
r0, r1 = np.where(r)[0][[0,-1]];  c0, c1 = np.where(c)[0][[0,-1]]
logo_ink = logo_ink[r0:r1+1, c0:c1+1]
print(f"Logo content: {logo_ink.shape}")

# 2 ── Scale to fill page height ────────────────────────────────────────────
lh, lw = logo_ink.shape
scale = PAGE_H / lh
tw = int(lw * scale)
logo_scaled = np.array(
    Image.fromarray((logo_ink*255).astype(np.uint8)).resize((tw, PAGE_H), Image.LANCZOS),
    dtype=np.float32) / 255.0
print(f"Scaled: {logo_scaled.shape}")

# 3 ── Hellschreiber column scan ────────────────────────────────────────────
# Feld-Hell: column-by-column scanning with double-strike (2-revolution motor)
DOT = 8   # pixels per Hell "dot" vertically

def hell_col(col, dot_px, half_h):
    n = len(col)
    n_cells = n // dot_px
    cells = np.zeros(n_cells)
    for i in range(n_cells):
        seg = col[i*dot_px:(i+1)*dot_px]
        cells[i] = 1.0 if seg.mean() > 0.30 else 0.0
    # Double-strike offset
    off = n_cells // 2
    ds = np.zeros(n_cells)
    ds[:n_cells-off] = cells[off:];  ds[n_cells-off:] = cells[:off]
    combined = np.clip(cells + ds * 0.5, 0, 1)
    result = np.repeat(combined, dot_px)[:n]
    if len(result) < n:
        result = np.pad(result, (0, n-len(result)))
    return result

H, W = logo_scaled.shape
hell = np.zeros((H, W), dtype=np.float32)
drifts = np.random.normal(0, 1.2, W).astype(int)
for x in range(W):
    col   = np.roll(logo_scaled[:, x], drifts[x])
    hell[:, x] = hell_col(col, DOT, H // 2)

# Slight vertical Gaussian blur (dot spread on paper)
hell_pil = Image.fromarray((hell*255).astype(np.uint8))
hell_pil = hell_pil.filter(ImageFilter.GaussianBlur(radius=DOT*0.35))
hell = np.array(hell_pil, dtype=np.float32) / 255.0

# Subtle noise (simulates electrical noise in the link)
hell = np.clip(hell + np.random.normal(0, 0.025, hell.shape), 0, 1)

# 4 ── Place on A4 canvas ───────────────────────────────────────────────────
canvas = np.zeros((PAGE_H, PAGE_W), dtype=np.float32)
x_off  = (PAGE_W - W) // 2
dc0 = max(0, x_off);  dc1 = dc0 + min(W, PAGE_W - dc0)
sc0 = max(0, -x_off); sc1 = sc0 + (dc1 - dc0)
canvas[:, dc0:dc1] = hell[:, sc0:sc1]

# 5 ── Colorize ─────────────────────────────────────────────────────────────
# Reduce ink alpha to ~30 % so the image reads as a subtle background
INK_ALPHA = 0.28
alpha = canvas[:,:,np.newaxis] * INK_ALPHA

# Sepia palette
bg  = np.array([250, 247, 240], dtype=np.float32) / 255.0   # warm off-white
ink = np.array([ 35,  30,  25], dtype=np.float32) / 255.0   # near-black warm

rgb = bg * (1 - alpha) + ink * alpha
rgb = np.clip(rgb, 0, 1)

out = Image.fromarray((rgb*255).astype(np.uint8), mode="RGB")
out.save(OUT_PNG, dpi=(150, 150))
print(f"Saved {OUT_PNG}  {out.size}")

# Quick stats
arr = np.array(out)
print(f"Mean R={arr[:,:,0].mean():.1f}  dark_frac={(arr[:,:,0]<200).mean():.3f}")
