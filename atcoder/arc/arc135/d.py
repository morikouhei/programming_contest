h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h)]

for i in range(h):
    for j in range(w):
        if (i+j)%2:
            A[i][j] *= -1

H = [sum(A[i]) for i in range(h)]
W = [0]*w
for i in range(h):
    for j in range(w):
        W[j] += A[i][j]

ans = [[0]*w for i in range(h)]

nw = 0
for i in range(h):
    if H[i] <= 0:
        continue
    while nw < w:
        if W[nw] <= 0:
            nw += 1
            continue
        m = min(H[i],W[nw])
        ans[i][nw] += m
        H[i] -= m
        W[nw] -= m
        if H[i] == 0:
            break
        nw += 1

nw = 0
for i in range(h):
    if H[i] >= 0:
        continue

    while nw < w:
        if W[nw] >= 0:
            nw += 1
            continue
        m = max(H[i],W[nw])
        ans[i][nw] += m
        H[i] -= m
        W[nw] -= m
        if H[i] == 0:
            break
        nw += 1


nh = 0
for i in range(h):
    if H[i] <= 0:
        continue
    while nh < h:
        if H[nh] >= 0:
            nh += 1
            continue
        m = min(H[i],-H[nh])
        ans[i][0] += m
        ans[nh][0] -= m
        H[i] -= m
        H[nh] += m
        if H[i] == 0:
            break

        nh += 1


nw = 0
for i in range(w):
    if W[i] <= 0:
        continue
    while nw < w:
        if W[nw] >= 0:
            nw += 1
            continue
        m = min(W[i],-W[nw])
        ans[0][i] += m
        ans[0][nw] -= m
        W[i] -= m
        W[nw] += m
        if W[i] == 0:
            break

        nw += 1
count = 0
for i in range(h):
    for j in range(w):
        count += abs(ans[i][j])
        if (i+j)%2:
            ans[i][j] *= -1
print(count)
for i in ans:
    print(*i)