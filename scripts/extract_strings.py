"""Extract all translatable strings from templates and Python sources."""
import os
import re
import json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRANS_RE = re.compile(r'\{%\s*trans\s+(["\'])(.*?)\1\s*%\}')
BLOCKTRANS_RE = re.compile(r'\{%\s*blocktranslate(?:\s+[^%]*?)?\s*%\}(.*?)\{%\s*endblocktranslate\s*%\}', re.S)
PLURAL_SPLIT_RE = re.compile(r'\{%\s*plural\s*%\}')
PY_STR_RE = re.compile(r"\bgettext\s*\(\s*(['\"])(.*?)\1\s*\)|\b_\s*\(\s*(['\"])(.*?)\2\s*\)")


def normalize_block(text):
    text = text.strip()
    text = re.sub(r'\{%\s*today\s+["\'][^"\']*["\']\s*%\}', '%(date)s', text)
    text = re.sub(r'\{%\s*trans\s+["\'][^"\']*["\']\s*%\}', '%(translation)s', text)
    text = re.sub(r'\{\{\s*([^}]+?)\s*\}\}', lambda m: '%({0})s'.format(m.group(1).strip()), text)
    text = re.sub(r'\{%\s*blocktranslate.*?%\}.*?\{%\s*endblocktranslate\s*%\}', '%(translation)s', text, flags=re.S)
    return text.strip()


def add_block(strings, block):
    parts = PLURAL_SPLIT_RE.split(block)
    if len(parts) == 2:
        singular = normalize_block(parts[0])
        plural = normalize_block(parts[1])
        if singular:
            strings.add(singular)
        if plural:
            strings.add(plural)
    else:
        norm = normalize_block(block)
        if norm:
            strings.add(norm)


def collect():
    strings = set()

    for root, _, files in os.walk(os.path.join(BASE, 'dashboard', 'templates')):
        for fn in files:
            if not fn.endswith('.html'):
                continue
            with open(os.path.join(root, fn), encoding='utf-8') as f:
                content = f.read()
            for m in TRANS_RE.finditer(content):
                strings.add(m.group(2))
            for m in BLOCKTRANS_RE.finditer(content):
                add_block(strings, m.group(1))

    for sub in ['templates', 'apps']:
        for root, _, files in os.walk(os.path.join(BASE, sub)):
            for fn in files:
                if fn.endswith('.html') or fn.endswith('.py'):
                    with open(os.path.join(root, fn), encoding='utf-8') as f:
                        content = f.read()
                    for m in TRANS_RE.finditer(content):
                        strings.add(m.group(2))
                    for m in BLOCKTRANS_RE.finditer(content):
                        add_block(strings, m.group(1))
                    if fn.endswith('.py'):
                        for m in PY_STR_RE.finditer(content):
                            s = m.group(2) if m.group(2) is not None else m.group(4)
                            strings.add(s)

    return strings


if __name__ == '__main__':
    all_strings = collect()
    with open(os.path.join(BASE, 'scripts', 'strings.json'), 'w', encoding='utf-8') as f:
        json.dump(sorted(all_strings), f, ensure_ascii=False, indent=2)
    print(f'Extracted {len(all_strings)} unique strings')
