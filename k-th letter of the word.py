words = []
word = []
for i in range(int(input())):
    a = input()
    words.append(a)
n_let = int(input())
for i in words:
    if len(i) >= n_let:
        print(i[n_let - 1], end = '')