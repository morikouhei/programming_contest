t = int(input())
a = list("atcoder")
for _ in range(t):
    s = list(input())
    ss = sorted(s,reverse=True)
    if a >= ss:
        print(-1)
        continue
    if a < s:
        print(0)
        continue
    x = 0
    for i in range(len(s)):
        if s[i] != "a":
            x = i
            break
    if s[x] > "t":
        print(x-1)
    else:
        print(x)