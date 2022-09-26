E = [list(map(int,input().split())) for i in range(4)]

def f(ind):
    a,b = E[ind]
    c,d = E[(ind+1)%4]
    e,f = E[(ind+2)%4]

    dx1,dy1 = c-a,d-b
    dx2,dy2 = e-a,f-b
    if dx1*dy2-dx2*dy1 <= 0:
        print("No")
        exit()
    return 1

for i in range(4):
    f(i)
print("Yes")