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
from PIL import Image
import subprocess, os, tempfile

_HERE     = os.path.dirname(os.path.abspath(__file__))
LOGO_PDF  = os.path.join(_HERE, "ssa-logotyp.pdf")
OUT_PNG   = os.path.join(_HERE, "hellschreiber-ssa.png")

PAGE_W, PAGE_H = 1240, 1754   # A4 at 150 DPI (210×297 mm → 1240×1754 px)
LOGO_HEIGHT_FRACTION = 0.70
LOGO_WIDTH_FRACTION = 0.65
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

# 2 ── Scale and center the logo with space around it ────────────────────────
lh, lw = logo_ink.shape
scale = min(PAGE_H * LOGO_HEIGHT_FRACTION / lh,
            PAGE_W * LOGO_WIDTH_FRACTION / lw)
tw, th = int(lw * scale), int(lh * scale)
logo_scaled = np.array(
    Image.fromarray((logo_ink*255).astype(np.uint8)).resize((tw, th), Image.LANCZOS),
    dtype=np.float32) / 255.0
print(f"Scaled: {logo_scaled.shape}")

# 3 ── Hellschreiber column scan ────────────────────────────────────────────
# Feld-Hell's vertically quantised dots and per-column timing retain the
# characteristic scan texture without printing a second, displaced logo.
DOT = 8   # pixels per Hell "dot" vertically

def hell_col(col, dot_px):
    n = len(col)
    n_cells = n // dot_px
    cells = np.zeros(n_cells)
    for i in range(n_cells):
        seg = col[i*dot_px:(i+1)*dot_px]
        cells[i] = 1.0 if seg.mean() > 0.30 else 0.0  # 30 % ink coverage → dot on
    result = np.repeat(cells, dot_px)[:n]
    if len(result) < n:
        result = np.pad(result, (0, n - len(result)))
    return result

H, W = logo_scaled.shape
hell = np.zeros((H, W), dtype=np.float32)
drifts = np.random.normal(0, 0.8, W).astype(int)  # subtle timing jitter per column
for x in range(W):
    col        = np.roll(logo_scaled[:, x], drifts[x])
    hell[:, x] = hell_col(col, DOT)

# Soften the quantised dots (receiver bandwidth / SDR screen pixels). The blur
# is applied *after* Hell quantisation so the 8 px dot cells stay recognisable
# but their hard stair-stepped edges become smooth, anti-aliased transitions.
def gaussian_blur_1d(img, sigma, axis):
    """Separable Gaussian blur along one axis, edge-replicated."""
    radius = int(np.ceil(sigma * 3))
    k = np.exp(-0.5 * (np.arange(-radius, radius + 1) / sigma) ** 2)
    k /= k.sum()
    pad = [(0, 0), (0, 0)]
    pad[axis] = (radius, radius)
    padded = np.pad(img, pad, mode="edge")
    out = np.zeros_like(img)
    for i, w in enumerate(k):
        out += w * (padded[i:i + img.shape[0], :] if axis == 0
                    else padded[:, i:i + img.shape[1]])
    return out

HELL_BLUR_Y = DOT * 0.38   # ~3.0 px: rounds the dot-cell steps
HELL_BLUR_X = DOT * 0.34   # ~2.7 px: softens left/right logo edges
hell = gaussian_blur_1d(hell, HELL_BLUR_Y, axis=0)
hell = gaussian_blur_1d(hell, HELL_BLUR_X, axis=1)

# 4 ── Build an SDR waterfall with visible noise and time history ─────────────
# A waterfall advances one horizontal scan at a time: random noise changes on
# every row, while slow level changes and fading channels leave horizontal
# history bands. Keep the floor dark enough for the white cover typography.
NOISE_FLOOR = 0.31
NOISE_SIGMA = 0.060
canvas = np.random.normal(
    NOISE_FLOOR, NOISE_SIGMA, (PAGE_H, PAGE_W)).astype(np.float32)

