n = int(input())
a = list(map(int,input().split()))
if 0 in a:
    print(0)
    exit()
m = 10**18
ans = 1
for i in a:
    ans *= i
    if ans > m:
        print(-1)
        exit()
print(ans)