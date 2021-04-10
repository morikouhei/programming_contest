
def solve():
    m = int(input())
    L = [list(map(int,input().split())) for i in range(m)]
    s = 0
    for p,n in L:
        s += p*n
    for i in range(s,max(1,s-5000),-1):
        count = 0
        num = i
        check = True
        for p,n in L:
            c = 0
            while num%p == 0:
                num //= p
                c += 1
            if n < c:
                check = False
                break
            count += (n-c)*p
        if num == 1 and i == count:
            return count
        
    return 0
    
    

T = int(input())
for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1,ans))