# Slow, irregular changes from scan to scan create gently banded time sweeps.
row_noise = np.random.normal(0, 1, PAGE_H)
row_kernel_x = np.arange(-24, 25, dtype=np.float32)
row_kernel = np.exp(-0.5 * (row_kernel_x / 9.0) ** 2)
row_kernel /= row_kernel.sum()
row_history = np.convolve(row_noise, row_kernel, mode="same").astype(np.float32)
canvas += row_history[:, np.newaxis] * 0.16

# Uneven fading and short stronger sweeps add recognizable received-signal
# history without drawing a frame, grid, or any display labels.
for y0 in np.random.randint(0, PAGE_H, 30):
    width = np.random.uniform(2.0, 13.0)
    strength = np.random.uniform(0.035, 0.11)
    rows = np.arange(PAGE_H, dtype=np.float32)
    canvas += (strength * np.exp(-0.5 * ((rows - y0) / width) ** 2))[:, None]

canvas = np.clip(canvas, 0, 1)

# A few narrow, fading carriers and drifting traces make the frequency
# structure legible against the noisy horizontal history.
yy = np.arange(PAGE_H, dtype=np.float32)
xx = np.arange(PAGE_W, dtype=np.float32)
for x0, drift, width, strength, phase in [
    (0.13,  0.012, 2.0, 0.29, 0.3),
    (0.27, -0.018, 3.0, 0.36, 1.1),
    (0.76,  0.022, 2.5, 0.32, 2.0),
    (0.88, -0.010, 2.0, 0.26, 2.7),
]:
    center = x0 * PAGE_W + drift * (yy - PAGE_H / 2)
    carrier = np.exp(-0.5 * ((xx[None, :] - center[:, None]) / width) ** 2)
    fading = 0.48 + 0.52 * np.maximum(
        0, np.sin(yy / 88.0 + phase))
    canvas += carrier * (strength * fading[:, None])

# Sparse shortwave-like traces: softly sloped, broken signals rather than
# regular bars. Their placement favors the margins and lower half of the cover.
for y_start, length, x_start, slope, width, strength in [
    (0.37, 0.22, 0.09,  0.10, 2.1, 0.24),
    (0.48, 0.20, 0.84, -0.08, 2.0, 0.22),
    (0.69, 0.19, 0.17, -0.06, 2.2, 0.30),
    (0.77, 0.16, 0.72,  0.08, 2.0, 0.27),
]:
    start = int(y_start * PAGE_H)
    end = min(PAGE_H, start + int(length * PAGE_H))
    ys = np.arange(start, end, dtype=np.float32)
    center = x_start * PAGE_W + slope * (ys - start)
    trace = np.exp(-0.5 * ((xx[None, :] - center[:, None]) / width) ** 2)
    # Dropouts and amplitude flutter are part of the received signal.
    flutter = np.clip(
        0.62 + 0.38 * np.sin(ys / 19.0 + x_start * 11), 0.0, 1.0)
    canvas[start:end] += trace * (strength * flutter[:, None])

canvas = np.clip(canvas, 0, 1)

x_off = (PAGE_W - W) // 2
y_off = (PAGE_H - H) // 2 + int(PAGE_H * 0.035)

# The logo is itself a received Hell scan, so it must suffer the same radio
# conditions as the waterfall behind it instead of sitting on top as a clean
# stencil. Everything below is derived from the same noise/sweep history.
bg = canvas[y_off:y_off + H, x_off:x_off + W]      # waterfall under the logo
bg_dev = bg - NOISE_FLOOR                           # shared noise + sweeps
rows_bg = bg_dev.mean(axis=1)                       # per-scan level history

