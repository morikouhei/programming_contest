n = int(input())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

lY = [0]*n
ma = 10**10
for i,y in enumerate(Y):
    ma = min(ma,y)
    lY[i] += ma
ma = 10**10
for i in range(n)[::-1]:
    y = Y[i]
    ma = min(ma,y)
    lY[i] += ma

ok = 1
for ly,y in zip(lY,Y):
    if ly < y:
        ok = 0
if ok:
    print(-1)
