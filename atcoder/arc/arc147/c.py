n = int(input())
LR = [list(map(int,input().split())) for i in range(n)]
M = max([max(x) for x in LR])+5


def calc(x):
    count = 0
    pos = []
    for l,r in LR:
        if l <= x <= r:
            pos.append(x)
        elif r < x:
            pos.append(r)
        else:
            pos.append(l)
    
    base = sum(pos)
    pos.sort()
    for i,p in enumerate(pos,1):
        base -= p
        count += base-(n-i)*p

    return count


ins = [0]*M
outs = [0]*M
for l,r in LR:
    ins[l] += 1
    outs[r] += 1

score = calc(0)

ans = score

now = 0
end = 0
for i in range(M):
    now += ins[i]
    now -= outs[i]
    end += outs[i]
    score += end*now
    score -= (n-end-now)*now
    ans = min(ans,score)

print(ans)