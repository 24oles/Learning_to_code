# объявление функции
def compute_binom(n, k):
    s = factorial(n)/ (factorial(k) * (factorial(n-k)))
    return int(s)

def factorial(x):
    factorial = 1
    while x > 1:
        factorial *= x
        x -= 1
    return factorial

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))