class Phieunhaphang:
    def __init__(self, maphieu = "", mancc = "", ngaylap = "", tenncc = "", diachi = ""):
        self.maphieu = maphieu
        self.mancc = mancc
        self.ngaylap = ngaylap
        self.tenncc = tenncc
        self.diachi = diachi
    def input(self):
        self.maphieu = input("Nhập mã phiếu: ")
        self.mancc = input("Nhập mã ncc: ")
        self.ngaylap = input("Nhập ngày lập: ")
        self.tenncc = input("Nhập tên ncc: ")
        self.diachi = input("Nhập địa chỉ: ")
    def output(self):
        print("{:>32}".format("Phiếu Nhập Hàng"))
        print("{}".format("Mã Phiếu: "), end = "")
        print(self.maphieu, end = "")
        print("{:>18}".format("Ngày lập: "), end = "")
        print(self.ngaylap)
        print("{}".format("Mã NCC: "), end = "")
        print(self.mancc, end = "")
        print("{:>20}".format("Tên NCC: "), end = "")
        print(self.tenncc)
        print("{}".format("Địa chỉ: "), end = "")
        print(self.diachi)

class merchandise:
    def __init__(self, tenhang = "", dongia = 0.0, soluong = 0):
        self.tenhang = tenhang
        self.dongia = dongia
        self.soluong = soluong
        self.thanhtien = self.dongia * self.soluong
    def input(self):
        self.tenhang = input("Nhập tên hàng: ")
        self.dongia = float(input("Nhập đơn giá: "))
        self.soluong = int(input("Nhập số lượng: "))
        self.thanhtien = self.dongia * self.soluong
    def output(self):
        print(self.tenhang, end = "")
        print("{:>20}".format(self.dongia), end = "")
        print("{:>35}".format(self.soluong), end = "")
        print("{:>40.2f}".format(self.thanhtien))

if __name__ == "__main__":
    phieunhaphang = Phieunhaphang("PH001", "NCC1", "1/1/2007", "LG-Electronic", "Khu công nghiệp Như Quỳnh A")
    phieunhaphang.output()
    tivi = merchandise("Tivi", 30, 2)
    quat = merchandise("Quạt", 1.2, 3)
    mobi = merchandise("Mobi", 5, 10)
    print("{:>5}".format("Tên Hàng"), end = "")
    print("{:>20}".format("Đơn giá"), end = "")
    print("{:>35}".format("Số lượng"), end = "")
    print("{:>40}".format("Thành Tiền"))
    tivi.output()
    quat.output()
    mobi.output()
    print("{:>94}".format("Cộng thành tiền: "), end = "")
    print("{:>4}".format(tivi.thanhtien + quat.thanhtien + mobi.thanhtien))





