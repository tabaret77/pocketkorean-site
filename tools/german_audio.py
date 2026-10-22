"""Pocket German web trial: cut a smaller audio set (A1 words, topic words, sentences of the day)
out of the app's full audio sprites, so the site does not carry all 250 MB.

Source: /home/claude/pgsrc/audio (l000.mp3 … + idx2.json, from the app)
Output: german/app/audio/ (same format: idx2.json {p: [files], m: {id: [file, wStart, wDur, exStart, exDur]}, x: {...}})
"""
import json, os, subprocess, sys

SRC = '/home/claude/pgsrc'
OUT = '/home/claude/pocketkorean-site/german/web/audio'
SR = 22050
GAP = int(0.12 * SR)          # silence between clips
PER_FILE = 15 * 60 * SR       # about 15 minutes per sprite, like the app


def free_ids():
    ids = {w['id'] for w in json.load(open(f'{SRC}/data/A1.json'))}
    for t in json.load(open(f'{SRC}/data/topics.json'))['topics']:
        ids.update(t['ids'])
    return ids


def main():
    """The app's index stores BYTE offsets into the MP3 files (CBR 24 kbit/s); the app cuts those byte ranges and decodes
    each one on its own. So we copy the same byte ranges, untouched, into new files and record the new offsets."""
    idx = json.load(open(f'{SRC}/audio/idx2.json'))
    want = free_ids() | {k for k in idx['m'] if k.startswith('N')}
    want = [k for k in idx['m'] if k in want]
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT): os.remove(f'{OUT}/{f}')
    srcb = {}
    files, m, buf = [], {}, bytearray()
    def flush():
        nonlocal buf
        if buf:
            name = f't{len(files):03d}.mp3'; open(f'{OUT}/{name}', 'wb').write(bytes(buf)); files.append(name); buf = bytearray()
    for k in want:
        e = idx['m'][k]
        if e[0] not in srcb: srcb[e[0]] = open(f'{SRC}/audio/{idx["p"][e[0]]}', 'rb').read()
        data = srcb[e[0]]
        rec = [len(files)]
        for s0, n in ((e[1], e[2]), (e[3], e[4])) if len(e) >= 5 else ((e[1], e[2]),):
            if s0 is None or s0 < 0 or n <= 0:
                rec += [-1, 0]; continue
            rec += [len(buf), n]; buf += data[s0:s0 + n]
        m[k] = rec
        if len(buf) >= 2_800_000: flush()
    flush()
    json.dump({'p': files, 'm': m, 'x': idx.get('x', {})}, open(f'{OUT}/idx2.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    print(len(files), 'files,', len(m), 'clips')


if __name__ == '__main__':
    main()
