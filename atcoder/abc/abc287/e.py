n = int(input())
S = [[input(),i] for i in range(n)]
S.sort()

ans = [0]*n

def calc(S1,S2):
    l = min(len(S1),len(S2))
    for i,(s1,s2) in enumerate(zip(S1,S2)):
        if s1 != s2:
            return i
    return l
for (s1,i1),(s2,i2) in zip(S,S[1:]):
    num = calc(s1,s2)
    ans[i1] = max(ans[i1],num)
    ans[i2] = max(ans[i2],num)

for i in ans:
    print(i)