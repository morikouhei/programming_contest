def solve():
    l,r = map(int,input().split())

    sl = str(l)
    sr = str(r)

    if len(sl) == len(sr):
        return r-l+1
    
    if sr[0] != "1":
        base = 10**(len(sr)-1)
        return r - base + 1
    
    if len(sr) - len(sl) != 1:
        ans = 10**(len(sr)-1) - 10**(len(sr)-2)
        ans += min(r-10**(len(sr)-1),10**(len(sr)-2)-1)
        return ans
    

    return min(10**(len(sr)-1),r-l+1)
t = int(input())
for _ in range(t):
    print(solve())