import bisect
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.append(10**20)
B.append(-10**20)

ans = 10**20

B.sort()
for a in A:
    ind = bisect.bisect_left(B,a)
    ans = min(ans,a-B[ind-1],B[ind]-a)
print(ans)