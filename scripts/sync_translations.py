import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALE_DIR = os.path.join(BASE_DIR, 'locale')

# Dictionary of translations for new / missing phrases
TRANSLATIONS = {
    "Назначение учебников классам": {
        "uz": "Darsliklarni sinflarga biriktirish",
        "kaa": "Sınıflarǵa sabaqlıqlardı biriktiriw",
        "en": "Assigning textbooks to classes"
    },
    "Назначение учебников по предметам": {
        "uz": "Darsliklarni fanlar bo'yicha biriktirish",
        "kaa": "Pánler boyınsha sabaqlıqlardı biriktiriw",
        "en": "Assigning textbooks by subject"
    },
    "Математика": {
        "uz": "Matematika",
        "kaa": "Matematika",
        "en": "Mathematics"
    },
    "Назначить": {
        "uz": "Biriktirish",
        "kaa": "Biriktiriw",
        "en": "Assign"
    },
    "Нет назначений": {
        "uz": "Biriktirilganlar yo'q",
        "kaa": "Biriktirilgenler joq",
        "en": "No assignments"
    },
    "Поиск по названию, предмету или автору...": {
        "uz": "Nomi, fani yoki muallifi bo'yicha qidiruv...",
        "kaa": "Ataması, páni yamasa avtorı boyınsha izlew...",
        "en": "Search by title, subject or author..."
    },
    "Поиск": {
        "uz": "Qidirish",
        "kaa": "Izlew",
        "en": "Search"
    },
    "выберите": {
        "uz": "tanlang",
        "kaa": "saylań",
        "en": "select"
    },
    "Всего": {
        "uz": "Jami",
        "kaa": "Barlıǵı",
        "en": "Total"
    },
    "Доступно": {
        "uz": "Mavjud",
        "kaa": "Qoljetimli",
        "en": "Available"
    },
    "Нет остатков. Добавьте учебник через форму выше.": {
        "uz": "Qoldiqlar yo'q. Yuqoridagi forma orqali darslik qo'shing.",
        "kaa": "Qaldıqlar joq. Joqarıdaǵı forma arqalı sabaqlıq qosıń.",
        "en": "No stock. Add a textbook via the form above."
    },
    "Остатки учебников": {
        "uz": "Darsliklar qoldig'i",
        "kaa": "Sabaqlıqlar qaldıǵı",
        "en": "Textbook stock"
    },
    "Учебники — Библиотечная система": {
        "uz": "Darsliklar — Kutubxona tizimi",
        "kaa": "Sabaqlıqlar — Kitapxana sisteması",
        "en": "Textbooks — Library System"
    }
}

def extract_trans_strings():
    pattern = re.compile(r'\{%\s*trans\s+["\']([^"\']+)["\']\s*%\}')
    extracted = set()
    
    search_dirs = [os.path.join(BASE_DIR, 'dashboard', 'templates'), os.path.join(BASE_DIR, 'apps')]
    for d in search_dirs:
        for root, dirs, files in os.walk(d):
            for f in files:
                if f.endswith('.html'):
                    path = os.path.join(root, f)
                    with open(path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        matches = pattern.findall(content)
                        for m in matches:
                            extracted.add(m)
    return extracted

def update_po_file(lang, missing_strings):
    po_path = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
    if not os.path.exists(po_path):
        return
    
    with open(po_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_entries = []
    for msgid in missing_strings:
        if f'msgid "{msgid}"' not in content:
            tr = TRANSLATIONS.get(msgid, {}).get(lang, msgid)
            entry = f'\nmsgid "{msgid}"\nmsgstr "{tr}"\n'
            new_entries.append(entry)
    
    if new_entries:
        with open(po_path, 'a', encoding='utf-8') as f:
            for ne in new_entries:
                f.write(ne)
        print(f"[{lang}] Added {len(new_entries)} missing translations to {po_path}")
    else:
        print(f"[{lang}] All strings are up to date in PO file.")

def main():
    extracted = extract_trans_strings()
    print(f"Extracted {len(extracted)} translatable strings from HTML templates.")
    
    for lang in ['uz', 'kaa', 'en']:
        update_po_file(lang, extracted)

if __name__ == '__main__':
    main()
