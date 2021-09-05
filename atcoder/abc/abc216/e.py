n,k = map(int,input().split())
A = list(map(int,input().split()))
if sum(A) <= k:
    ans = 0
    for a in A:
        ans += a*(a+1)//2
    print(ans)
    exit()

def search(x):
    count = 0
    for a in A:
        if a < x:
            continue
        count += a-x+1
    return count
l = 0
r = 2*10**10
while r > l + 1:
    m = (r+l)//2
    if search(m) > k:
        l = m
    else:
        r = m

ans = 0
count = 0
cand = 0
for a in A:
    if a >= r:
        ans += a*(a+1)//2-l*(l+1)//2
        count += a-r+1
        cand += 1
    elif a == r-1:
        cand += 1
ans += min((k-count),cand)*(r-1)
print(ans)