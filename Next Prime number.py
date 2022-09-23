# объявление функции
def get_next_prime(num):
    flag = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            flag = False
    if num > 1 and flag == True:
        return True
    else:
        return False
        
# считываем данные
num = int(input())

# бесконечный цикл для поиска числа 
x = 0

while x == 0:
    num += 1
    get_next_prime(num)
    if get_next_prime(num) == True:
        print(num)
        break

# вызываем функцию но ответ на условие, а не ответ свмой функции
get_next_prime(num)