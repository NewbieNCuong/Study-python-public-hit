n = int(input())
a = [str(input()) for i in range(0, n)]
b = tuple(a)
print(b)
cnt = 0
for i in b:
    if(i.isdigit()):
        cnt += 1
print(cnt)