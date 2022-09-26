n,m = map(int,input().split())

sumA = 0

count = {}

for i in range(n):
    a,b = map(int,input().split())
    sumA += a
    count[b-a] = count.get(b-a,0)+1

inf = 10**10
dp = [inf]*(m+1)
dp[sumA] = 0

def get(x,dx):

    l = []

    two = 0
    while x >= 1<<two:   
        l.append([1<<two,dx*(1<<two)])
        x -= 1<<two
        two += 1

    if x:
        l.append([x,dx*x])

    return l

for dx,num in count.items():

    if dx == 0:
        continue

    l = get(num,dx)

    for cost,dis in l:

        if dx > 0:
            for i in range(m+1)[::-1]:
                if dp[i] == inf:
                    continue
                if i+dis <= m:
                    dp[i+dis] = min(dp[i+dis],dp[i]+cost)
                
        else:
            for i in range(m+1):
                if dp[i] == inf:
                    continue
                if 0 <= i+dis:
                    dp[i+dis] = min(dp[i+dis],dp[i]+cost)


for i in dp:
    if i == inf:
        print(-1)
    else:
        print(i)