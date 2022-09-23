n, a, b = int(input()), 0, 1
if n == 1:
    print("1")
else: 
    print(1, end = " ")
    for i in range(1, n):
        fn = a + b
        print(fn, end = " ")
        a = b
        b = fn
        fn = 0