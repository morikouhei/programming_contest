h,w,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

if sum(A)%k != sum(B)%k:
    print(-1)
    exit()

base = h*w*(k-1)

ca = 0
cb = 0
for a in A:
    m = w*(k-1)
    ca += (k+m%k-a)%k
for b in B:
    m = h*(k-1)
    cb += (k+m%k-b)%k
print(base-max(ca,cb))