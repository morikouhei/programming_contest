
def solve():
    n,k = map(int,input().split())
    P = list(map(int,input().split()))
    P.sort()
    cand = [0,0,]
    cand.append(P[0]-1)
    cand.append(k-P[-1])
    for a,b in zip(P,P[1:]):
        c1 = (b-a)//2
        center = (a+b)//2
        for j in range(center-2,center+3):
            if j <= a or j >= b:
                continue
            cal = (j-a-1)//2+(b-j-1)//2+1
            c1 = max(c1,cal)
        cand.append(c1)
    cand.sort()
    count = cand[-1]+cand[-2]
    for a,b in zip(P,P[1:]):
        count = max(count,b-a-1)
    return count/k
T = int(input())
for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1,ans))