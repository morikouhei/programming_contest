t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = ""
    for i in range(n):
        ans += s[i*2]
    print(ans)