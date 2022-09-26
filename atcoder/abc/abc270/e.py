n,k = map(int,input().split())
A = list(map(int,input().split()))

def calc(m):
    num = 0
    for a in A:
        num += min(a,m)
    return num >= k

l = 0
r = k+2

while r > l + 1:
    m = (r+l)//2

    if calc(m):
        r = m
    else:
        l = m


num = 0
ans = []
for a in A:
    num += min(a,r-1)
    ans.append(a-min(a,r-1))
for i in range(n):
    if num < k and ans[i]:
        ans[i] -= 1
        num += 1
print(*ans)