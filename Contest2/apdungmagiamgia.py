def check(s):
    cnt = 0
    for i in range(0, len(s)):
        if(s[i].isdigit() == True):
            cnt += 1
    if(cnt == len(s)):
        return True
    return False
def convert(s):
    res = 0
    for i in range(0, len(s)):
        res = res * 10 + int(s[i])
    return res

a = [i for i in map(str, input().split())]
b = int(input())
res = []
for i in range(0, len(a)):
    if(a[i][0] == '$'):
        if(check(a[i][1:]) == True):
            tmp = convert(a[i][1:])
            tmp = tmp - b/100 * tmp
            x = '$' + str(tmp)
            res.append(x)
        else: res.append(a[i])
    else: res.append(a[i])
for i in range(0, len(res)):
    if(a[i] != res[i]):
        c = float(res[i][1:])
        print("$", end = "")
        print("{:.2f}".format(c), end = " ")
    else: print(res[i], end = " ")