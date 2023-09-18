n = int(input())
S = [[0]*101 for i in range(101)]
for i in range(n):
    a,b,c,d = map(int,input().split())

    for x in range(a,b):
        for y in range(c,d):
            S[x][y] = 1

ans = 0
for i in S:
    ans += sum(i)
print(ans)