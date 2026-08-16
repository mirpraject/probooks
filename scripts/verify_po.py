"""Verify .po coverage."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compile_messages import _parse_po

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE, 'scripts', 'strings.json'), encoding='utf-8') as f:
    expected = set(json.load(f))

ok = True
for lang in ['uz', 'kaa', 'en']:
    po_path = os.path.join(BASE, 'locale', lang, 'LC_MESSAGES', 'django.po')
    entries = _parse_po(po_path)
    msgids = {e['msgid'] for e in entries}
    msgids |= {e['msgid_plural'] for e in entries if e['msgid_plural']}
    missing = {m for m in expected - msgids if m}
    empty = [e['msgid'] for e in entries if e['msgid'] and not e['msgstrs']]
    print(f'[{lang}] entries={len(entries)} missing={len(missing)} empty_msgstr={len(empty)}')
    if missing:
        for m in sorted(missing):
            print('   MISSING:', m)
    if empty:
        for m in empty[:10]:
            print('   EMPTY  :', m)
    if missing or empty:
        ok = False

if ok:
    print('ALL STRINGS COVERED')
