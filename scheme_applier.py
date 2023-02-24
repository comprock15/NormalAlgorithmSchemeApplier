# пустая подстановка
eps = "eps"


# получить список из файла
def get_list_from_file(filename):
    with open(file=filename, mode='r') as f:
        lines = [line.rstrip() for line in f]
    return lines


# напечатать схему
def print_scheme(scheme):
    for substitution in scheme:
        print(substitution)
    print()


# применить схему к слову
def apply_scheme(scheme, word):
    if word == eps:
        word = ""

    if word == "":
        print(eps, end='')
    else:
        print(word, end='')

    # проход по подстановкам
    for substitution in scheme:
        final = False
        item_to_replace, replacement = "", ""

        if substitution.find("->.") != -1: # подстановка конечная
            item_to_replace, replacement = substitution.split(" ->. ")
            final = True
        else: # подстановка не конечная
            item_to_replace, replacement = substitution.split(" -> ")

        if item_to_replace == eps:
            item_to_replace = ""
        if replacement == eps:
            replacement = ""

        # подстановку можно применить
        if word.find(item_to_replace) != -1:
            print(" => ", end="")
            word = word.replace(item_to_replace, replacement, 1)
            if not final:
                apply_scheme(scheme, word)
            else:
                if word == "":
                    print(eps)
                else:
                    print(word)
            break
    # схема не применима
    else:
        print()


if __name__ == "__main__":
    scheme_filename = "scheme.txt"
    words_filename = "words.txt"

    scheme = get_list_from_file(scheme_filename)
    print("Scheme:")
    print_scheme(scheme)

    words = get_list_from_file(words_filename)

    for word in words:
        apply_scheme(scheme, word)

    input()
