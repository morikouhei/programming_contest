from collections import deque
Q = int(input())
mod = 998244353
tens = [1]*(Q+5)
for i in range(Q+4):
    tens[i+1] = tens[i]*10%mod

q = deque([1])
ans = 1
le = 1

for _ in range(Q):
    l = list(map(int,input().split()))
    if l[0] == 1:
        x = l[1]
        q.append(x)
        ans *= 10
        ans += x
        ans %= mod
        le += 1
    elif l[0] == 2:
        x = q.popleft()
        ans -= x * tens[le-1]
        ans %= mod
        le -= 1
    else:
        print(ans)
