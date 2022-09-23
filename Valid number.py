n = input().strip().split('-')
if len(n) == 4:
    if n[0] == '7' and len(n[0]) == 1 and n[1].isdigit() and len(n[1]) == 3 and n[2].isdigit() and len(n[2]) == 3 and n[3].isdigit() and len(n[3]) == 4:
        print('YES')
    else:
        print('NO')
elif len(n) == 3:
    if n[0].isdigit() and len(n[0]) == 3 and n[1].isdigit() and len(n[1]) == 3 and n[2].isdigit() and len(n[2]) == 4:
        print('YES')
    else:
        print('NO')
else:
    print('NO')