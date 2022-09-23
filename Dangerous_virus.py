s1 = {'write' : 'W', 'read': 'R', 'execute': 'X'}

s2 = {}
for _ in range(int(input())):
    a, b = input().split(' ', 1)
    s2[a] = b

for _ in range(int(input())):
    action, file = input().split() 
    print(('Access denied', 'OK')[s1[action] in s2[file]])  