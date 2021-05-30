
def solve():
    a,b,k = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    counta = [[] for i in range(a+1)]
    countb = [[] for i in range(b+1)]
    for a,b in zip(A,B):
        counta[a].append(b)
        countb[b].append(a)
    ans = 0
    for a,b in zip(A,B):
        ans += k-1-len(counta[a])-len(countb[b])+2
    return ans//2


t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)