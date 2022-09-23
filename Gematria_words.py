words = []

def gematria(x):
    return sum(ord(i.upper()) - 65 for i in x.upper())
    
for i in range(int(input())):
    w = input()
    words.append(w)

words.sort()
print(*sorted(words, key=gematria), sep='\n')