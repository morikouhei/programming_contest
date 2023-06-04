n,m,d = map(int,input().split())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))

B = [-10**20] + B + [10**20]

ans = -1

nl = 0
nr = 0

for a in A:
    while B[nl] < a-d:
        nl += 1
    
    while B[nr] <= a+d:
        nr += 1

    
    if abs(a - B[nl]) <= d:
        ans = max(ans,a+B[nl])
    
    if abs(a-B[nr-1]) <= d:
        ans = max(ans,a+B[nr-1])
print(ans)