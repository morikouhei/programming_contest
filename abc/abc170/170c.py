x,n = map(int,input().split())
l = list(map(int,input().split()))
ans = 10**10
if n == 0:
    print(x)
    exit()
for i in range(-100,1000):
    if i in l:
        continue
    if ans > abs(i-x):
        ans1 = i
        ans = abs(i-x)
print(ans1)
    