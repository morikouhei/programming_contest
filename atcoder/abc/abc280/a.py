h,w = map(int,input().split())
ans = 0
for i in range(h):
    ans += input().count("#")
print(ans)