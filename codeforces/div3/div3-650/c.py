t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l = input()
    s = []
    for i in range(n):
        if l[i] =="1":
            s.append(i)
    count = 0
    if s == []:
        count += (n+k)//(k+1)
    else:
        count += (s[0])//(k+1)
        count += (n-1-s[-1])//(k+1)

        for i in range(len(s)-1):
            if s[i+1]-s[i] >= 2*k+1:
                count += (s[i+1]-s[i]-1-k)//(k+1)
    print(count)