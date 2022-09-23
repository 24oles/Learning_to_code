x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
a = (x1 + y1)
b = (x2 + y2)
if a == b:
    print("YES")
elif ((a - b) % 2 == 0 or (b - a) % 2 == 0) and (x1 - x2) == (y1 - y2):
    print("YES")
else: 
    print("NO")