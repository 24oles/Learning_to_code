ip_list = []
for _ in range(int(input())):
    ip = [int(i) for i in input().split('.')]
    ip_list.append(ip)
ip_list.sort()    
for i in ip_list:
    x = [str(j) for j in i]
    print('.'.join(x))