n = int(input())
a = []
while n > 0:
    name, x = map(str, input().split())
    a.append([name, int(x)])
    n -= 1
y = int(input())
tmp = "LONGMA"
def cmp(x):
    return x[1]    
a_change = sorted(a, key = cmp)
print(a_change)
if(a_change[len(a_change) - 1][1] > y):
    print("YES")
elif(a_change[len(a_change) - 1][1] == y and len(a_change[len(a_change) - 1][0]) > len(tmp)):
    print("YES")
elif(a_change[len(a_change) - 1][1] == y and len(a_change[len(a_change) - 1][0]) == len(tmp)):
    print("NO")
elif(a_change[len(a_change) - 1][1] == y and len(a_change[len(a_change) - 1][0]) < len(tmp)):
    print("NO")
else:
    print("NO")

