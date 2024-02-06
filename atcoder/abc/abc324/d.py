n = int(input())
S = sorted(list(map(int,input())))

ans = 0
for i in range(4*10**6):

    t = list(map(int,str(i**2).zfill(n)))
    t.sort()

    if S == t:
        ans += 1
print(ans)