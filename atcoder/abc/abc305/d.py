n = int(input())
A = list(map(int,input().split()))
q = int(input())
LR = [list(map(int,input().split())) for i in range(q)]

event = []
for i,a in enumerate(A[1:]):
    event.append([a,0,0])

ans = [0]*q
for i,(l,r) in enumerate(LR):
    event.append([l,-1,i])
    event.append([r,1,i])

event.sort()

times = 0
num = 0
last = 0
for e,f,ind in event:
    if f == 0:
        num += 1
        if num%2 == 0:
            times += e-last
        else:
            last = e
    
        continue

    time = times

    if num%2:
        time += e-last
    
    ans[ind] += f*time

for i in ans:
    print(i)