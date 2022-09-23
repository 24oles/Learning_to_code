n = 8
m = [['.'] * n for _ in range(n)]
x = input()
col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
row = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
x1 = row.get(x[1])
x2 = col.get(x[0])


for i in range(n):
    for j in range(n):
        if i + j == x1 + x2 or i == x1 or j == x2 or i - j == x1 - x2:
            m[i][j] = '*'
            
m[x1][x2] = 'Q'
# i + j == n - 1 or i == (n-1)/2 or j == (n-1)/2:

for i in m:
    print(*i)