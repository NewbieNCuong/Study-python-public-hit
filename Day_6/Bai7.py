import math
def tinh(b):
    return math.sqrt(b[0] ** 2 +  b[1] ** 2)
n = int(input())
a = []
for i in range(0, n):
    x = [i for i in map(int, input().split())]
    a.append(x)
b = sorted(a, key = tinh)
print(b)
