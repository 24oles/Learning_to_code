# занести данные в матрицу
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
        
# сделать последовательность
flat_matrix = [*range(1, n+1)]
# сделать второй вариант перевернутой матрицы
matrix1 = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    matrix1.append(row)
# for i in matrix1:
#    print(*i)

#Проверить наличие последовательности в матрице только однажды
flag1 = True
for i in range(n):
    for j in range(n):
        if flat_matrix[i] not in matrix[j]: # проверка по строкам
            flag1 = False
            break
        if flat_matrix[i] not in matrix1[j]: # проверка по строкам в перевернутой матрице (столбцы)
            flag1 = False
            break
    if flag1 == False:
        break

if flag1 == True:
    print('YES')
else: 
    print('NO')