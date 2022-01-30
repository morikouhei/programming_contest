n = int(input())
A = list(map(int,input().split()))
fmin = min(A[:n])

cand = 10**10
for i in range(n):
    if A[i] == fmin:
        cand = min(cand,A[i+n])

if cand < fmin:
    print(fmin,cand)
    exit()

used = [0]*n

first = 10**10
second = 10**10
last = -1
if cand > fmin:
    for i in range(n):
        if A[i] == fmin:
            if first == 10**10:
                first = A[i+n]
            elif second == 10**10:
                second = A[i+n]
            used[i] = 1
            last = i

else:
    p = 1
    same = 0
    mins = 0
    lsame = -1

    for i in range(n):
        if A[i] == fmin:
            if A[i+n] == fmin:
                if p == 1:
                    used[i] = 1
                else:
                    same += 1
                    mins += 1
                    lsame = i
            else:
                p = 0
                mins += 1

    can1 = mins
    can2 = same*2
    for j in range(lsame+1,n):
        if A[i] == fmin:
            can2 += 1

    if can1 > can2:
        for i in range(n):
            if A[i] == fmin:
                if first == 10**10:
                    first = A[i+n]
                elif second == 10**10:
                    second = A[i+n]
                used[i] = 1
                last = i

    else:
        for i in range(n):
            if A[i] == fmin:
                if i > lsame or A[i+n] == fmin:
                    if first == 10**10:
                        first = A[i+n]
                    elif second == 10**10:
                        second = A[i+n]
                    used[i] = 1
                    last = i


l = []
for i in range(last+1,n):
    now = A[i]
    while l and l[-1][0] > now:
        l.pop()
    l.append([now,i])
sames = 1
for x,(num,ind) in enumerate(l):
    if num < first:
        used[ind] = 1
    elif num == first:
        if first < second:
            used[ind] = 1

        else:
            sames = 1
            for i in range(n):
                if used[i]:
                    if A[i+n] != first:
                        sames = 0
            
            if sames == 0:
                for t in range(x+1,len(l)):
                    num,ind = l[i]
                    if num < first:
                            used[ind] = 1
                    elif num == first:
                        if first <= second:
                            used[ind] = 1
                ans = []
                for i in range(n):
                    if used[i]:
                        ans.append(A[i])
                for i in range(n):
                    if used[i]:
                        ans.append(A[i+n])
                print(*ans)
                exit()

            mincand = 10**10
            for t in range(x+1,len(l)):
                num,ind = l[i]
                if num == first:
                    mincand = min(mincand,A[ind+n])

            if mincand < first:
                ans = []
                for i in range(n):
                    if used[i]:
                        ans.append(A[i])
                ans.append(first)
                for i in range(n):
                    if used[i]:
                        ans.append(A[i+n])
                ans.append(mincand)
                print(*ans)
                exit()
            elif mincand > first:
                for t in range(x+1,len(l)):
                    num,ind = l[i]
                    if num < first:
                            used[ind] = 1
                    elif num == first:
                        if first <= second:
                            used[ind] = 1
                ans = []
                for i in range(n):
                    if used[i]:
                        ans.append(A[i])
                for i in range(n):
                    if used[i]:
                        ans.append(A[i+n])
                print(*ans)
                exit()

            

ans = []
for i in range(n):
    if used[i]:
        ans.append(A[i])
for i in range(n):
    if used[i]:
        ans.append(A[i+n])
print(*ans)
exit()            

