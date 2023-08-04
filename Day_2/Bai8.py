from math import *

def tinhtonguoccua1so(x):
    res = 0
    for i in range(1, x):
        if x % i == 0:
            res += i
    return res

# Duyệt tổng ước từ 2 -> n
def duyet(y):
    a = []
    for i in range(0, y + 1):
        a.append(tinhtonguoccua1so(i))
    return a

# Check xem từ 2 -> n có các cặp Amicable nào
def check(z):
    b = duyet(z)
    c = []
    for i in range(2, len(b)):
        if(b[i] <= z and b[i] != i and b[b[i]] == i):
            c.append((i, b[i]))
    return c

if __name__ == '__main__':
    n = int(input())
    print(check(n))