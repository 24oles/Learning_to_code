def evaluate(coefficients, x):
    p = len(coefficients) # 2, 1, 0
    total = 0
    for i in coefficients: #x 2, 4, 3 = 2*(c**2) + 4*(c**1) + 3(c**0)
        p -= 1
        total += i * (x**p)   
    return total

print(evaluate(list(map(lambda x: int(x), input().split())), int(input())))