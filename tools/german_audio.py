"""Pocket German web trial: cut a smaller audio set (A1 words, topic words, sentences of the day)
out of the app's full audio sprites, so the site does not carry all 250 MB.

Source: /home/claude/pgsrc/audio (l000.mp3 … + idx2.json, from the app)
Output: german/app/audio/ (same format: idx2.json {p: [files], m: {id: [file, wStart, wDur, exStart, exDur]}, x: {...}})
"""
import json, os, subprocess, sys
import numpy as np

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


def decode(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-f', 's16le', '-ac', '1', '-ar', str(SR), '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16)


def main():
    idx = json.load(open(f'{SRC}/audio/idx2.json'))
    want = free_ids() | {k for k in idx['m'] if k.startswith('N')}
    want = [k for k in idx['m'] if k in want]
    by_file = {}
    for k in want:
        by_file.setdefault(idx['m'][k][0], []).append(k)
    os.makedirs(OUT, exist_ok=True)
    files, m = [], {}
    buf, pos = [], 0

    def flush():
        nonlocal buf, pos
        if not buf:
            return
        name = f't{len(files):03d}.mp3'
        pcm = np.concatenate(buf)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 's16le', '-ar', str(SR), '-ac', '1', '-i', '-',
                        '-codec:a', 'libmp3lame', '-b:a', '24k', f'{OUT}/{name}'], input=pcm.tobytes(), check=True)
        files.append(name)
        buf, pos = [], 0

    ms = lambda n: int(round(n * 1000 / SR))
    for fi in sorted(by_file):
        pcm = decode(f'{SRC}/audio/{idx["p"][fi]}')
        for k in by_file[fi]:
            e = idx['m'][k]
            rec = [len(files)]
            for s, d in ((e[1], e[2]), (e[3], e[4])) if len(e) >= 5 else ((e[1], e[2]),):
                a = int(s * SR / 1000); b = a + int(d * SR / 1000)
                clip = pcm[a:b]
                rec += [ms(pos), ms(len(clip))]
                buf.append(clip); buf.append(np.zeros(GAP, np.int16)); pos += len(clip) + GAP
            m[k] = rec
            if pos >= PER_FILE:
                flush()
        print(f'{idx["p"][fi]} → {len(m)} clips', file=sys.stderr)
    flush()
    json.dump({'p': files, 'm': m, 'x': idx.get('x', {})}, open(f'{OUT}/idx2.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    print(len(files), 'files,', len(m), 'clips')


if __name__ == '__main__':
    main()