# (a) Scan-to-scan timing variation: slowly wandering horizontal shift per
#     scan line (smoothed noise), applied to the logo coverage.
shift_noise = np.random.normal(0, 1, H)
shift_kernel_x = np.arange(-12, 13, dtype=np.float32)
shift_kernel = np.exp(-0.5 * (shift_kernel_x / 4.0) ** 2)
shift_kernel /= shift_kernel.sum()
shift = np.convolve(shift_noise, shift_kernel, mode="same")
shift = np.rint(shift / shift.std() * 0.9).astype(int)   # about +-1-2 px
cover = np.empty_like(hell)
for y in range(H):
    cover[y] = np.roll(hell[y], shift[y])

# (b) Receiver ringing: a short one-sided smear along the scan direction.
tail = np.exp(-np.arange(0, 5, dtype=np.float32) / 1.8)
tail /= tail.sum()
smeared = np.zeros_like(cover)
for i, w in enumerate(tail):
    smeared[:, i:] += w * cover[:, :W - i]
cover = 0.75 * cover + 0.25 * smeared

# (c) Signal strength follows the same level history as the waterfall rows
#     (fading and sweeps), plus occasional short partial dropouts.
gain = 0.86 + 0.10 * np.sin(np.arange(H, dtype=np.float32)[:, None] / 24.0)
gain = gain + rows_bg[:, None] * 0.8
dropout_rows = np.random.rand(H) < 0.02
dropout_rows = np.convolve(dropout_rows.astype(np.float32),
                           np.ones(3, dtype=np.float32), mode="same") > 0
dropout_depth = np.where(dropout_rows, np.random.uniform(0.60, 0.85, H), 1.0)
gain = gain * dropout_depth[:, None]

# (d) Per-pixel receiver noise: the waterfall's own noise is carried into the
#     logo, with extra multiplicative grain so the logo is not a flat colour.
grain = np.random.normal(0, 1, (H, W)).astype(np.float32)
grain = gaussian_blur_1d(grain, 0.8, axis=1) * 1.6
inside = (0.72 * gain * (1.0 + 0.16 * grain)
          + bg_dev * 0.6 + 0.03 * grain)

# Alpha-composite with the blurred, jittered coverage so edges pick up the
# surrounding noise as well.
cover = np.clip(cover, 0.0, 1.0)
canvas[y_off:y_off + H, x_off:x_off + W] = np.clip(
    bg * (1.0 - cover) + inside * cover, 0.0, 1.0)

# Keep the central title area quiet and dark for the white lettering; the
# noise remains visible, while strong carriers and sweeps are softened there.
title_y = np.arange(PAGE_H, dtype=np.float32)
title_x = np.arange(PAGE_W, dtype=np.float32)
y_fade = np.clip((title_y - PAGE_H * 0.05) / (PAGE_H * 0.08), 0, 1)
y_fade *= np.clip((PAGE_H * 0.66 - title_y) / (PAGE_H * 0.10), 0, 1)
x_fade = np.clip((title_x - PAGE_W * 0.08) / (PAGE_W * 0.12), 0, 1)
x_fade *= np.clip((PAGE_W * 0.92 - title_x) / (PAGE_W * 0.12), 0, 1)
title_guard = (y_fade[:, None] * x_fade[None, :]) * 0.66
canvas = canvas * (1.0 - title_guard) + NOISE_FLOOR * title_guard

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
    [  2,   5,  11],   # near-black
    [  6,  20,  44],   # deep blue
    [ 12,  57, 107],   # blue
    [ 24, 114, 125],   # muted cyan
    [ 61, 128,  95],   # muted green
    [170, 149,  77],   # softened yellow
    [188, 112,  64],   # softened orange
    [222, 216, 196],   # warm white
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

BRIGHTNESS = 0.58   # keep the signal dark enough for the white cover title
rgb = np.clip(rgb * BRIGHTNESS, 0, 1)

out = Image.fromarray((rgb * 255).astype(np.uint8), mode="RGB")

out.save(OUT_PNG, dpi=(150, 150))
print(f"Saved {OUT_PNG}  {out.size}")

arr = np.array(out)
print(f"Mean R={arr[:,:,0].mean():.1f}  bright_frac={(arr[:,:,0]>150).mean():.3f}")
