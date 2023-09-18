n = int(input())
S = list(input())
q = int(input())
TXC = [input().split() for i in range(q)]

last = [-1]*n
for i,(t,x,c) in enumerate(TXC):
    if int(t) == 1:
        S[int(x)-1] = c
        last[int(x)-1] = i


for i in range(q)[::-1]:

    t,x,c = TXC[i]

    t = int(t)

    if t == 2:
        for j,s in enumerate(S):
            if last[j] < i:
                S[j] = s.lower()
        break

    if t == 3:
        for j,s in enumerate(S):
            if last[j] < i:
                S[j] = s.upper()
        break

print(*S,sep="")