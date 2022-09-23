a, b = int(input()), int(input()) # 1,5
for i in range(a, b + 1): # i = 1 till 5   a = 1   b 
    count = 0
    for j in range(1, b + 1):  # a = 1    j = 1 - 5   i = 1 till 5
         if i % j == 0:
                count += 1
    if count == 2:
         print(i)