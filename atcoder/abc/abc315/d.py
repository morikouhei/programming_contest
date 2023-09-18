h,w = map(int,input().split())
C = []
for i in range(h):
    c = [ord(s)-ord("a") for s in input()]
    C.append(c)

H = [[0]*26 for i in range(h)]
W = [[0]*26 for i in range(w)]
for i in range(h):
    for c in C[i]:
        H[i][c] += 1

for i in range(w):
    for j in range(h):
        W[i][C[j][i]] += 1


delH = [0]*h
delW = [0]*w
sH = h
sW = w
while True:

    tH = []
    tW = []
    for i in range(h):
        if delH[i]:
            continue
        
        for j in range(26):
            if H[i][j] == sW and sW >= 2:
                tH.append([i,j])
    
    for i in range(w):
        if delW[i]:
            continue
        for j in range(26):
            if W[i][j] == sH and sH >= 2:
                tW.append([i,j])


    
    if tH == [] and tW == []:
        break

    for i,x in tH:
        delH[i] = 1
        H[i] = [0]
        sH -= 1
        for j in range(w):
            if delW[j]:
                continue
            
            W[j][x] -= 1
        
    for i,x in tW:
        delW[i] = 1
        W[i] = [0]
        sW -= 1
        for j in range(h):
            if delH[j]:
                continue
            
            H[j][x] -= 1


ans = 0
for i in H:
    ans += sum(i)
print(ans)
