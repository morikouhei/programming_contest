n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

l = []
for i in range(n):
    a,b = A[i],B[i]
    if a <= b:
        l.append(i)
    else:
        while l and A[l[-1]] >= a-b:
            l.pop()

ans = len(l)
r = 0
le = len(l)

for i in range(n):
    while r < le and l[r] <= i:
        r += 1
    if A[i] <= B[i]:
        base = B[i]-A[i]+1
        if base < le-r:
            base += le-r-base
        ans = min(ans,base)
print(ans)