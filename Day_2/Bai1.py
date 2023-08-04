'''def phanacach1(n):
    tmp =  str(n)
    res = 0
    for i in tmp:
        res += int(i)
    return res

def phanacach2(n):
    res = 0
    while n > 0:
        tmp = n % 10
        res += tmp
        n //= 10
    return res
if __name__ == '__main__':
    n = int(input())
    print(phanacach1(n))
    print(phanacach2(n))'''


'''def phanb(n):
    cnt = 0
    for i in range(2, n):
        if(n % i == 0):
            cnt += 1
    if cnt != 0: return False
    return True
if __name__ == '__main__':
    n = int(input())
    if(phanb(n) == True):
        print("n la so nguyen to")
    else:
        print("n khong la so nguyen to")
'''

# def phanc(n):
#     res = 0
#     for i in range(2, n + 1):
#         if n % i == 0:
#             res += i
#     return res

# if __name__ == '__main__':
#     n = int(input())
#     print(phanc(n))

def generate_pascal_triangle(n):
    pascal_triangle = []
    for i in range(n):
        if i == 0:
            pascal_triangle.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
            row.append(1)
            pascal_triangle.append(row)
    return pascal_triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    try:
        N = int(input("Nhập số hàng của tam giác Pascal (N >= 1): "))
        if N < 1:
            raise ValueError("Số hàng phải lớn hơn hoặc bằng 1.")
        
        pascal_triangle = generate_pascal_triangle(N)
        print("Tam giác Pascal có", N, "hàng:")
        print_pascal_triangle(pascal_triangle)
        
    except ValueError as ve:
        print("Lỗi:", ve)
