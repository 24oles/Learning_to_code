import string
from random import choice, shuffle

chars1 = [с for с in string.ascii_uppercase if с not in 'OI']
chars2 = [с for с in string.ascii_lowercase if с not in 'ol']
chars3 = list(string.digits[2:])
chars = chars1 + chars2 + chars3

def generate_password(length):
    result = [choice(i) for i in (chars1, chars2, chars3)] + [choice(chars) for _ in range(3, length)]
    shuffle(result)
    return ''.join(result)

def generate_passwords(count, length):
    result = set()
    while len(result) < count:
        result.add(generate_password(length))
    return list(result)

for i in generate_passwords(int(input()), int(input())):
    print(i)