Q = int(input())
top = []
lt = 0
bottom = []
lb = 0
for _ in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        top.append(x)
        lt += 1
    elif t == 2:
        bottom.append(x)
        lb += 1
    else:
        if x <= lt:
            print(top[-x])
        else:
            print(bottom[x-lt-1])