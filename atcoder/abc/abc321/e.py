def solve():
    n,x,k = map(int,input().split())
    ans = 0
    bx = -1
    if k >= 120:
        return 0
        
    for i in range(60):
        if k == 0:
            ans += 1
            break

        li = x*2
        if li != bx:

            lli = li << (k-1)
            rri = min(n,lli + (1<<k-1)-1)

            if lli <= n:
                ans += rri - lli + 1

        ri = x*2+1
        if ri != bx:

            lli = ri << (k-1)
            rri = min(n,lli + (1<<k-1)-1)

            if lli <= n:
                ans += rri - lli + 1

        bx = x
        x = x//2
        k -= 1
        
        if x == 0:
            break


    return ans

t = int(input())
for _ in range(t):
    print(solve())
