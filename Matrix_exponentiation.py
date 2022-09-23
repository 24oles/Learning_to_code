from copy import deepcopy

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
stp = int(input())

matrix1 = deepcopy(matrix) 

for st in range(stp - 1):
    matrix2 = [[0 for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix2[i][j] += matrix1[i][k] * matrix[k][j]
    matrix1 = deepcopy(matrix2)


for row in matrix2:
    print(*row)