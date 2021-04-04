t = int(input())
for _ in range(t):
    x = int(input())
    ans = 0
    s = set()
    for i in range(1,10001):
        s.add(i**3)
    for i in range(1,10001):
        if x-i**3 in s:
            ans = 1
            break
    print("YES" if ans else "NO")
