a = {i for i in map(int, input().split())}
b = {i for i in map(int, input().split())}
print("Sinh vien hoc tai 2 ban la:", a&b)
print("Danh sach cac sinh vien dang ky la:", a|b)
print("Danh sach cac sinh vien dang ky ban 1 ma khong dang ky ban 2 la:", a - b)
print("Danh sach cac sinh vien dang ky duy nhat 1 ban la: ", a - b, " va", b - a)