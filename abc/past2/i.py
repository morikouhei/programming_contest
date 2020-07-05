n = int(input())
k = n
a = list(map(int,input().split()))
n = 2**n
seg = [-1]*(2*n)

def add(i,x):
    i += n-1
    seg[i] = x
    while i > 0:
        i = (i-1)//2
        seg[i] = max(seg[i*2+1],seg[i*2+2])

def cal(i,x):
    count = 1
    i += n-1
    while i > 0:
        i = (i-1)//2
        if seg[i] == x:
            count += 1
        else:
            break
    print(min(count,k))
for i in range(n):
    add(i,a[i])

for i in range(n):
    cal(i,a[i])
