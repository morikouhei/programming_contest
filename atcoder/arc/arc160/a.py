n,k = map(int,input().split())
P = list(map(int,input().split()))
pos = [0]*n
for i,p in enumerate(P):
    pos[p-1] = i
used = [0]*n
l = 0
def nC2(n):
    return n*(n-1)//2
for _ in range(n):
    for i in range(n):
        if used[i]:
            continue

        p = pos[i]
        if p != l:
            if k > 1:
                k -= 1

            else:
                P[l:p+1] = P[l:p+1][::-1]
                print(*P)
                exit()
        
        else:
            num = l+1 + nC2(n-l)
            if num >= k:
                l += 1
                used[i] = 1
                break
            else:
                k -= num
    # k -= 1


print(*P)
