import math

n = int(input())
A = list(map(int,input().split()))
m = min(A)
dic = {}

for a in A:
    cand = set()
    for j in range(1,int(a**0.5)+1):
        if a%j == 0:
            cand.add(j)
            cand.add(a//j)
    for c in cand:
        if c in dic:
            dic[c] = math.gcd(dic[c],a)
        else:
            dic[c] = a
    
ans = 0
for i,j in dic.items():
    if i == j and i <= m:
        ans += 1
        print(i)
print(ans)
