t = int(input())
for _ in range(t):
    r,b,d = map(int,input().split())
    if r < b:
        r,b = b,r
    rn,rm = divmod(r,b)
    if rm:
        rn += 1
    if rn - 1 > d:
        print("No")
    else:
        print("Yes")