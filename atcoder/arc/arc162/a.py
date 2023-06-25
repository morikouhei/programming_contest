def solve():
    n = int(input())
    P = list(map(int,input().split()))
    sP = [0]*n
    for i,p in enumerate(P,1):
        sP[p-1] = i

    
    ma = 0
    ans = 0
    for p in sP:
        if p > ma:
            ans += 1
            ma = p
    return ans


t = int(input())
for _ in range(t):
    print(solve())