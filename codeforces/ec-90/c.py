t = int(input())
for _ in range(t):
    s = input()
    
    count = len(s)
    now = 0
    m = 0
    for i in range(len(s)):
        if s[i] == "-":
            now += 1
        else:
            now -= 1
        if m < now:
            count += (i+1)
            m = now
    print(count)
        