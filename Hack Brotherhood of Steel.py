lines = int(input().lstrip('#'))
code = []
for _ in range(lines):
    code.append(input())
for i in code:
    x = i.rfind('#')
    if x > 0:
        i = i[:x].rstrip()
    print(i)