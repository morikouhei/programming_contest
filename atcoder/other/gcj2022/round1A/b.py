import sys
def solve():
    n = int(input())
    lis = []
    for i in range(30):
        if 1<<i <= 10**9:
            lis.append(1<<i)
        if len(lis) == n:
            break

    for i in range(10**9,10**8,-1):
        if len(lis) == n:
            break
        if i in lis:
            continue
        lis.append(i)

    print(*lis)
    sys.stdout.flush()
    lis2 = list(map(int,input().split()))

    s = sum(lis) + sum(lis2)
    all = sorted(lis+lis2)
    target = s//2
    ans = []
    for l in all[::-1]:
        if target >= l:
            ans.append(l)
            target -= l

    print(*ans)
    sys.stdout.flush()
    
t = int(input())
for i in range(t):
    ans = solve()
    # print("Case #{}:".format(i+1),end=" ")
    # print(ans)