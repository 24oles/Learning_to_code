n, final, midl = input().split(), [[]], []
for i in range(len(n)):
    for j in range(len(n)):
        midl = n[j:i + j + 1]
        if len(midl) == i + 1:
            final.append(midl)
print(final)