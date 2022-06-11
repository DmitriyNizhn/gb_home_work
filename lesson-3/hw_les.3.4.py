def thesaurus_adv(*name):
    name = list(name)
    name.sort(key=lambda x: x.split()[1])
    dict = {}
    for el in name:
        split_el = el.split()
        letter_surname = split_el[1][0]
        letter_name = split_el[0][0]
        if letter_surname in dict:
            if letter_name in dict[letter_surname]:
                dict[letter_surname][letter_name].append(el)
            else:
                dict[letter_surname][letter_name] = [el]
        else:
            dict.update({letter_surname: {letter_name: [el]}})
    print('{')
    for key in dict.keys():
        print(' ', key, ':', '{')
        for key1, value1 in dict[key].items():
            print('     ', key1, ':', value1)
    print("}")


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Агар Саитов",
              "Инна Ипатова", "Ирина Серова", "Игорь Семенков", "Игорь Игнатьев")
