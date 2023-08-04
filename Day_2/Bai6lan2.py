def solve(n):
    res = []
    for i in range(0, n):
        if i == 0:
            res.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(res[i - 1][j - 1] + res[i - 1][j])
            row.append(1)
            res.append(row)
    return res

def inra(kq):
    for i in kq:
        # Cái này em học ở gpt: join là phương thức nối 1 list thành 1 chuỗi
        # Còn str(x) for x in i: cái này hay ghê: biến cả các biến trong i thành chuỗi xong mới dùng được join
        '''
            Em có thử cách này nma kh được:
            for i in kq:
                for j in i:
                    print(j, end = " ")
                print()
        '''
        print(" ".join(str(x) for x in i)) 

if __name__ == '__main__':
    n = int(input("Nhập số hàng của tam giác Pascal (N >= 1): "))
    tmp = solve(n)
    print("Tam giác Pascal có", n, "hàng:")
    inra(tmp)
