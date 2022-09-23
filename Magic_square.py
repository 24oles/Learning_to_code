# занести данные в матрицу
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
        
# сделать плоскую матрицу чтобы проверить последовательность
flat_matrix = []
flag1 = True
for i in range(n): 
    for j in range(n):
        flat_matrix.append(matrix[i][j])

# Условие 1. Проверить наличие последовательности в матрице только однажды. 
for i in range(1, n ** 2 + 1):
    if 0 == flat_matrix.count(i) or flat_matrix.count(i) > 1:
        flag1 = False
        break
    
# сумма столблов в один массив
summ_stolb = []
for i in range(n):
    stolb = 0
    for j in range(n):
        stolb += matrix[j][i]
    summ_stolb.append(stolb)

# условие 2.3 проверить столбци и строки
flag2 = True
flag3 = True
for i in range(n - 1):
    if sum(matrix[i]) != sum(matrix[i + 1]):
        flag2 = False
    if summ_stolb[i] != summ_stolb[i + 1]:
        flag3 = False

if flag1 and flag2 and flag3 == True:
    print('YES')
else: 
    print('NO')