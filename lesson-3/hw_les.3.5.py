from random import choice, randint


def get_jokes(n, rep=True):
    """creates jokes from list words,
    if rep = False each word is used in only one joke"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    answer = []
    i = n
    if rep:
        while i != 0:
            joke = choice(nouns), choice(adverbs), choice(adjectives)
            joke = " ".join(joke)
            i -= 1
            answer.append(joke)
        return print(answer)
    else:
        if i > 5:
            print("Max count jokes, 5")
            i = 5
        while i != 0:
            len_nouns = len(nouns)
            len_adverds = len(adverbs)
            len_adjective = len(adjectives)
            joke = nouns.pop(randint(0, len_nouns - 1)), \
                   adverbs.pop(randint(0, len_adverds - 1)), \
                   adjectives.pop(randint(0, len_adjective - 1))
            joke = " ".join(joke)
            i -= 1
            answer.append(joke)
        return print(answer)


get_jokes(5,False)
