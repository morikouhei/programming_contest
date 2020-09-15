n = int(input())
X = []
Y = []
for i in range(n):
    x,y = map(int,input().split())
    X.append(x+y)
    Y.append(x-y)

print(max(max(X)-min(X),max(Y)-min(Y)))

