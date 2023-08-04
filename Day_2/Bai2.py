a = int(input())
b = int(input())
print('{} + {} = {}'.format(a, b, a + b)) 
print('{} - {} = {}'.format(a, b, a - b)) 
print('{} * {} = {}'.format(a, b, a * b)) 
print('{} // {} = {}'.format(a, b, a // b)) 
print('{} ^ {} = {}'.format(a, b, a ** b)) 
print('{} % {} = {}'.format(a, b, a % b)) 
if a > b:
    print("a lon b")
elif(a == b):
    print("a == b")
else:
    print("a be hon b")
print('{} and {} = {}'.format(a, b, a&b))
print('{} or {} = {}'.format(a, b, a|b))
print('{} XOR {} = {}'.format(a, b, a^b))
print('NOT {} == {} = {}'.format(a, b, a != b))
print('{} >> 1 = {}'.format(a, a >> 1))
print('{} << 1 = {}'.format(a, a << 1))




