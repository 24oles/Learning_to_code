n1, m1 = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for _ in range(n1)]
input()
n2, m2 = [int(i) for i in input().split()]
b = [[int(i) for i in input().split()] for _ in range(n2)]
c = [[0] * n1 for _ in range(m2)]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]

for row in c:
    print(*row)