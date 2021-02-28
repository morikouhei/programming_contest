k = int(input())
S = list(input())[:4]
T = list(input())[:4]
cs = [0]*10
ct = [0]*10
for s,t in zip(S,T):
    cs[int(s)] += 1
    ct[int(t)] += 1

ans = 0
for i in range(1,10):
    for j in range(1,10):
        ns = cs
        nt = ct
        ns[i] += 1
        nt[j] += 1
        count = [0]*10
        for q in range(10):
            count[q] = ns[q]+nt[q]
        if max(count) > k:
            continue
        ss = 0
        st = 0
        for q in range(10):
            ss += q*(10**ns[q])
            st += q*(10**nt[q])
        if ss > st:
            if i != j:
                ans += (k-count[i]+1)*(k-count[j]+1)
            else:
                ans += (k-count[i]+2)*(k-count[j]+1)

base = (9*k-8)*(9*k-9)
ans /= base
print(ans)