n,l = map(int,input().split())
ans = 0
for a in list(map(int,input().split())):
    if a >= l:
        ans += 1
print(ans)