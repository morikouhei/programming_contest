t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    S = input()
    if S.count("*") == 1:
        print(1)
        continue
    l = []
    for i in range(n):
        if S[i] == "*":
            l.append(i)
    
    last = l[0]
    ans = 0
    for i in range(1,len(l)-1):
        if l[i] - last > k:
            if last == l[i-1]:
                last = l[i]
                ans += 1
            else:
                last = l[i-1]
                ans += 1
    if l[-1] - last > k:
        ans += 1
    print(ans+2)