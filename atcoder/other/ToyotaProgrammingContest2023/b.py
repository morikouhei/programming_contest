from functools import cmp_to_key

def cmp(X,Y):
    si,pi,_ = X
    sj,pj,_ = Y

    if pi == 0:
        return 1
    if pj == 0:
        return -1

    return - si*(100-pj)/pj + sj*(100-pi)/pi


n = int(input())
SP = []
for i in range(n):
    s,p = map(int,input().split())
    SP.append([s,p,i])

SP = sorted(SP,key=cmp_to_key(cmp))

ans = [sp[2]+1 for sp in SP]
print(*ans)