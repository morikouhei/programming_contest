n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

AB = []
for i,a in enumerate(A):
    AB.append([a,i,0])
for i,b in enumerate(B):
    AB.append([b,i,1])

AB.sort()

ansA = [0]*n
ansB = [0]*m

for x,(_,ind,t) in enumerate(AB):
    if t == 0:
        ansA[ind] = x+1
    else:
        ansB[ind] = x+1

print(*ansA)
print(*ansB)