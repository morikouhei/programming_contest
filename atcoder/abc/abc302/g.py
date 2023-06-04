from itertools import permutations

n = int(input())
A = [int(x)-1 for x in input().split()]
nums = [0]*4
for a in A:
    nums[a] += 1


L = [0]*4
R = [0]*4
now = 0
for i in range(4):
    L[i] = now
    now += nums[i]
    R[i] = now

pos = [[0]*4 for i in range(4)]

for i,a in enumerate(A):
    for j,(l,r) in enumerate(zip(L,R)):
        if l <= i < r:
            pos[a][j] += 1


ans = 0
for i in range(4):
    pos[i][i] = 0


for i in range(4):
    for j in range(i):
        mi = min(pos[i][j],pos[j][i])
        ans += mi
        pos[i][j] -= mi
        pos[j][i] -= mi

for l in permutations(range(4),3):

    l = list(l) + [l[0]]
    mi = n+1
    for i,j in zip(l,l[1:]):
        mi = min(mi,pos[i][j])
    
    ans += mi*2
    for i,j in zip(l,l[1:]):

        pos[i][j] -= mi

        # print(pos[i][j],pos[j][i],i,j)


num = 0
for p in pos:
    num += sum(p)

ans += num//4*3

print(ans)