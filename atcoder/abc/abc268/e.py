n = int(input())
P = list(map(int,input().split()))
id = [0]*n
for i,p in enumerate(P):
    id[p] = i
l = [0]*n
for i in range(n):
    l[(id[i]+n-i)%n] += 1

plus = 0
minus = 0
for i in range(n):
    if n%2 and i == n//2:
        continue
    if i < (n+1)//2:
        plus += l[i]
    else:
        minus += l[i]

ans = 0
for i in range(n):
    c = (id[i]-i)%n
    ans += min(c,n-c)

base = ans
for i in range(1,n+1):
    ans = min(ans,base)

    base -= minus
    base += plus


    if n%2 == 0:
        pind = (n-i)+n//2
        plus -= l[pind%n]
        minus += l[pind%n]
    else:
        pind = (n-i)+n//2
        plus -= l[pind%n]
        minus += l[(pind+1)%n]


    mind = (n-i)%n
    minus -= l[mind]
    plus += l[mind]

print(ans)
