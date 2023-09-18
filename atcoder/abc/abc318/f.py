n = int(input())
X = list(map(int,input().split()))
L = list(map(int,input().split()))

event = set()

for x in X:
    for l in L:
        event.add(x-l)
        event.add(x+l)

event = sorted(event)

ans = 0

inf = 10**20
event.append(inf)
last = -inf

def check(e):
    sX = [abs(x-e) for x in X]
    sX.sort()
    for x,l in zip(sX,L):
        if x > l:
            return 0

    return 1
# print(event)
for e,ne in zip(event,event[1:]):


    
    c = check(e)
    # print(e,ne,c,last)
    if c == 0:
        last = -inf
        continue

    if last != -inf:
        ans += e-last
    last = e
    # ans += 1
    nc = check(e+1)
    if nc:
        ans += 1
        last += 1
    else:
        last = -inf
        ans += 1
    # print(nc,ans,last)
print(ans)