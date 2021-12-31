def tup(tutors, klasses):
    i = 0
    for el in tutors:
        if i <= len(klasses) - 1:
            yield el, klasses[i]
            i += 1
        else:
            yield el, None


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Александр', 'Егор'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б'
]

tup_names_klass = tup(tutors, klasses)
print(next(tup_names_klass))
print(next(tup_names_klass))
print(next(tup_names_klass))
print(*tup_names_klass)
