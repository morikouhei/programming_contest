t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    k = 2**m-n
    l = [-1]
    for i in range(n):
        s = input()[::-1]
        c = 0
        for j in range(m):
            if s[j] == "1":
                c += pow(2,j)
        l.append(c)
    l.sort()
    l.append(2**m)
    count = (k+1)//2
    for i in range(1,n+2):
        dif = l[i]-l[i-1]-1
        if dif < count:
            count -= dif
        else:
            ans = l[i-1]+count
            break
    ans = bin(ans)[2:]
    print(ans.zfill(m))
