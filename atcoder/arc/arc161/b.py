def solve():

    n = int(input())

    dp0 = [-1]*4

    dp1 = [-1]*4

    dp0[0] = 0

    
    for i in range(len(bin(n))-2)[::-1]:
        s = n >> i & 1
        # print(dp0,dp1)
        # print(1<<i,s)
        for j in range(3)[::-1]:
            if dp1[j] != -1:
                dp1[j+1] = max(dp1[j+1],dp1[j]+(1<<i))
        
        if s:
            for j in range(4):
                dp1[j] = max(dp1[j],dp0[j])
            
            for j in range(3)[::-1]:
                if dp0[j] != -1:
                    dp0[j+1] = max(dp0[j+1],dp0[j]+(1<<i))
        
    

    ans = max(dp0[-1],dp1[-1])

    if ans == -1:
        ans = -1
    return ans


t = int(input())
for _ in range(t):
    print(solve())