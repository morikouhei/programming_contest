import sys
sys.setrecursionlimit(2*10**5)

n = int(input())
l = [int(i) for i in input().split()]
check = [0]*(2*10**5)
for i in l:
    check[i] = 1

ans = []
c = False
for i in range(n):
    if check[i] == 0:
        now = i
        c = True
        break
if not c:
    now = max(l)+1
M = now
b = l[0]
for i in range(n):
    if b == l[i]:
        while now < n+2 and check[now]:
            now += 1    
        ans.append(now)
        check[now] = 1
        M = max(M,now)
    else:
        if now < b and check[b-1]:
            if b-1 == now:
                M = max(M,b)
                now = b
        ans.append(b)
        b = l[i]
        
    if M < l[i]-1:
        print(-1)
        exit()
    
print(*ans)


