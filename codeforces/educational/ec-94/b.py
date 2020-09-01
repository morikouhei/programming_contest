t = int(input())
for _ in range(t):
    p,f = map(int,input().split())
    cs,cw = map(int,input().split())
    s,w = map(int,input().split())
    ans = 0
    if w < s:
        s,w = w,s
        cs,cw = cw,cs
    
    for i in range(cs+1):
        count = min(i,p//s)
        np = p-count*s
        ns = cs-count
        count2 = min(cw,np//w)
        nw = cw-count2
        count3 = min(ns,f//s)
        nf = f-count3*s
        count += count2 + count3 + min(nw,nf//w)
        
        ans = max(ans,count)
    print(ans)