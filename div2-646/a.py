t = int(input())
for _ in range(t):
    s = input()
    a = [0]
    b = [0]
    for i in range(len(s)):
        if s[i] == "1":
            a.append(a[-1]+1)
        else:
            a.append(a[-1])
        if s[-1-i] == "0":
            b.append(b[-1]+1)
        else:
            b.append(b[-1])
    ans = float("INF")
    for i,j in zip(a,b[::-1]):
        ans = min(ans,i+j,len(s)-i-j)
    print(ans)

