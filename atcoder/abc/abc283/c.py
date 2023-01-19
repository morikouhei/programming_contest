S = list(map(int,input()))[::-1]
ans = 0
S += "#"

n = len(S)-1
now = 0
while now < n:
    ans += 1
    if S[now]:
        now += 1
    elif S[now+1] == 0:
        now += 2
    else:
        now += 1
print(ans)