import random
import time

start = time.time()

n = 1000
size = 30
ABCD = [list(map(int,input().split())) for i in range(n)]

cx,cy = 400,400

ans = [[] for i in range(size)]
root = [[] for i in range(size)]
done1 = [[0]*n for i in range(size)]
done2 = [[0]*n for i in range(size)]
score = []

x,y = 400,400

center = [0]*n
count = 0
for i, (a,b,c,d) in enumerate(ABCD):

    if 300 <= c <= 500 and 300 <= d <= 500:
        center[i] = 1   
        count += 1

if count < 100:
    for i, (a,b,c,d) in enumerate(ABCD):
        if center[i]:
            continue
        if 200 <= c <= 600 and 200 <= d <= 600:
            center[i] = 1   
            count += 1

minid = []
for i,(a,b,c,d) in enumerate(ABCD):
    if center[i] == 0:
        continue
    dx = abs(cx-a)
    dy = abs(cy-b)
    minid.append([dx+dy,i])
minid.sort()
for id in range(size):

    x,y = cx,cy
    root[id].append([cx,cy])

    fid = minid[id][1]

    ans[id].append(fid+1)
    a,b,c,d = ABCD[fid]
    done1[id][fid] = 1
    root[id].append([a,b])
    x,y = a,b

    for food in range(49):

        cand = 10**10
        fid = -1
        for i,(a,b,c,d) in enumerate(ABCD):
            if done1[id][i] or center[i] == 0:
                continue

            dx = abs(x-a)
            dy = abs(y-b)
            if dx+dy < cand:
                cand = dx+dy
                fid = i

        ans[id].append(fid+1)

        a,b,c,d = ABCD[fid]
        done1[id][fid] = 1
        root[id].append([a,b])

        x,y = a,b

    for food in range(50):
        
        cand = 10**10
        fid = -1
        for i,(a,b,c,d) in enumerate(ABCD):
            if done1[id][i] == 0 or done2[id][i]:
                continue
            dx = abs(x-c)
            dy = abs(y-d)
            if dx+dy < cand:
                cand = dx+dy
                fid = i
        a,b,c,d = ABCD[fid]

        done2[id][fid] = 1
        root[id].append([c,d])

        x,y = a,b
    root[id].append([400,400])


    nowscore = 0
    for (x,y), (nx,ny) in zip(root[id],root[id][1:]):
        nowscore += abs(x-nx)+abs(y-ny)
    score.append(nowscore)
    
count = 0

upd = 0
while time.time() - start <= 1.8:
    if time.time() - start > 1.0 and upd == 0:
        upd = 1
        size //= 6
        scores = [[s,i] for i,s in enumerate(score)]
        scores.sort()
        nans = []
        nroot = []
        ndone1 = []
        ndone2 = []
        nscore = []
        for i in range(size):
            s,i = scores[i]
            nscore.append(s)
            nans.append(ans[i])
            nroot.append(root[i])
            ndone1.append(done1[i])
            ndone2.append(done2[i])
        
        ans = nans
        root = nroot
        done1 = ndone1
        done2 = ndone2
        score = nscore
        

    id = count%size

    if (count//size) % 2:

        c1id = random.randint(1,50)
        c2id = random.randint(1,50)


    else:

        c1id = random.randint(51,100)
        c2id = random.randint(51,100)

    count += 1
    if abs(c1id - c2id) <= 1:
        continue

    bx1,by1 = root[id][c1id-1]
    ax1,ay1 = root[id][c1id+1]

    bx2,by2 = root[id][c2id-1]
    ax2,ay2 = root[id][c2id+1]

    c1x,c1y = root[id][c1id]
    c2x,c2y = root[id][c2id]
    
    bcost = abs(bx1-c1x)+abs(c1x-ax1) + abs(by1-c1y)+abs(c1y-ay1) + abs(bx2-c2x)+abs(c2x-ax2) + abs(by2-c2y)+abs(c2y-ay2)

    ncost = abs(bx2-c1x)+abs(c1x-ax2) + abs(by2-c1y)+abs(c1y-ay2) + abs(bx1-c2x)+abs(c2x-ax1) + abs(by1-c2y)+abs(c2y-ay1)
    
    if bcost >= ncost:
        root[id][c1id],root[id][c2id] = root[id][c2id],root[id][c1id]
        score[id] -= bcost-ncost


id = score.index(min(score))
ans = []
for i in range(n):
    if done1[id][i]:
        ans.append(i+1)
print(50,*ans)
print(len(root[id]),end=" ")
for x,y in root[id]:
    print(x,y,end=" ")

