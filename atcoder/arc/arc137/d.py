n = int(input())
A = list(map(int,input().split()))
Q = int(input())
que = []

def calc(X,Y):
    ans = [0]*n
    for i,x in enumerate(X):
        ans[i] = Y[x]
    return ans


move = [i for i in range(n)]

for _ in range(Q):
    q = list(map(int,input().split()))

    if q[0] == 1:
        _,x,y = q
        x -= 1
        y -= 1
        que.append([x,y])
        move[x],move[y] = move[y],move[x]

    elif q[0] == 2:
        x,y = que.pop()
        move[x],move[y] = move[y],move[x]
    else:
        k = q[1]
        base = move[:]
        norm = [i for i in range(n)]
        while k:
            if k&1:
                norm = calc(norm,base)
            base = calc(base,base)
            k >>= 1
        A = [A[i] for i in norm]
print(*A)
