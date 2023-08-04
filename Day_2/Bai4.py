
def fibonancci(n):
    a = [0, 1, 1]
    for i in range(3, n + 1):
        a.append(a[i - 1] + a[i - 2])
    return a
    
# def fibonancci(n):
#     if(n == 1 or n == 2): return 1
#     return fibonancci(n - 1) + fibonancci(n - 2)

if __name__ == '__main__':
    n = int(input())
    print(fibonancci(n))