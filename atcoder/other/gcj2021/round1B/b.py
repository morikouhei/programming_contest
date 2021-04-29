
M = 1005

def solve():
    n,a,b = map(int,input().split())
    need = [0]+list(map(int,input().split()))
    
    def calc(x):
        count = [0]*(x+1)
        count[x] = 1
        for i in range(x+1)[::-1]:
       
            if i > n:
                if i - a > 0:
                    count[i-a] += count[i]
                if i - b > 0:
                    count[i-b] += count[i]
                count[i] = 0
            else:
                base = need[i]
                can = count[i]-base
                if can >= 0:
                    if i - a > 0:
                        count[i-a] += can
                    if i - b > 0:
                        count[i-b] += can
                    count[i] = base
                else:
                    return False

        return True

    for i in range(n,M):
        if calc(i):
            return i
    return "IMPOSSIBLE"


T = int(input())
for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1,ans))