a, b = int(input()), int(input())
maxx_num = 0 # число с максимальной суммой делителей
maxx_sum = 0 # сумму его делителей
total = 0
numm = 0
for i in range (a, b + 1): 
    total = 0
    for j in range (1, i + 1): 
        if i % j == 0:
            total += j
            if total >= maxx_sum:
                maxx_sum = total
                maxx_num = j
print(maxx_num, maxx_sum)