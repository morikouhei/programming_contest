t = int(input())
for _ in range(t):
    ans = []
    n = int(input())
    l = list(map(int,input().split()))
    count = [0]*(n+1)
    for i in l:
        if count[i] == 0:
            count[i] += 1
            ans.append(i)
    print(*ans)