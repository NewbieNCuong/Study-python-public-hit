# Phần a
a = [i for i in map(int, input("Danh sach n so nguyen la: ").split())]
x = int(input("Nhap x = "))
print("So lan xuat hien X trong list la:", a.count(x))
# Phần b
a[2: 8] = [6, 9, 7, 0 , 8, 0]
# Phần c
print(max(a))
print(min(a))
# Phần d
x1 = int(input("Nhap so X1 = "))
a.insert(0, x1)
# Phần e
print("NO")
# Phần f
print(a)
b = []
tmp = 0
for i in range(0, len(a)):
    tmp += a[i]
    b.append(tmp)
print(b)
# Phần g
def cmp(a):
    return abs(a)

c =  [-1, 5, -76, 120, 234, 1000, -12, -7, 35]
c1 = sorted(c, key = cmp)
c.sort()
print(c)
print(c1)