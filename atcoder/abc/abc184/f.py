n,t = map(int,input().split())
a = list(map(int,input().split()))

l = [[0] for i in range(2)]
num = 0
for i in range(n):
    for j in range(len(l[num])-1,-1,-1):
        l[num].append(l[num][j]+a[i])
    num = (num+1)%2
A = sorted(l[0])
B = sorted(l[1])
r = len(B)-1
ans = 0
for i in range(len(A)):
    x = A[i]
    while r >= 0 and x + B[r] > t:
        r -= 1
    if r >= 0:
        ans = max(ans,x+B[r])
print(ans)