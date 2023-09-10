def Input():
    a = [i for i in map(int, input().split())]
    return a
def tong(x, a):
    res = 0
    for i in range(0, x):
        res += a[i]
    return res

a = Input()
q = int(input())
while(q > 0):
    x = int(input())
    print(tong(x, a))
    q -= 1

