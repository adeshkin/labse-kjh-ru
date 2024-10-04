def main():
    paths = [
        'data/kjh_ru_texts/kjh_text_1.txt',
        'data/kjh_ru_texts/kjh_text_2.txt',
        'data/kjh_ru_texts/kjh_text_3.txt',
        'data/kjh_ru_texts/kjh_text_7.txt',
        'data/kjh_ru_texts/kjh_text_8.txt',
        'data/kjh_ru_texts/kjh_text_13.txt',
    ]
    old2news = [
        {'e': 'ӱ', 'E': 'Ӱ', 'J': 'Ӧ', 'I': 'І', 'a': 'а', 'c': 'с', 'i': 'і', 'j': 'ӧ', 'o': 'ӧ', 'u': 'ғ', 'x': 'ҷ',
         'y': 'ң', '\ufeff': ' ', 'w': 'ӱ'},
        {'E': 'Ӱ', 'I': 'І', 'J': 'Ӧ', 'e': 'ӱ', 'i': 'і', 'j': 'ӧ', 'u': 'ғ', 'x': 'ҷ', 'y': 'ң', '\ufeff': ' '},
        {'I': 'І', 'i': 'і', '\\': ' ', 'ö': 'ӧ', 'y': 'ң'},
        {'C': 'С', 'I': 'І', 'a': 'а', 'c': 'с', 'e': 'е', 'p': 'р', 'i': 'і', 'u': 'и', 'y': 'у'},
        {'I': 'І', 'i': 'і'},
        {'\ufeff': ' '},
    ]

    for path, old2new in zip(paths, old2news):
        with open(path, "r", encoding="utf8") as f:
            text = f.read()

        for old_ch, new_ch in old2new.items():
            text = text.replace(old_ch, new_ch)
        text = text.replace('…', ' ... ').replace('Ӏ', 'І')
        with open(path.replace('.txt', '_clean.txt'), "w", encoding="utf8") as f:
            f.write(text)


def main1():
    paths = [
        'data/kjh_ru_texts/ru_text_1.txt',
        'data/kjh_ru_texts/ru_text_2.txt',
        'data/kjh_ru_texts/ru_text_3.txt',
        'data/kjh_ru_texts/ru_text_7.txt',
        'data/kjh_ru_texts/ru_text_8.txt',
        'data/kjh_ru_texts/ru_text_13.txt',
    ]

    old2new = {
        'B': 'В',
        'a': 'а',
        'c': 'с',
        'e': 'е',
        'o': 'о',
        'p': 'р',
        'y': 'у',
        '\ufeff': ' ',
        '…': ' ... '
    }

    for path in paths:
        with open(path, "r", encoding="utf8") as f:
            text = f.read()

        for old_ch, new_ch in old2new.items():
            text = text.replace(old_ch, new_ch)

        with open(path.replace('.txt', '_clean.txt'), "w", encoding="utf8") as f:
            f.write(text)


if __name__ == '__main__':
    main()
    main1()
