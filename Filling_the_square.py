def find_c(chislo):
    while chislo > y:
        chislo -= y
    return chislo

n = [int(i) for i in input().split()]
x = n[0]
y = n[1]

for i in range(x):
    row = []
    for j in range(y):
        chislo = i + j + 1
        if chislo <= y:
            row.append(chislo)
        else: 
            row.append(find_c(i + j + 1))
    print(*row)