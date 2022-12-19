import sys
M = 12
n = int(input())
areas = [[] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(M):
        r = i+(1<<j)-1
        r = min(r,n)
        areas[i].append([i,r])

print(n*M)
for i in range(1,n+1):
    for x,y in areas[i]:
        print(x,y)
sys.stdout.flush()

q = int(input())

def get_id(x,y):
    return (x-1)*M+y+1
for _ in range(q):
    l,r = map(int,input().split())

    if l == r:
        id = get_id(l,0)
        print(id,id)
        sys.stdout.flush()
        continue
    k = (r-l+1).bit_length()-1
    k2 = 1<<k
    # print(r-l+1,k,k2)
    print(get_id(l,k),get_id(r-k2+1,k))
    sys.stdout.flush()