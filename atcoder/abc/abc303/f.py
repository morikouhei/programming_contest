from heapq import heappop,heappush
n,H = map(int,input().split())

TD = [list(map(int,input().split())) for i in range(n)]

ts = [t for t,d in TD] + [H+1]
ts = sorted(set(ts))
dic = {t:i for i,t in enumerate(ts)}


max_d = [0]*len(ts)
for t,d in TD:
    t = dic[t]
    max_d[t] = max(max_d[t],d)


day = 0

cons = 0

## cons t <= day damage is constant
## prop t > day damage is proportional of day

h = []
for t,d in TD:
    heappush(h,[-d,t])

prop_d,prop_t = heappop(h)
prop_d *= -1

def rsum(first,prop_d,num):

    return (first + first + (prop_d)*(num-1))*(num)//2


for t,nex_d in zip(ts,max_d):

    dif = t-day
    ## calc damage 

    prop_base = (day+1)*prop_d
    if prop_d:
        need = (cons-prop_base+prop_d-1)//prop_d
    else:
        need = dif

    need = min(max(need,0),dif)

    if need * cons >= H:
        ans = day + (H+cons-1)//cons
        print(ans)
        exit()
    else:
        H -= need * cons

    if dif-need:
        first = prop_base + prop_d * need
        damage = rsum(first,prop_d,dif-need)

        if damage >= H:

            l = 0
            r = dif-need+1
            while r > l + 1:
                m = (r+l)//2
                if rsum(first,prop_d,m) >= H:
                    r = m
                else:
                    l = m

            ans = day + r
            print(ans)
            exit()

        else:
            H -= damage

    day = t
    cons = max(cons,t*nex_d)
    
    if prop_t <= day:
        while h:
            prop_d,prop_t = heappop(h)
            prop_d *= -1

            if prop_t > day:
                break
        
        if prop_t <= day:
            prop_d = 0

    