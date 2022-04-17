n = int(input())
A = list(map(int,input().split()))

sA = sorted(A)
lim = sA[n//2]

l = [1 if a <= lim else -1 for a in A]
for i in range(len(l)-1):
    l[i+1] += l[i]
ma = 10**10
mind = -1
for i in range(n):
    if l[i] < ma:
        ma = l[i]
        mind = (i+1)%n
print(mind,sum(sorted(A)[n//2:]))