n = int(input())
S = [list(input()) for i in range(n)]
T = [list(input()) for i in range(n)]
ok = 0
for i in range(n):
    for j in range(n):
        if S[i][j] == "#":
            sx,sy = i,j
            ok = 1
            break
    if ok:
        break
def rotate(L):
    return [list(reversed(a)) for a in zip(*L)]

def check(sx,sy,tx,ty):
    for i in range(n):
        for j in range(-n,n):
            ssx = sx+i
            ssy = sy+j
            ttx = tx+i
            tty = ty+j
            if 0 <= ssx < n and 0 <= ssy < n:
                if S[ssx][ssy] == "#":
                    if 0 <= ttx < n and 0 <= tty < n and T[ttx][tty] == "#":
                        continue
                    return 0
                else:
                    if 0 <= ttx < n and 0 <= tty < n and T[ttx][tty] == "#":
                        return 0
            else:
                if 0 <= ttx < n and 0 <= tty < n and T[ttx][tty] == "#":
                    return 0
    return 1
for _ in range(4):
    ok = 0
    for i in range(n):
        for j in range(n):
            if T[i][j] == "#":
                tx,ty = i,j
                ok = 1
                break
        if ok:
            break
    if check(sx,sy,tx,ty):
        print("Yes")
        exit()
    T = rotate(T)

print("No")