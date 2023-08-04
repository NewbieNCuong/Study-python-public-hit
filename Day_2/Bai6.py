def checkperfectnumber(n):
    tmp = 0
    for i in range(1, n):
        if n % i == 0:
            tmp += i
    if tmp == n: return True
    return False

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        if checkperfectnumber(i):
            print(i, end = " ")

# Bài 7 là bài 3 phần c