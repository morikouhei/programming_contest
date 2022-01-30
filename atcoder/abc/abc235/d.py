from heapq import heappop,heappush
a,n = map(int,input().split())

M = 10**6+1
inf = 10**10
dp = [inf]*M
dp[1] = 0

h = [[0,1]]

while h:
    d,now = heappop(h)
    if dp[now] != d:
        continue
 
    if now*a < M and dp[now*a] > d+1:
        dp[now*a] = d+1
        heappush(h,[d+1,now*a])

    if now%10 == 0 or now < 10:
        continue

    count = 0
    s = len(str(now))
    num = now
    for i in range(s):

        c = num%10
        if c == 0:
            break
        num //= 10
        num += c*10**(s-1)
        count += 1

        if num < M and dp[num] > d+count:
            dp[num] = d+count
        
            heappush(h,[d+count,num])

ans = dp[n]
if ans == inf:
    ans = -1
print(ans)



