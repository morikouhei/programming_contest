from heapq import heappop, heappush
from collections import defaultdict
def solve():
    n = int(input())
    lis = [list(map(int,input().split())) for i in range(n)]
    dic = defaultdict(list)
    L = set([lis[i][0] for i in range(n)])
    L.add(-1)
    L.add(10**20)
    L = sorted(list(L))
    for l,r in lis:
        if l in dic:
            dic[l].append(r)
        else:
            dic[l] = [r]

    h = []
    for bl,l in zip(L,L[1:]):
        while bl < l and h:
            x = heappop(h)
            if x < bl:
                return "No"
            bl += 1
        for v in dic[l]:
            heappush(h,v)
        
    return "Yes"

t = int(input())
for _ in range(t):
    print(solve())