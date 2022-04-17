import sys
sys.setrecursionlimit(10**7)

def dfs(x,l):
    global ns 
    if sum(l) == 0:
        ns.append(x)

    for i,nx in enumerate(l):
        if nx:
            xx = x + str(i)
            nl = l[:]
            nl[i] -= 1
            dfs(xx,nl)
    return 

def calc(x,y):

    same = 0
    for i,j in zip(x,y):
        if i == j:
            same += 1
        else:
            break
    
    count = len(x)-same + len(y) - same
    return count

def solve():
    global ns
    e,w = map(int,input().split())
    W = [list(map(int,input().split())) for i in range(e)]
    dp = {"":0}
    for i in range(e):
        ns = []
        dfs("",W[i])
        ndp = {}
        for k,v in dp.items():
            for s in ns:
                num = calc(k,s)
                if s in ndp:
                    ndp[s] = min(ndp[s],v+num)
                else:
                    ndp[s] = v+num
        dp = ndp
    ans = 10**10
    for k,v in dp.items():
        ans = min(ans,v+len(k))

    return ans


    
t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1),end=" ")
    print(ans)