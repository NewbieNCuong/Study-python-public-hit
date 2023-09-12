def check():
    s = input()
    cnt = 0
    cnt1 = 0
    a =  []
    for i in range(0, len(s)):
        if(s[i].isdigit() == True):
            cnt += 1
            a.append(int(s[i]))
    if(cnt == len(s)):
        for i in range(0, len(a)):
            if(int(a[i]) > 0):
                cnt1 += 1
        if(cnt1 == len(a)):
            print("The string is number only")
    else:
        print(s.lower())
        print(s.upper())
        print(s[0].upper(), end = "")
        print(s[1:].lower())

check()
