"""
Generate Hellschreiber background image of SSA logo.

Feld-Hell (Hellschreiber) is a facsimile-based teleprinter system where
each character is transmitted column by column as a series of dots.
The rendering mimics a modern SDR waterfall display: dark noise floor
with bright signal dots coloured using the classic waterfall palette
(black → dark-blue → cyan → yellow → white).

Run from the repository root:
    python3 images/generate_hellschreiber.py

Requires: Pillow, numpy, pdftoppm (poppler-utils)
"""
import numpy as np
from PIL import Image, ImageFilter
import subprocess, os, tempfile

_HERE     = os.path.dirname(os.path.abspath(__file__))
LOGO_PDF  = os.path.join(_HERE, "ssa-logotyp.pdf")
OUT_PNG   = os.path.join(_HERE, "hellschreiber-ssa.png")

PAGE_W, PAGE_H = 1240, 1754   # A4 at 150 DPI (210×297 mm → 1240×1754 px)
np.random.seed(1928)           # Year Hellschreiber was invented

# 1 ── Load logo ────────────────────────────────────────────────────────────
_tmpdir  = tempfile.gettempdir()
ppm_base = os.path.join(_tmpdir, "ssa_hell_gen")
ppm      = ppm_base + "-1.ppm"
if not os.path.exists(ppm):
    subprocess.run(["pdftoppm", "-r", "200", LOGO_PDF, ppm_base], check=True)
logo_gray = np.array(Image.open(ppm).convert("L"), dtype=np.float32)
logo_ink  = (logo_gray < 200).astype(np.float32)  # threshold: <200/255 = ink

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

def hell_col(col, dot_px):
    n = len(col)
    n_cells = n // dot_px
    cells = np.zeros(n_cells)
    for i in range(n_cells):
        seg = col[i*dot_px:(i+1)*dot_px]
        cells[i] = 1.0 if seg.mean() > 0.30 else 0.0  # 30 % ink coverage → dot on
    # Double-strike: motor completes 2 revolutions per character row, so the
    # same column is printed again offset by half the total height.
    off = n_cells // 2
    ds = np.zeros(n_cells)
    ds[:n_cells-off] = cells[off:];  ds[n_cells-off:] = cells[:off]
    combined = np.clip(cells + ds * 0.5, 0, 1)
    result = np.repeat(combined, dot_px)[:n]
    if len(result) < n:
        result = np.pad(result, (0, n - len(result)))
    return result

H, W = logo_scaled.shape
hell = np.zeros((H, W), dtype=np.float32)
drifts = np.random.normal(0, 1.2, W).astype(int)  # ±1–2 px timing jitter per column
for x in range(W):
    col        = np.roll(logo_scaled[:, x], drifts[x])
    hell[:, x] = hell_col(col, DOT)

# Slight vertical Gaussian blur (dot spread on the SDR screen pixels)
hell_pil = Image.fromarray((hell*255).astype(np.uint8))
hell_pil = hell_pil.filter(ImageFilter.GaussianBlur(radius=DOT * 0.35))  # ~35 % of dot size
hell = np.array(hell_pil, dtype=np.float32) / 255.0

# 4 ── Place on A4 canvas with noise floor ──────────────────────────────────
# Noise floor: dark Gaussian speckle, as seen on a real SDR waterfall.
NOISE_FLOOR  = 0.10   # baseline level for the noise floor (0 = black)
NOISE_SIGMA  = 0.055  # spread of the Gaussian noise on top
canvas = np.random.normal(NOISE_FLOOR, NOISE_SIGMA, (PAGE_H, PAGE_W)).astype(np.float32)
canvas = np.clip(canvas, 0, 1)

x_off = (PAGE_W - W) // 2
dc0 = max(0, x_off);  dc1 = dc0 + min(W, PAGE_W - dc0)
sc0 = max(0, -x_off); sc1 = sc0 + (dc1 - dc0)

PEAK_SIGNAL  = 0.90   # scale signal to 90 % of max, leaving headroom for white-hot
canvas[:, dc0:dc1] = np.maximum(canvas[:, dc0:dc1], hell[:, sc0:sc1] * PEAK_SIGNAL)

# 5 ── SDR waterfall colormap ────────────────────────────────────────────────
# Classic waterfall palette used by SDR# / GQRX / WebSDR, defined by
# key-stops at normalised power values 0 … 1:
#   0.00 → black          (noise floor)
#   0.20 → dark blue
#   0.40 → blue
#   0.55 → cyan
#   0.70 → green
#   0.82 → yellow
#   0.92 → orange
#   1.00 → white          (strongest signal / saturation)

_STOPS = np.array([0.00, 0.20, 0.40, 0.55, 0.70, 0.82, 0.92, 1.00])
_COLORS = np.array([
    [  0,   0,   0],   # black
    [  0,   0, 140],   # dark blue
    [  0,  60, 220],   # blue
    [  0, 220, 220],   # cyan
    [  0, 200,  50],   # green
    [230, 230,   0],   # yellow
    [255, 130,   0],   # orange
    [255, 255, 255],   # white
], dtype=np.float32) / 255.0

def waterfall_colormap(v):
    """Map scalar array v (0…1) to RGB using the SDR waterfall palette."""
    v = np.clip(v, 0, 1)
    out = np.zeros((*v.shape, 3), dtype=np.float32)
    for i in range(len(_STOPS) - 1):
        lo, hi = _STOPS[i], _STOPS[i + 1]
        mask = (v >= lo) & (v < hi)
        t = np.where(mask, (v - lo) / (hi - lo), 0.0)[:, :, np.newaxis]
        c0 = _COLORS[i];  c1 = _COLORS[i + 1]
        out += mask[:, :, np.newaxis] * (c0 * (1 - t) + c1 * t)
    # Handle v == 1.0 exactly
    out[v >= 1.0] = _COLORS[-1]
    return out

rgb = waterfall_colormap(canvas)

BRIGHTNESS = 0.82   # reduce to 82 % so the image doesn't overpower the cover text
rgb = np.clip(rgb * BRIGHTNESS, 0, 1)

out = Image.fromarray((rgb * 255).astype(np.uint8), mode="RGB")
out.save(OUT_PNG, dpi=(150, 150))
print(f"Saved {OUT_PNG}  {out.size}")

arr = np.array(out)
print(f"Mean R={arr[:,:,0].mean():.1f}  bright_frac={(arr[:,:,0]>150).mean():.3f}")
