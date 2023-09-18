n,m = map(int,input().split())
L = list(map(int,input().split()))

inf = 10**10
def search(width):

    lines = 1
    now = width
    for l in L:

        if l > width:
            return inf

        if now == width:
            if now >= l:
                now -= l
            else:
                lines += 1
                now = width-l
        else:
            if now >= l+1:
                now -= l+1
            else:
                lines += 1
                now = width-l
    return lines


l = max(L)-1
r = 10**15

while r-l > 1:
    c = (r+l)//2
    if search(c) > m:
        l = c
    else:
        r = c
print(r)
