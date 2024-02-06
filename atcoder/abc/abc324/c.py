def check(s,t):

    if len(s) != len(t)-1:
        return 0

    now = 0
    add = 0
    for i in s:
        while now < len(t) and t[now] != i:
            now += 1
            add += 1
        now += 1
    
    return 1 if add <= 1 else 0


def check2(s,t):
    if len(s) != len(t):
        return 0

    dif = 0
    for i,j in zip(s,t):
        if i != j:
            dif += 1
    
    return 1 if dif <= 1 else 0
n,s = input().split()
n = int(n)
ans = []

for i in range(n):
    t = input()

    c = check(s,t) + check(t,s) + check2(s,t)
    if c:
        ans.append(i+1)

print(len(ans))
print(*ans)