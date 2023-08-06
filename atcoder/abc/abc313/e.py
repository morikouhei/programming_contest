n = int(input())
S = list(map(int,input()))
mod = 998244353

for s,ns in zip(S,S[1:]):
    if s != 1 and ns != 1:
        print(-1)
        exit()


turn = 0

for s in S[1:][::-1]:
    turn += 1
    turn += (s-1)*turn
    turn %= mod
print(turn)