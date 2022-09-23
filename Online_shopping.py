d1 = {}

for _ in range(int(input())):
    l = input().split()
    a, b, c = l[0], l[1], int(l[2])
    if a not in d1.keys():
        d1[a] = d1.setdefault(a, {b: c})
    else:
        if b not in d1[a]:
            d1[a].update({b : c})
        else:
            d1[a][b] = d1[a].get(b) + c

for i in sorted(d1):
    print(f'{i}:')
    for j in sorted(d1[i].items()):
        print(*j)