t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = input()
    check = True
    l = [0]*61
    for i in range(n-1,-1,-1):
        x = a[i]
        for j in range(60,-1,-1):
            if x & (1<<j):
                x ^= l[j]

        if s[i] == "0":
            if x:
                l[x.bit_length()-1] = x
        else:
            if x:
                print(1)
                check = False
                break
    if check:
        print(0)
                


