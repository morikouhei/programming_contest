n,d,p = map(int,input().split())
F = list(map(int,input().split())) + [0]*d
F.sort(reverse=True)

ans = sum(F)
count = ans
for i in range((n+d-1)//d):

    count += p
    for j in range(d):
        count -= F[i*d+j]
    ans = min(ans,count)
print(ans)