n,m = map(int,input().split())
S = list(map(int,input()))
T = list(map(int,input()))

k = int(input())
XY = [list(map(int,input().split())) for i in range(k)]


M = 5*10**5

facts = [0]*M
for i in range(1,M):
    now = i
    while now%2 == 0:
        facts[i] += 1
        now //= 2

for i in range(M-1):
    facts[i+1] += facts[i]


def nCr(n,r):
    if n < r:
        return 0

    num = facts[n]-facts[r]-facts[n-r]
    
    if num > 0:
        return 0
    else:
        return 1


for x,y in XY:
    x,y = x-1,y-1
    if x == 0:
        print(T[y])
        continue
    if y == 0:
        print(S[x])
        continue

    num = 0
    for i in range(1,x+1):
        if S[i] == 0:
            continue

        d = y-1 + (x-i)
        num += nCr(d,y-1)
        num %= 2

    for i in range(1,y+1):
        if T[i] == 0:
            continue

        d = x-1 + (y-i)
        num += nCr(d,x-1)
        num %= 2
    print(num)