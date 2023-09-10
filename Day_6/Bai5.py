def UCLN(a, b):
    if b == 0:
        return a
    return UCLN(b, a % b)

def BCNN(a, b):
    return (a * b) // UCLN(a, b)
if __name__ == "__main__":
    a, b = map(int, input().split())
    print(BCNN(a, b))