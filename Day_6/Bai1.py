a, b = map(str, input().split())
res = lambda x, y: x > y
print(a) if res(a, b) == True else print(b)