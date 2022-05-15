n = int(input())
T = list(map(int,input().split()))

def check(x,y):
    for i in range(70)[::-1]:
        if x[i] and y[i] == 0:
            return 1
        if x[i] == 0 and y[i]:
            return 0
    return 0
ans = [0]*70
for t in T:
    nans = [0]*70
    nans[t] = 1
    if check(nans,ans):
        ans = nans
        continue

    for i in range(t+1,70):
        nans[i] = ans[i]

    if check(nans,ans):
        ans = nans
        continue
    find = 0
    for i in range(t+1,70):
        if nans[i]:
            nans[i] = 0
        else:
            nans[i] = 1
            break
    ans = nans

count = 0
for i in ans[::-1]:
    count *= 2
    count += i
print(count)
        
