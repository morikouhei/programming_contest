n = int(input())
S = [[int(x) for x in input()] for i in range(n)]
ans = 10**10

for i in range(10):
    cand = [0]*2000
    for j in range(n):
        ind = S[j].index(i)
        cand[ind] += 1
    
    last = 0
    for j in range(2000):
        if cand[j]:
            last = j
        if cand[j] > 1:
            cand[j+10] += cand[j]-1
    ans = min(ans,last)
print(ans)