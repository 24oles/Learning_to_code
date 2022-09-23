a, b, c, d = int(input()), int(input()), int(input()), int(input())
x = a - c
y = b - d
if -1 <= x <= 1 and -1 <= y <= 1:
    print("YES")
else:
    print("NO")