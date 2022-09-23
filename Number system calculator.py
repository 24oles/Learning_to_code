def number_in_system(x, sys, loc): 
    ### сумма каждого дидвита в различной системе (от двуичной, до 16-ричной)
    num = x * (sys ** loc)
    return num

def digit_list(n):
    ### разбиваем число на список из диджитов в 10-чной системе
    x = []
    for i in str(n): 
        if i.isdigit():
            i = int(i)
        elif i == 'A':
            i = 10
        elif i == 'B':
            i = 11
        elif i == 'C':
            i = 12
        elif i == 'D':
            i = 13
        elif i == 'E':
            i = 14
        elif i == 'F':
            i = 15
        x.append(i)
    return x

# вход данных 
print('Введите число: ')
n = input()
print('Введите систему изчисления: ')
sys = int(input())
print('Считаем . . .')
summ = 0        # значение инпута в десятичной системе

x = digit_list(n)
loc = len(n) - 1

for i in x:
    print(i, '*' , sys, '**', loc)
    summ += number_in_system(i, sys, loc)
    loc -= 1
    
print()
print('Введеное число в десятичной системе: ', summ)