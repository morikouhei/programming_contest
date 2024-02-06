n,k = map(int,input().split())

X = []
Y = []
for i in range(n):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
cX = [0]
cY = [0]
for x in X:
    cX.append(cX[-1]+x)
for y in Y:
    cY.append(cY[-1]+y)

def cost(m,X,cX):
    
    count = 10**20
    r = 0
    for i,x in enumerate(X):
        while r < n and X[r] <= x+m:
            r += 1
        
        num = x*i - cX[i] + cX[-1] - cX[r] - (n-r) * (x+m)
        count = min(count,num)


    l = n-1
    for i in range(n)[::-1]:
        x = X[i]
        while l >= 0 and X[l] >= x-m:
            l -= 1
        

        num = (x-m) * (l+1) - cX[l+1] + cX[-1] - cX[i] - x * (n-i)
        count = min(count,num)

    return count

def calc(m):

    num = cost(m,X,cX) + cost(m,Y,cY)
    return num <= k


l = -1

r = 10**9+5

while r > l + 1:

    m = (r+l)//2

    if calc(m):
        r = m
    else:
        l = m

print(r)