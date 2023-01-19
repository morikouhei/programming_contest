n,x = map(int,input().split())

def get(dir):
    cand = [x]
    used = set([x])
    now = 1

    def search(dir,target):
        while 0 < target <= n and target in used:
            target += dir
        if 0 < target <= n:
            return target
        else:
            return -1

    while True:
        if dir == 1:
            target = cand[-1]+now
        else:
            target = cand[-1]-now
        
        target = search(dir,target)
        if target > 0:
            used.add(target)
            cand.append(target)
            now += 1
            continue

        dir *= -1
        if dir == 1:
            target = cand[-1]+now
        else:
            target = cand[-1]-now
        
        target = search(dir,target)
        if target > 0:
            used.add(target)
            cand.append(target)
            now += 1
            continue
        break
    return cand


cand1 = get(1)
cand2 = get(-1)
if len(cand1) > len(cand2):
    cand = cand1
else:
    cand = cand2

used = set(cand)
for i in range(1,n+1):
    if i not in used:
        cand.append(i)
print(*cand)
         