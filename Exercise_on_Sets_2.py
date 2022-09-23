m = int(input())
l1 = {input() for _ in range(int(input()))}
lx = set()
for i in range(m - 1):
    for j in range(int(input())):
        lx.add(input())
    l1 &= lx
    lx.clear()
print(*sorted(l1), sep = '\n')