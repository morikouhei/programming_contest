from heapq import heappop,heappush
n = int(input())
q = int(input())

boxs = [[] for i in range(n+1)]
cards = [[] for i in range(2*10**5+5)]
Q = [list(map(int,input().split())) for i in range(q)]
for l in Q:

    if l[0] == 1:
        i,j = l[1:]

        heappush(boxs[j],i)
        heappush(cards[i],j)

    elif l[0] == 2:
        i = l[1]
        ans = [x for x in boxs[i]]
        print(*sorted(ans))
    
    else:
        i = l[1]
        ans = []
        last = -1
        cards[i].sort()
        for x in cards[i]:
            if x == last:
                continue
            ans.append(x)
            last = x
        print(*ans)