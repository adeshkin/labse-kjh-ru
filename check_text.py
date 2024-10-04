def main():
    paths = [
        'data/kjh_ru_texts/kjh_text_1_clean.txt',
        'data/kjh_ru_texts/kjh_text_2_clean.txt',
        'data/kjh_ru_texts/kjh_text_3_clean.txt',
        'data/kjh_ru_texts/kjh_text_7_clean.txt',
        'data/kjh_ru_texts/kjh_text_8_clean.txt',
        'data/kjh_ru_texts/kjh_text_13_clean.txt',
    ]
    kjh_texts = []
    ru_texts = []
    for path in paths:
        with open(path, "r", encoding="utf8") as f:
            text = f.read()
        kjh_texts.append(text)

        with open(path.replace('kjh_text_', 'ru_text_'), "r", encoding="utf8") as f1:
            r_text = f1.read()
        ru_texts.append(r_text)

    kjh_full_text = ' '.join(kjh_texts)
    ru_full_text = ' '.join(ru_texts)

    print(sorted(set(kjh_full_text)))
    print(sorted(set(ru_full_text)))



if __name__ == '__main__':
    main()
