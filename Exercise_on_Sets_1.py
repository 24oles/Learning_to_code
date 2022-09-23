m = int(input()) + int(input())
one = list(input() for _ in range(m))
set1 = set()
for i in one:
    if one.count(i) == 1:
        set1.add(i) 
if len(set1) > 0:
    print(len(set1))
else:
    print('NO')