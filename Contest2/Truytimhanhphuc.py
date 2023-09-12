def check1(x, y):
    tmp = 0
    for i in range(1, y):
        if( y % i == 0):
            tmp += i
    if(x == tmp):
        return True
    return False

def check2(x, y):
    tmp = 0
    for i in range(1, y):
        if( y % i == 0):
            tmp += i
    if(tmp - x == 1):
        return True
    return False

a = [i for i in map(int, input().split())]
b = sorted(a)
restt = 0
reshh = 0
i = 0
while(i < len(b) - 1):
    for j in range(0, len(b)):
        if(check1(b[i], b[j] == True or check1(b[j], b[i]) == True)):
            restt += 1
        if(check2(b[i], b[j]) == True or check2(b[j], b[i]) == True):
            reshh += 1
    i += 1
print(restt, end = " ")
print(reshh)

