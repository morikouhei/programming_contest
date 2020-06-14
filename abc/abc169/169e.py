n = int(input())
la = []
lb = []
for i in range(n):
    a,b = map(int,input().split())
    la.append(a)
    lb.append(b)
la.sort()
lb.sort()

if n % 2 != 0:
    left = la[n//2]
    right = lb[n//2]
    print(right-left+1)
else:
    left = (la[n//2]+la[n//2-1])/2
    right = (lb[n//2]+lb[n//2-1])/2
    print(int(right-left)*2+1)