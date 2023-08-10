a, b, n = map(int, input().split())
res = []
for i in range(a, b + 1):
    if i % n == 0:
        res.append(i)
print(len(res))
print(res)