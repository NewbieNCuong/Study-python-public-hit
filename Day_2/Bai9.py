# def phanacach1(n):
#     cnt = 0
#     while(n > 0):
#         cnt += 1
#         n //= 2
#     return cnt

def phanacach2(n):
    cnt = 0
    while n:
        cnt += 1
        n >>= 1
    return cnt

def phanb():
    x = "awesome"
    print("Python is", x)
    print('Python is {}'.format(x))
    print('Python is %s'%x)
    print(f'Python is {x}')

# def phanc():
#     # python --version

if __name__ == '__main__':
    n = int(input())
    n = abs(n)
    print(phanacach2(n))
    phanb()