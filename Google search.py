list_base, list_sech, list_resu = [], [], []
count = 0
for i in range(int(input())):
    list_base.append(input())
n_serch = int(input())
for j in range(n_serch):
    list_sech.append(input())

for i in list_base:
    for j in list_sech:
        if j.lower() in i.lower():
            count += 1
            if count == n_serch:
                print(i)
    count = 0