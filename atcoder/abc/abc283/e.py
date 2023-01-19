h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h)]

inf = 10**5
dp = [0,1,0,1]
left = []

def get_isolate(a):
    cand = []
    for i in range(w):
        x = a[i]
        if i and x^a[i-1] == 0:
            continue
        if i < w-1 and x^a[i+1] == 0:
            continue
        cand.append(i)
    return cand

cand = get_isolate(A[0])
for i in range(4):
    left.append(cand)


for a,na in zip(A,A[1:]):
    ndp = [inf]*4
    nleft = [[] for i in range(4)]
    ncand = get_isolate(na)

    for i in range(4):
        if dp[i] == inf:
            continue

        f = i & 1
        for j in range(2):

            ok = 1
            for x in left[i]:
                if a[x]^f == na[x]^j:
                    continue
                ok = 0
            if ok == 0:
                continue
            
            now = []
            for x in ncand:
                if a[x]^f == na[x]^j:
                    continue
                now.append(x)

            ni = f*2 + j
            if ndp[ni] > dp[i]+j:
                ndp[ni] = dp[i]+j
                nleft[ni] = now

    dp = ndp
    left = nleft
ans = inf
for i in range(4):
    if dp[i] != inf and len(left[i]) == 0:
        ans = min(ans,dp[i])
if ans == inf:
    ans = -1
print(ans)