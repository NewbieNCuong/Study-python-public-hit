def phana(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

def phanb(n):
    res = 0
    for i in range(1, n + 1):
        res += 1.0 * 1/i
    return res

def phanc(a, b, c):
    denta = b ** 2 - 4 * a * c
    if denta == 0:
        print("Phuong trinh co 2 nghiem bang nhau")
        print("x1 = x2 =", -1.0 * b / 2 * a)
    elif denta < 0:
        print("phuong trinh vo nghiem")
    else:
        print("x1 =", (-b + pow(denta, 1 / 2)) / 2 * a)
        print("x2 =", (-b - pow(denta, 1 / 2)) / 2 * a)

if __name__ == '__main__':
    # n = int(input())
    # print(phana(n))
    # print(phanb(n))
    print("Hay nhap a, b, c >= 0")
    a = int(input())
    b = int(input())
    c = int(input())
    print(phanc(a, b, c))
