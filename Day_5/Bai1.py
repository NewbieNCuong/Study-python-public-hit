n = int(input("Nhap so luong sinh vien = "))
a = {}
for i in range(0, n):
    ma_sv = input("Nhap ma sv: ")
    diemtb = float(input("Nhap diem TB = "))
    a[ma_sv] = diemtb
cnt = 0
for value in a.values():
    if(value >= 2.5 and value <= 3.5):
        cnt += 1
print("So sinh vien trong doan[2.5, 3.5] la: ", cnt)
print("Nhap them 1 sinh vien: ")
ma_sv = input("Nhap ma sv: ")
diemtb = float(input("Nhap diem TB = "))
a[ma_sv] = diemtb
atmp = []
for key in a:
    if(a[key] < 2.0):
        atmp.append(key)
for i in atmp:
    a.pop(i)
print(a)