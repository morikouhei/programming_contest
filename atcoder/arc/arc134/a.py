n,l,w = map(int,input().split())
A = list(map(int,input().split()))+[l]
ans = 0
r = 0
for a in A:
    if a > r:
        ans += (a-r+w-1)//w
    r = a+w

print(ans)