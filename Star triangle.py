m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        if m % 2 == 1:
            print(m)
        m += 1
else: 
    for i in range(m, n - 1, -1):
        if m % 2 == 1:
            print(m)
        m -= 1