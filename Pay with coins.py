n = int(input())
for i in range(1, ((n+1)//2 + 1)):
    print("*" * i)
a = n//2
for i in range(a):
    print("*" * a)
    a -=1