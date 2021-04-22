a,b = map(int,input().split())
if a >= b:
    ans = [i for i in range(1,a+1)]
    for i in range(b-1):
        ans.append(-i-1)
    s = sum(ans)
    ans.append(-s)
else:
    ans = [-i for i in range(1,b+1)]
    for i in range(a-1):
        ans.append(i+1)
    s = sum(ans)
    ans.append(-s)
print(*ans)
