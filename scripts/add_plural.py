import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PLURALS = {
    'uz': {
        'msgid': '%(counter)s учебник к бронированию',
        'msgid_plural': '%(counter)s учебников к бронированию',
        'msgstrs': ['%(counter)s ta darslik bronlash uchun'],
    },
    'kaa': {
        'msgid': '%(counter)s учебник к бронированию',
        'msgid_plural': '%(counter)s учебников к бронированию',
        'msgstrs': ['%(counter)s sabaqlıq bronlaw ushın'],
    },
    'en': {
        'msgid': '%(counter)s учебник к бронированию',
        'msgid_plural': '%(counter)s учебников к бронированию',
        'msgstrs': ['%(counter)s textbook to reserve', '%(counter)s textbooks to reserve'],
    },
}

def esc(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')

for lang, p in PLURALS.items():
    path = os.path.join(BASE, 'locale', lang, 'LC_MESSAGES', 'django.po')
    content = open(path, encoding='utf-8').read()
    if f'msgid "{esc(p["msgid"])}"' in content:
        print(f'{lang}: already present')
        continue
    lines = [f'msgid "{esc(p["msgid"])}"', f'msgid_plural "{esc(p["msgid_plural"])}"']
    for i, s in enumerate(p['msgstrs']):
        lines.append(f'msgstr[{i}] "{esc(s)}"')
    block = '\n\n' + '\n'.join(lines) + '\n'
    content = content.rstrip('\n') + block
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(f'{lang}: added plural entry')
