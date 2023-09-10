def change():
    n, m = map(int, input().split())
    a = []
    for i in range(0, n):
        x = [i for i in map(int, input().split())]
        a.append(x)
    i, j = 0, 0
    while(j <= m - 1):
        for k in range(0, n):
            print(a[k][j], end = " ")
        print()
        j += 1
    print("Va mang ban dau la: ")
    for i in range(0, n):
        for j in range(0, m):
            print(a[i][j], end = " ")
        print()
change()