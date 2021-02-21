b,c = map(int,input().split())

if c == 1:
    print(1+int(b!=0))
    exit()

if b <= 0:
    maxp = -b+(c-1)//2
    maxm = max(0,-b-(c-1)//2)
else:
    maxp = b+(c-2)//2
    maxm = max(0,b-c//2)

ans = maxp-maxm+1

if b <= 0:
    maxm = b-c//2
    maxp = min(-1,b+(c-2)//2)
else:
    maxm = -b-(c-1)//2
    maxp = min(-1,-b+(c-1)//2)
ans += maxp-maxm+1
print(ans)