n,m = map(int,input().split())
S = input()


l = -1
r = n+1
def solve(c):

    n1,n2 = m,c

    for s in S:
        if s == "0":
            n1,n2 = m,c
            continue
        if s == "2":
            n2 -= 1
            if n2 < 0:
                return False
            continue

        if s == "1":
            if n1:
                n1 -= 1
                continue
            if n2:
                n2 -= 1
                continue
            return False

    return True

while r > l + 1:
    c = (r+l)//2
    if solve(c):
        r = c
    else:
        l = c

print(r)
            