n = int(input())
X = [0]*n
Y = [0]*n
for i in range(n):
    X[i],Y[i] = map(int,input().split())
X.sort()
Y.sort()
cx,cy = X[n//2],Y[n//2]
ans = 0
for x,y in zip(X,Y):
    ans += abs(x-cx)+abs(y-cy)
print(ans)
