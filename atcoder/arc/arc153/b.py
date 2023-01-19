h,w = map(int,input().split())
A = [input() for i in range(h)]

q = int(input())

ph = 1
pw = 1
for i in range(q):
    a,b = map(int,input().split())

    if ph <= a:
        ph = a-ph+1
    else:
        ph = a+h-ph+1


    if pw <= b:
        pw = b-pw+1
    else:
        pw = b+w-pw+1

PH = [0]*h
PW = [0]*w
ph,pw = ph-1,pw-1
for i in range(h):
    if q%2:
        PH[i] = (ph-i)%h
    else:
        PH[i] = (i+ph)%h

for i in range(w):
    if q%2:
        PW[i] = (pw-i)%w
    else:
        PW[i] = (i+pw)%w

ans = [[0]*w for i in range(h)]

for i in range(h):
    for j in range(w):
        ans[PH[i]][PW[j]] = A[i][j]

for i in ans:
    print(*i,sep="")