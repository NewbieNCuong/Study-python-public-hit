def check(tmp):
    cnt1 = 0
    cnt2 = 0
    for i in range(0, len(tmp)):
        if(tmp[i] >= '0' and tmp[i] <= '9'):
            cnt1 += 1
            continue
        if(tmp[i] >= 'a' and tmp[i] <= 'z'):
            cnt2 += 1
            continue
        else:
            return False
    if(cnt1 > 0 and cnt2 > 0):
        return True
    else: 
        return False
n = int(input())
a = [i for i in map(str, input().split())]
res = 0
for tmp in a:
    if(check(tmp)):
        res += 1
print(res)