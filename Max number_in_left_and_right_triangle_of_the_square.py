N = int(input())
matrix = [[int(i) for i in input().split()] for j in range(N)]

max_l = matrix[0][0]
max_r = matrix[0][0]

for i in range(N):
    for j in range(N):
        if i >= j and i <= N-1-j:
            if matrix[i][j] > max_l:
                max_l = matrix[i][j]
        if i <= j and i >= N-1-j:
            if matrix[i][j] > max_r:
                max_r = matrix[i][j]
print(max(max_l, max_r))