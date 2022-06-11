def num_translate(num):
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
    return print(translate.get(num))



num_translate("one")
