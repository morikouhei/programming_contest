n,m,t = map(int,input().split())
A = list(map(int,input().split()))
bonus = [0]*(n+1)
for i in range(m):
    x,y = map(int,input().split())
    bonus[x] += y

for i,a in enumerate(A,1):
    if t <= a:
        print("No")
        exit()
    t -= a
    t += bonus[i+1]
print("Yes")