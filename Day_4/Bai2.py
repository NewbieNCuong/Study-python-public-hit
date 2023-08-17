while True:
    n = (int)(input())
    if(n > 0):
        break

s = {i for i in map(int, input().split())}
key = int(input())
tmp = tuple(s)
sorted(tmp)
tmp1 = 0
res = []
# Trường hợp toàn số 0
if(tmp1 == key):
    for i in tmp:
        if(i == 0):
            res.append(0)
    print(set(res))
    exit()

for i in tmp:
    if(tmp1 >= key):
        break
    tmp1 += i
    res.append(i)
if(tmp1 > key): res.pop()
print(set(res))