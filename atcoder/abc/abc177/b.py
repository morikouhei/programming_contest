s = list(input())
t = list(input())
ans = float("INF")
for i in range(len(s)-len(t)+1):
    count = 0
    for j in range(len(t)):
        if s[i+j] == t[j]:
            continue
        count += 1
    ans = min(ans,count)
print(ans)