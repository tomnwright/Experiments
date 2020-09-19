translation_dict = {
    'a': '@',
    '_b': '8',
    '_c': '(',
    'd': '|)',
    'e': '3',
    'f': '#',
    'g': '6',
    'h': '[-]',
    'i': '|',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': '[]\\/[]',
    'n': '[]\\[]',
    'o': '0',
    'p': '|D',
    'q': '(,)',
    'r': '|Z',
    's': '$',
    't': '\'][\'',
    'u': '|_|',
    'v': '\\/',
    'w': '\\/\\/',
    'x': '}{',
    'y': '`/',
    'z': '2',
}


def translate(original: str):
    result = ''
    original = original.lower()

    for char in original:
        if char not in translation_dict:
            result += char
            continue

        new = translation_dict[char]
        result += new

    return result


text = str(input())
print(translate(text))