import bisect
def solve():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    p2 = [0]
    p1 = []
    for a,b in zip(A,B):
        if b == 2:
            p2.append(a)
        else:
            p1.append(a)
    p2.sort(reverse=True)
    p1.sort(reverse=True)
    cum = [0]
    for p in p1:
        cum.append(cum[-1]+p)

    ans = 10**20
    cost = 0
    for i,p in enumerate(p2):
        ind = bisect.bisect_left(cum,m-cost)
        if ind < len(cum):
            ans = min(ans,i*2+ind)
        cost += p
    if ans == 10**20:
        return -1
    return ans



t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)