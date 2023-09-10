def bai3():
    a = [i for i in map(float, input().split())]
    tmp = lambda x : x > 0
    res = 0
    cnt  = 0
    for i in a:
        if(tmp(i) == True):
            res += i
            cnt += 1
    return res / cnt
    
print(bai3())