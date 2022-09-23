a = int(input())
if a == 0:
    print("зеленый")
elif a < 0 or a > 36:
    print("ошибка ввода")
elif a <= 10 or 19 <= a <= 28:
    if a % 2 == 0:
        print("черный")
    else:
        print("красный")
else:
    if a % 2 == 0:
        print("красный")
    else:
        print("черный")