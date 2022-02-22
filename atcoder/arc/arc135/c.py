n = int(input())
A = list(map(int,input().split()))
ans = sum(A)

bcount = [0]*30
for a in A:
    for i in range(30):
        if a >> i & 1:
            bcount[i] += 1


for a in A:
    count = 0
    for i,b in enumerate(bcount):
        if a >> i & 1:
            count += (1<<i)*(n-b)
        else:
            count += (1<<i)*b
    ans = max(ans,count)
print(ans)