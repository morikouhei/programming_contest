n,k = map(int,input().split())
A = sorted(list(map(int,input().split())))


def search(x):
    num = 0
    count = 0
    for a in A:
        if a < x:
            num += a
        else:
            count += 1

    need = (k-count)*x
    return need <= num


l = 0
r = 10**18
while r > l+1:
    m = (r+l)//2
    if search(m):
        l = m
    else:
        r = m

print(l)