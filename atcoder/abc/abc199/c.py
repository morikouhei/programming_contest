n = int(input())
S = list(input())
Q = int(input())
swap = 0
for i in range(Q):
    T = list(map(int,input().split()))
    if T[0] == 2:
        swap ^= 1

        continue
    t,a,b = T
    a -= 1
    b -= 1
    if swap == 0:
        S[a],S[b] = S[b],S[a]
    else:
        if a >= n:
            a -= n
        else:
            a += n
        if b >= n:
            b -= n
        else:
            b += n
        S[a],S[b] = S[b],S[a]

if swap:
    S = S[n:]+S[:n]
print(*S,sep="")

        