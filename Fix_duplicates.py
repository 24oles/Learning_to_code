n = input().split()
d = {}

for w in n:
    d[w] = d.get(w,-1) + 1
    if d[w] > 0:
        print(w, '_', d[w], sep = '', end = ' ')
    else: 
        print(w, sep = '', end = ' ')