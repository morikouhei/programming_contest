n = int(input())
S = list(map(int,input()))
T = list(map(int,input()))
num = 0

for s,t in zip(S,T):
    if s != t:
        num += 1

if num%2:
    print(-1)
    exit()

if sum(S) < sum(T):
    S,T = T,S

dif = sum(S)-sum(T)
dif //= 2
ans = [0]*n

now = 0
for i in range(n)[::-1]:
    if S[i] and T[i] == 0 and dif:
        ans[i] = 1
        dif -= 1
print(*ans,sep="")