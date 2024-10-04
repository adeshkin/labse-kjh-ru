import re


def find_words(text, char):
    return re.findall(f"\w*{char}\w*", text)


def main():
    path = 'data/kjh_ru_texts/kjh_text_1.txt'

    with open(path, "r", encoding="utf8") as f:
        text = f.read()
    print(sorted(set(text)))

    char = input("char: ")
    print(find_words(text, char))


if __name__ == '__main__':
    main()
