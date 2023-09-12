class SV:
    def __init__(self, masv = "", hoten = "", namsinh = "", lop = "", gioitinh = ""):
        self.masv = masv
        self.hoten = hoten
        self.namsinh = namsinh
        self.lop = lop
        self.gioitinh = gioitinh
    def input(self):
        self.masv = input("Nhập mã SV: ")
        self.hoten = input("Nhập họ và tên: ")
        self.namsinh = input("Nhập năm sinh: ")
        self.lop = input("Nhập lớp: ")
        self.gioitinh = input("Nhập giới tính: ")
    def output(self):
        print("{:%s%s%s%s%s}".format(self.masv, self.hoten, self.namsinh, self.lop, self.gioitinh))
    def layten(self, a):
        for i in range(0, len(a)):
            c = a.self.hoten
            s = ""
            for i in range(len(c) - 1, 0):
                if c[i] == " ":
                    break
                s += c[i]
            print(s, end = " ")

