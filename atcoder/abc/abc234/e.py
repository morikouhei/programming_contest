X = int(input())
l = len(str(X))
ans = 10**30

for i in range(l,l+10):
    for j in range(-8,10):
        
        for k in range(1,10):
            now = k
            cand = 0
            for t in range(i):
                cand *= 10
                cand += now
                now += j
       
                if t < i-1 and (now < 0 or now >= 10):
                    cand = 10**30
                    break

            if cand >= X:
                ans = min(ans,cand)
print(ans)
