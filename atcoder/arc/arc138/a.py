import bisect
n,k = map(int,input().split())
A = list(map(int,input().split()))
nA = [[A[i],i] for i in range(k,n)]

nA.sort()
l = []
for a,i in nA[::-1]:
    if l == []:
        l.append(i)
    else:
        l.append(min(i,l[-1]))
l = l[::-1]
sA = [a for a,_ in nA]
ans = 10**10
for i in range(k):
    a = A[i]
    ind = bisect.bisect_right(sA,a)
    if ind == len(sA):
        continue
    ans = min(ans,l[ind]-i)
if ans == 10**10:
    ans = -1
print(ans)


