def thesaurus(*elements):
    dict = {}
    for el in elements:
        letter_name = el[0]
        if letter_name in dict:
            dict[letter_name] = dict.setdefault(letter_name, []) + [el]
        else:
            dict[letter_name] = [el]
    print('{')
    for key, value in dict.items():
        print('  ', key, ':', value, )
    print('}')



thesaurus("Иван", "Мария", "Петр", "Илья")
