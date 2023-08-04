# ĐPT: n * log(n)
def checkArmstrong(n):
    n1 = str(n)
    a = list(n1)
    tmp = 0
    for i in a:
        tmp += pow(int(i), 3)
    if(tmp == n): return True
    return False

# ĐPT: k * n (k số lượng số của n)
# def checkArmstrong(n):
#     tmp1 = n
#     res = 0
#     while(n > 0):
#         tmp = n % 10
#         res += pow(tmp, 3)
#         n //= 10
#     if res == tmp1: return True
#     else: return False

if __name__ == '__main__':
    n = int(input())
    for i in range(0, n + 1):
        if(checkArmstrong(i)):
            print(i, end = " ")
