a = {i for i in map(int, input().split())}
b = list(a)
try:
    b.remove(11)
except:
    pass
if(len(b) == len(a)):
    a.add(11)
else:
    pass
print(a)
respair = []
sorted(a)
for i in b:
    if(b.count(11 - i) != 0):
        respair.append((i, 11 - i))
respair = set(respair)
respair = tuple(respair)
print(11*len(respair) / 2)



