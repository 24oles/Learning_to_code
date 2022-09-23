from fractions import Fraction as F
from math import gcd as gcd
n = int(input())
l = []

for n1 in range(1, n // 2 + n % 2):
    n2 = n - n1
    if n1 / n2 != int(n1/n2) and gcd(n1, n2) == 1:
        l.append(F(n1, n2))

print(l[-1])