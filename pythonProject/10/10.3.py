with open('../en-ru.txt', 'r') as f:
    en_ru_dict = {}
    for line in f:
        parts = line.strip().split(' - ')
        if len(parts) == 2:
            en_ru_dict[parts[0]] = parts[1]

ru_en_dict = {}

for en_word, ru_translations in en_ru_dict.items():
    ru_words = ru_translations.split(', ')
    for ru_word in ru_words:
        if ru_word in ru_en_dict:
            ru_en_dict[ru_word].append(en_word)
        else:
            ru_en_dict[ru_word] = [en_word]

with open('../ru-en.txt', 'w') as f:
    for ru_word, en_words in sorted(ru_en_dict.items()):
        f.write('{} - {}\n'.format(ru_word, ', '.join(sorted(en_words))))