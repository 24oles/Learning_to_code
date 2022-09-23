n = input().split()
n1 = [[n[0]]]
for i in range(1, len(n)):
    if n[i] != n[i - 1]:
        n1.append([n[i]])
    else:
        n1[-1].append(n[i])

print(n1)