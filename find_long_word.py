import nltk

nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize


def main():
    paths = [
        'data/kjh_ru_texts/ru_text_1_clean.txt',
        'data/kjh_ru_texts/ru_text_2_clean.txt',
        'data/kjh_ru_texts/ru_text_3_clean.txt',
        'data/kjh_ru_texts/ru_text_7_clean.txt',
        'data/kjh_ru_texts/ru_text_8_clean.txt',
        'data/kjh_ru_texts/ru_text_13_clean.txt',
    ]

    for path in paths:
        with open(path, "r", encoding="utf8") as f:
            text = f.read()

        words = word_tokenize(text)
        for word in words:
            if len(word) >= 15:
                print(path)
                print(word)
                print('\n')


def main1():
    paths = [
        'data/kjh_ru_texts/ru_text_1_clean.txt',
        'data/kjh_ru_texts/ru_text_2_clean.txt',
        'data/kjh_ru_texts/ru_text_3_clean.txt',
        'data/kjh_ru_texts/ru_text_7_clean.txt',
        'data/kjh_ru_texts/ru_text_8_clean.txt',
        'data/kjh_ru_texts/ru_text_13_clean.txt',
    ]

    for path in paths:
        with open(path, "r", encoding="utf8") as f:
            text = f.read()

        words = word_tokenize(text)
        for word in words:
            if len(word) >= 10:
                print(path)
                print(word)
                print('\n')


if __name__ == '__main__':
    main1()
