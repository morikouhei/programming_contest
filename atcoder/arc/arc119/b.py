n = int(input())
S = list(input())
T = list(input())
if S.count("1") != T.count("1"):
    print(-1)
    exit()

ans = 0
for i in range(2):
    now = 0
    for s,t in zip(S,T):
        if s == t == "1":
            continue
        if s == t == "0":
            if now > 0:
                ans += 1
        if s == "1" and t == "0":
            now += 1
        if s == "0" and t == "1":
            if now > 0:
                ans += 1
            now -= 1
    S = S[::-1]
    T = T[::-1]

print(ans)