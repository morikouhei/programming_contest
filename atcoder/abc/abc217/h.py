from heapq import heappop as pop,heappush as push
n = int(input())
ql,qr,l,r,t,ans = [0]*n,[0]*n,0,0,0,0
for _ in range(n):
    nt,d,x = map(int,input().split())
    l -= nt-t
    r += nt-t
    if d:
        ans += max(0,-ql[0]+l-x)
        push(ql,-x+l)
        push(qr, -pop(ql)+l-r)
    else:
        ans += max(0,x-(qr[0]+r))
        push(qr,x-r)
        push(ql, -pop(qr)-r+l)
    t = nt
print(ans)
