from Bai5 import BCNN

def Lcm(*args):
    x = list(args)
    if len(x) < 2:
        return x[0]
    res = BCNN(x[0], x[1])
    for i in range(2, len(x)):
        res = BCNN(res, x[i])
    return res

n = list(map(int, input().split()))
print(Lcm(*n))