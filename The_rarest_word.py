dct = {}
lst = [word.strip('.,!?:;-') for word in input().lower().split()]
for word in lst:
    dct[word] = dct.get(word, 0) + 1
lst = [(value, key) for key, value in dct.items()]
lst.sort()
print(lst[0][1])