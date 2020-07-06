W,H,x,y = map(int,input().split())

if x*2 == W and y*2 == H:
    print(W*H/2,1)
else:
    a = min(x*H,(W-x)*H)
    b = min(y*W,(H-y)*W)
    print(max(a,b),0)
