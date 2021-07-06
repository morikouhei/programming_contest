from collections import Counter
import random
import time
start = time.time()
n,m = map(int,input().split())
L = "ABCDEFGH."
S = [input() for i in range(m)]

ans = [["."]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        x = random.randint(0,7)
        ans[i][j] = L[x]
def check():
    use = [[0]*n for i in range(n)]
    done = [0]*m
    for i in range(n):
        for j in range(n):
            for x in range(m):
                if done[x]:
                    continue
                s = S[x]
                if ans[i][j] != s[0]:
                    continue
                l = len(s)
                ok = 1
                for k in range(l):
                    if ans[i][(j+k)%n] != s[k]:
                        ok = 0
                        break
                if ok:
                    done[x] = 1
                    for k in range(l):
                        use[i][(j+k)%n] += 1
                
                ok = 1
                for k in range(l):
                    if ans[(i+k)%n][j] != s[k]:
                        ok = 0
                        break
                if ok:
                    done[x] = 1
                    for k in range(l):
                        use[(i+k)%n][j] += 1
    return use,done

def clear(use):
    for i in range(n):
        for j in range(n):
            if use[i][j]:
                continue
            ans[i][j] = "."

bestuse,bestdone = check()
bestans = [ans[i][:] for i in range(n)]
best = sum(bestdone)
count = 0
while time.time() - start < 2.5:
    for i in range(n):
        for j in range(n):
            if bestuse[i][j] <= 1:
                x = random.randint(0,7)
                ans[i][j] = L[x]
    use,done = check()
    nbest = sum(done)
    if best < nbest:
        best = nbest
        bestans = [ans[i][:] for i in range(n)]
        bestuse = [use[i][:] for i in range(n)]
        bestdone = done[:]
    count +=1 
    if count%10:
        print(best)

for x in range(m):
    if bestdone[x]:
        continue
    s = S[x]
    for i in range(n):
        for j in range(n):
            l = len(s)
            ok = 1
            for k in range(l):
                if bestans[i][(j+k)%n] != s[k] and bestuse[i][(j+k)%n]:
                    ok = 0
                    break
            if ok:
                bestdone[x] = 1
                for k in range(l):
                    bestuse[i][(j+k)%n] += 1
                    bestans[i][(j+k)%n] = s[k]
                break
            ok = 1
            for k in range(l):
                if bestans[(i+k)%n][j] != s[k] and bestuse[(i+k)%n][j]:
                    ok = 0
                    break
            if ok:
                done[x] = 1
                for k in range(l):
                    bestuse[(i+k)%n][j] += 1
                    bestans[(i+k)%n][j] = s[k]
                break
    
if best == m:
    clear(bestuse)
                
for i in bestans:
    print(*i,sep="")