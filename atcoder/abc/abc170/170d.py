from collections import Counter
n = int(input())
l = list(map(int,input().split()))
c = Counter(l)

l.sort()
check = [-1]*(10**6+2)

ans = 0
for i in l:
    if check[i] == -1:
        if c[i] == 1:
            ans += 1
        for j in range(i,10**6+2,i):
            check[j] = i
print(ans)

