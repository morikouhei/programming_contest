n,k = map(int,input().split())
S = [ord(s)-ord("a") for s in input()]
ans = 10**20

for i in range(1,n+1):
    if n%i:
        continue
    count = 0

    r = n//i
    for j in range(i):
        l = [0]*26
        for x in range(r):
            l[S[x*i+j]] += 1
        count += r-max(l)
    if count <= k:
        ans = min(ans,i)
print(ans) 