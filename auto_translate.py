import json
import time
import io
import sys
from deep_translator import MyMemoryTranslator

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def translate_all():
    with open('missing.json', 'r', encoding='utf-8') as f:
        missing = json.load(f)
    
    # Load previously translated to resume
    try:
        with open('translations_new.json', 'r', encoding='utf-8') as f:
            new_dict = json.load(f)
    except:
        new_dict = {}
        
    translator_uz = MyMemoryTranslator(source='ru-RU', target='uz-UZ')
    translator_en = MyMemoryTranslator(source='ru-RU', target='en-GB')
    
    for i, text in enumerate(missing):
        if text in new_dict:
            continue
        print(f"Translating {i}/{len(missing)}...")
        try:
            uz = translator_uz.translate(text)
            en = translator_en.translate(text)
        except Exception as e:
            uz = text
            en = text
            
        new_dict[text] = {
            "uz": uz,
            "kaa": uz,
            "en": en
        }
        time.sleep(0.3)
        
        # Save every 10 iterations
        if i % 10 == 0:
            with open('translations_new.json', 'w', encoding='utf-8') as f:
                json.dump(new_dict, f, ensure_ascii=False, indent=4)
                
    # Final save
    with open('translations_new.json', 'w', encoding='utf-8') as f:
        json.dump(new_dict, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    translate_all()
