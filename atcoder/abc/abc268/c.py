n = int(input())
P = list(map(int,input().split()))

l = [0]*n
id = [0]*n
for i,p in enumerate(P):
    id[p] = i

for i in range(n):
    l[(id[i]+n-i)%n] += 1

ans = 0

for i in range(n):
    c = 0
    for j in range(-1,2):
        c += l[(i+j)%n]
    ans = max(ans,c)
print(ans)