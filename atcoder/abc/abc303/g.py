from collections import deque

n,a,b,c,d = map(int,input().split())
X = list(map(int,input().split()))

cumX = [0]
for x in X:
    cumX.append(cumX[-1]+x)
dp = [[0]*(n+1) for j in range(n+1)]

for w in range(1,n+1):

    for l in range(n-w+1):
        base = cumX[l+w]-cumX[l]
        dp[l][l+w] = 2*base - min(dp[l][l+w-1],dp[l+1][l+w])

    for cost,area in [[a,b],[c,d]]:
        sliding_window = deque()
        id = 0

        for l in range(n-w+1):
            r = l+w

            base = cumX[r]-cumX[l]

            if w-area <= 0:
                dp[l][r] = max(dp[l][r],2*base-cost)
                continue

            if sliding_window and sliding_window[0][1] < l:
                sliding_window.popleft()
            
            sw = w-area
            lim = min(n,l+area+1)

            while id < lim:
                num = dp[id][id+sw]
                while sliding_window and sliding_window[-1][0] >= num:
                    sliding_window.pop()
                
                sliding_window.append([num,id])
                id += 1

            score = 2*base - sliding_window[0][0] - cost
            dp[l][r] = max(dp[l][r],score)
print(dp[0][n] - cumX[-1])