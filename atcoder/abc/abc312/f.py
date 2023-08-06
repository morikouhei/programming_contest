n,m = map(int,input().split())

T0 = []
T1 = []
T2 = [0]*(m+1)
for i in range(n):
    t,x = map(int,input().split())
    if t == 0:
        T0.append(x)
    elif t == 1:
        T1.append(x)
    else:
        T2.append(x)

T0.sort(reverse=True)
T1.sort(reverse=True)
T2.sort(reverse=True)

ans = 0

ind2 = 0
ind1 = 0
ind0 = 0

score = 0
left = 0
while True:

    left += T2[ind2]
    ind2 += 1

    while ind1 < len(T1) and ind1+ind2 < m and left:
        score += T1[ind1]
        ind1 += 1
        left -= 1
    
    if ind2+ind1 >= m:
        break

ans = score
for ind0,t0 in enumerate(T0,1):
    if ind0 > m:
        break

    if ind2 and left - T2[ind2-1] >= 0:
        ind2 -= 1
        left -= T2[ind2]
    elif ind1:
        ind1 -= 1
        score -= T1[ind1]
        left += 1
    score += t0
    ans = max(ans,score)
print(ans)

