n,T = input().split()
n = int(n)
lt = len(T)
prefix = [0]*(lt+1)
saffix = [0]*(lt+1)

for i in range(n):
    S = input()

    now = 0
    count = 0

    for s in S:
        if now < lt and s == T[now]:
            now += 1

    prefix[now] += 1

    now = lt-1

    for s in S[::-1]:
        if now >= 0 and s == T[now]:
            now -= 1

    saffix[lt-1-now] += 1
ans = 0

cum = 0
for i in range(lt+1):
    cum += saffix[lt-i]
    ans += prefix[i]*cum
print(ans)