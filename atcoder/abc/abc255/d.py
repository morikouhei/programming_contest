n,q = map(int,input().split())
A = sorted(list(map(int,input().split())))
X = []
for i in range(q):
    x = int(input())
    X.append([x,i])

ans = [0]*q
X.sort()

s = sum(A)
lsum = 0
now = 0
for x,ind in X:

    while now < n and A[now] < x:
        lsum += A[now]
        now += 1
    
    count = x*now - lsum
    count += (s-lsum) - x * (n-now)
    ans[ind] = count
for i in ans:
    print(i)