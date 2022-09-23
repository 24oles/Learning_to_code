from random import randrange as R

n = [input() for i in range(int(input()))]

x = R(1,len(n))
santa = []
for i in range(len(n)):
    if i + x >= len(n):
        santa.append(n[i + x - len(n)])
    else:
        santa.append(n[i + x])

for i in range(len(n)):
    print(f'{n[i]} - {santa[i]}')