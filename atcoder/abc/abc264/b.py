r,c = map(int,input().split())

dr = min(r,16-r)
dc = min(c,16-c)
d = min(dr,dc)
if d%2:
    print("black")
else:
    print("white")