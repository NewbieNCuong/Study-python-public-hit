n = int(input())
a = [i for i in map(str, input().split())]
res = []
for tmp in a:
    if(tmp[len(tmp) - 1] == '1' or tmp[len(tmp) - 1] == '3' or tmp[len(tmp) - 1] == '5' or tmp[len(tmp) - 1] == '7' or tmp[len(tmp) - 1] == '9'):
        res.append(int(tmp))
print(len(res))
res.sort()
print(res)