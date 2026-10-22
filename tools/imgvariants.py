#!/usr/bin/env python3
"""Make WebP size variants next to each image used on the site: foo.jpg -> foo.w480.webp, foo.w800.webp, foo.w1600.webp.
Run after adding covers or photos (tools/covers.py calls it). Existing variants newer than the source are kept."""
import os, sys
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ['media/covers', 'media/library', 'media/t', 'media/uploads']
WIDTHS = (480, 800, 1600)

def variants(path):
    base, ext = os.path.splitext(path)
    if ext.lower() not in ('.jpg', '.jpeg', '.png') or '.w' in os.path.basename(base)[-6:]: return 0
    n = 0; im = None
    for w in WIDTHS:
        out = f'{base}.w{w}.webp'
        if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(path): continue
        if im is None:
            im = Image.open(path).convert('RGB')
        if w > im.width and w != WIDTHS[0]: continue
        v = im.copy(); v.thumbnail((w, w * 2))
        v.save(out, 'WEBP', quality=78, method=6); n += 1
    return n

if __name__ == '__main__':
    total = 0
    for d in (sys.argv[1:] or DIRS):
        p = os.path.join(ROOT, d)
        if os.path.isfile(p): total += variants(p); continue
        for r, _, fs in os.walk(p):
            for f in fs: total += variants(os.path.join(r, f))
    print('webp variants written:', total)
