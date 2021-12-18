duration = int(input())
if duration < 60:
    print(duration, 'сек')
elif duration < 3600:
    minutes = duration // 60
    sec = duration % 60
    print(minutes, 'мин', sec, 'сек')
elif duration < 3600 * 24:
    sec = duration % 60
    minutes = duration // 60
    hour = minutes // 60
    minutes = minutes % 60
    print(hour, 'час', minutes, 'мин', sec, 'сек')
else:
    sec = duration % 60
    minutes = duration // 60
    hour = minutes // 60
    days = hour // 24
    hour = hour % 24
    minutes = minutes % 60
    print(days, 'дн', hour, 'час', minutes, 'мин', sec, 'сек')

# # Проверка списком
# list_sec = list(map(int, input().split()))
# for duration in list_sec:
#     if duration < 60:
#         print(duration, 'сек')
#     elif duration < 3600:
#         minutes = duration // 60
#         sec = duration % 60
#         print(minutes, 'мин', sec, 'сек')
#     elif duration < 3600 * 24:
#         sec = duration % 60
#         minutes = duration // 60
#         hour = minutes // 60
#         minutes = minutes % 60
#         print(hour, 'час', minutes, 'мин', sec, 'сек')
#     else:
#         sec = duration % 60
#         minutes = duration // 60
#         hour = minutes // 60
#         days = hour // 24
#         hour = hour % 24
#         minutes = minutes % 60
#         print(days, 'дн', hour, 'час', minutes, 'мин', sec, 'сек')
