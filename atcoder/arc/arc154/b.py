from collections import Counter
n = int(input())
S = input()
T = input()

if Counter(S) != Counter(T):
    print(-1)
    exit()


if S == T:
    print(0)
    exit()

def check(x):
    dic = {}
    for i in range(x):
        dic[S[i]] = dic.get(S[i],0)+1

    nS = x
    for t in T:
        if nS < n and t == S[nS]:
            nS += 1
        elif dic.get(t,0) > 0:
            dic[t] -= 1
        else:
            return False
    return True
l = 0
r = n
while r > l + 1:
    m = (r+l)//2
    if check(m):
        r = m
    else:
        l = m
print(r)