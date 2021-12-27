def num_translate_adv(num):
    letter_one = num[0]
    num = num.lower()
    translate = {'zero': '"ноль"',
                 'one': '"один"',
                 'two': '"два"',
                 'three': '"три"',
                 'four': '"четыре"',
                 'five': '"пять"',
                 'six': '"шесть"',
                 'sever': '"семь"',
                 'eight': '"восемь"',
                 'nine': '"девять"',
                 'ten': '"десять"', }
    answer = translate.get(num)
    if letter_one.isupper():
        answer = answer.title()
        return print(answer)
    else:
        return print(answer)


num_translate_adv("one")
