"""Compile .po files to .mo without gettext tools."""
import os
import struct

LOCALE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'locale')


def _unesc(s):
    return s.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')


def _parse_po(po_path):
    """Parse .po file into a list of entry dicts.

    Entry shape: {'msgid': str, 'msgid_plural': str|None, 'msgstrs': [str, ...]}
    """
    with open(po_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = []
    current_id = []
    current_plural_parts = []
    has_plural = False
    current_strs = []
    in_id = False
    in_id_plural = False
    in_str = False

    def flush():
        if current_id or current_strs or has_plural:
            entries.append({
                'msgid': _unesc(''.join(current_id)),
                'msgid_plural': _unesc(''.join(current_plural_parts)) if has_plural else None,
                'msgstrs': [_unesc(v) for v in current_strs],
            })

    for line in content.split('\n'):
        if line.startswith('msgid "'):
            flush()
            current_id = []
            current_plural_parts = []
            has_plural = False
            current_strs = []
            current_id.append(line[7:-1])
            in_id = True
            in_id_plural = False
            in_str = False
        elif line.startswith('msgid_plural "'):
            in_id = False
            in_id_plural = True
            in_str = False
            has_plural = True
            current_plural_parts.append(line[14:-1])
        elif line.startswith('msgstr['):
            in_id = False
            in_id_plural = False
            in_str = True
            idx = line.index(']')
            val = line[idx + 2:-1]
            current_strs.append(val)
        elif line.startswith('msgstr "'):
            in_id = False
            in_id_plural = False
            in_str = True
            current_strs.append(line[8:-1])
        elif in_id and line.startswith('"'):
            current_id.append(line[1:-1])
        elif in_id_plural and line.startswith('"'):
            current_plural_parts.append(line[1:-1])
        elif in_str and line.startswith('"'):
            current_strs[-1] = current_strs[-1] + line[1:-1]
        elif not line.startswith('"') and not line.startswith('#'):
            in_id = False
            in_id_plural = False
            in_str = False

    flush()
    return entries


def _id_bytes(entry):
    if entry['msgid_plural'] is not None:
        return (entry['msgid'] + '\x00' + entry['msgid_plural']).encode('utf-8')
    return entry['msgid'].encode('utf-8')


def _str_bytes(entry):
    if entry['msgid_plural'] is not None:
        return '\x00'.join(entry['msgstrs']).encode('utf-8')
    return (entry['msgstrs'][0] if entry['msgstrs'] else '').encode('utf-8')


def po_to_mo(po_path, mo_path):
    entries = _parse_po(po_path)
    if not entries:
        print(f'No entries found in {po_path}')
        return

    # Ensure empty msgid is first (catalog metadata)
    empty_entry = None
    non_empty = []
    for entry in entries:
        if entry['msgid'] == '':
            empty_entry = entry
        else:
            non_empty.append(entry)
    ordered = ([empty_entry] if empty_entry else []) + non_empty

    id_bytes = [_id_bytes(e) for e in ordered]
    str_bytes = [_str_bytes(e) for e in ordered]
    id_lengths = [len(b) for b in id_bytes]
    str_lengths = [len(b) for b in str_bytes]
    count = len(ordered)

    # .mo format (little-endian):
    # Header: magic(4) + version(4) + count(4) + orig_offset(4) + trans_offset(4) = 20 bytes
    HEADER_SIZE = 20
    orig_table_offset = HEADER_SIZE
    trans_table_offset = orig_table_offset + count * 8
    str_data_offset = trans_table_offset + count * 8

    le = '<'
    with open(mo_path, 'wb') as f:
        # Magic number (little-endian)
        f.write(struct.pack(le + 'I', 0x950412de))
        # Version, count, orig_offset, trans_offset
        f.write(struct.pack(le + '4I', 0, count, orig_table_offset, trans_table_offset))

        # Original strings table: each entry = (length, offset)
        offset = str_data_offset
        for length in id_lengths:
            f.write(struct.pack(le + 'II', length, offset))
            offset += length

        # Translated strings table
        offset = str_data_offset + sum(id_lengths)
        for length in str_lengths:
            f.write(struct.pack(le + 'II', length, offset))
            offset += length

        # Raw string data
        for b in id_bytes:
            f.write(b)
        for b in str_bytes:
            f.write(b)
        # Trailing null byte to ensure tend < buflen for last entry
        f.write(b'\x00')

    print(f'Compiled {count} messages: {po_path} -> {mo_path}')


def main():
    for lang in ['uz', 'kaa', 'en']:
        po = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
        mo = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'django.mo')
        if os.path.exists(po):
            po_to_mo(po, mo)


if __name__ == '__main__':
    main()
