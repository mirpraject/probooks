import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADD = {
    'uz': {
        '2025-2026': '2025-2026',
        'Excel': 'Excel',
        'ID ученика': "O'quvchi IDsi",
        'А': 'A',
        'Должники': 'Qarzdorlar',
        'Логин ученика': "O'quvchi logini",
        'Название района': 'Tuman nomi',
        'Название школы': 'Maktab nomi',
        'Новый пароль (мин. 6)': 'Yangi parol (kamida 6)',
        'Подтвердите пароль': 'Parolni tasdiqlang',
        'Поиск книг и учебников...': "Kitoblar va darsliklarni qidirish...",
        'Поиск по имени или логину...': "Ism yoki login bo'yicha qidirish...",
        'Поиск по названию или автору...': "Nomi yoki muallifi bo'yicha qidirish...",
        'Текущий пароль': 'Joriy parol',
        'Убрать': 'Olib tashlash',
        'Удалить': "O'chirish",
        'логин': 'login',
        'Учебники и книги': 'Darsliklar va kitoblar',
        'Геймификация': "O'yinlashtirish",
        'Статистика': 'Statistika',
        'Показать пароль': "Parolni ko'rsatish",
        'Копировать пароль': 'Parolni nusxalash',
        'Изменение логина': "Loginni o'zgartirish",
        'Новый логин': 'Yangi login',
        'Изменить логин': "Loginni o'zgartirish",
        'Пароль': 'Parol',
        'Логин не может быть пустым': "Login bo'sh bo'lishi mumkin emas",
        'Логин может содержать только латинские буквы, цифры и символы _-.': "Login faqat lotin harflari, raqamlar va _-. belgilaridan iborat bo'lishi mumkin",
        'Пользователь с таким логином уже существует': 'Bunday loginli foydalanuvchi allaqachon mavjud',
        'Логин изменён': "Login o'zgartirildi",
        'Неверный текущий пароль': "Joriy parol noto'g'ri",
        'Новый пароль слишком короткий (минимум 6 символов)': 'Yangi parol juda qisqa (kamida 6 ta belgi)',
        'Пароли не совпадают': 'Parollar mos kelmaydi',
        'Пароль успешно изменён': "Parol muvaffaqiyatli o'zgartirildi",
    },
    'kaa': {
        '2025-2026': '2025-2026',
        'Excel': 'Excel',
        'ID ученика': 'Oqıwshı IDsi',
        'А': 'A',
        'Должники': 'Qarızlar',
        'Логин ученика': 'Oqıwshı logini',
        'Название района': 'Rayon atı',
        'Название школы': 'Mektep atı',
        'Новый пароль (мин. 6)': 'Jańa parol (keminde 6)',
        'Подтвердите пароль': 'Paroldı tastıyıqlań',
        'Поиск книг и учебников...': 'Kitap hám sabaqlıqlardı izlew...',
        'Поиск по имени или логину...': 'Atı yamasa loginı boyınsha izlew...',
        'Поиск по названию или автору...': 'Atı yamasa avtorı boyınsha izlew...',
        'Текущий пароль': 'Házirgi parol',
        'Убрать': 'Alıp taslaw',
        'Удалить': 'Óshiriw',
        'логин': 'login',
        'Учебники и книги': 'Sabaqlıqlar hám kitaplar',
        'Геймификация': 'Oyınlastırıw',
        'Статистика': 'Statistika',
        'Показать пароль': 'Paroldı kórsetiw',
        'Копировать пароль': 'Paroldı kóshiriw',
        'Изменение логина': 'Logindı ózgertiriw',
        'Новый логин': 'Jańa login',
        'Изменить логин': 'Logindı ózgertiriw',
        'Пароль': 'Parol',
        'Логин не может быть пустым': 'Login bosh bolıwı múmkin emes',
        'Логин может содержать только латинские буквы, цифры и символы _-.': 'Login tek latın háripleri, sanlar hám _-. belgilerinen ibarat bolıwı múmkin',
        'Пользователь с таким логином уже существует': 'Bunday loginli paydalanıwshı áne házir bar',
        'Логин изменён': 'Login ózgertirildi',
        'Неверный текущий пароль': 'Házirgi parol qáte',
        'Новый пароль слишком короткий (минимум 6 символов)': 'Jańa parol júdá qısqa (keminde 6 belgi)',
        'Пароли не совпадают': 'Parollar sáykes kelmeydi',
        'Пароль успешно изменён': 'Parol tabıslı ózgertirildi',
    },
    'en': {
        '2025-2026': '2025-2026',
        'Excel': 'Excel',
        'ID ученика': 'Student ID',
        'А': 'A',
        'Должники': 'Debtors',
        'Логин ученика': 'Student login',
        'Название района': 'District name',
        'Название школы': 'School name',
        'Новый пароль (мин. 6)': 'New password (min 6)',
        'Подтвердите пароль': 'Confirm password',
        'Поиск книг и учебников...': 'Search books and textbooks...',
        'Поиск по имени или логину...': 'Search by name or login...',
        'Поиск по названию или автору...': 'Search by title or author...',
        'Текущий пароль': 'Current password',
        'Убрать': 'Remove',
        'Удалить': 'Remove',
        'логин': 'login',
        'Учебники и книги': 'Textbooks and books',
        'Геймификация': 'Gamification',
        'Статистика': 'Statistics',
        'Показать пароль': 'Show password',
        'Копировать пароль': 'Copy password',
        'Изменение логина': 'Change login',
        'Новый логин': 'New login',
        'Изменить логин': 'Change login',
        'Пароль': 'Password',
        'Логин не может быть пустым': 'Login cannot be empty',
        'Логин может содержать только латинские буквы, цифры и символы _-.': 'Login may contain only Latin letters, digits and _-. symbols',
        'Пользователь с таким логином уже существует': 'A user with this login already exists',
        'Логин изменён': 'Login changed',
        'Неверный текущий пароль': 'Current password is incorrect',
        'Новый пароль слишком короткий (минимум 6 символов)': 'New password is too short (minimum 6 characters)',
        'Пароли не совпадают': 'Passwords do not match',
        'Пароль успешно изменён': 'Password changed successfully',
    },
}

def escape_po(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

for lang, mapping in ADD.items():
    path = os.path.join(BASE, 'locale', lang, 'LC_MESSAGES', 'django.po')
    with open(path, encoding='utf-8') as f:
        content = f.read()
    missing = [k for k in mapping if f'msgid "{escape_po(k)}"' not in content]
    if not missing:
        print(f'{lang}: nothing to add')
        continue
    blocks = []
    for k in missing:
        block = f'msgid "{escape_po(k)}"\nmsgstr "{escape_po(mapping[k])}"'
        blocks.append(block)
    insertion = '\n\n' + '\n\n'.join(blocks) + '\n'
    if content.endswith('\n\n'):
        content = content + insertion.lstrip('\n')
    else:
        content = content.rstrip('\n') + '\n\n' + insertion.lstrip('\n')
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(f'{lang}: added {len(missing)} entries')
