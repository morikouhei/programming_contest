n,m = map(int,input().split())
S = input()
T = input()

if T not in S:
    print("No")
    exit()

dpf = [0]*(n+1)
dpb = [0]*(n+1)

dpf[0] = 1

for i in range(n):
    if dpf[i] == 0 and dpb[i] == 0:
        continue

    if dpf[i]:
        ok = 1
        for j in range(m):
            if i+j < n and S[i+j] == T[j]:
                dpf[i+j+1] = 1
            else:
                ok = 0
                break

        if ok:
            dpf[i+m] = dpb[i+m] = 1

    
    if dpb[i]:
        for l in range(m):

            ok = 1
            for r in range(l,m):
                if i+r-l < n and S[i+r-l] == T[r]:
                    continue
                else:
                    ok = 0
            if ok:
                dpb[i+r-l+1] = 1

    
    if dpf[i] and dpb[i]:
        for l in range(m):
            ok = 1
            for r in range(l,m):
                if i+r-l < n and S[i+r-l] == T[r]:
                    dpf[i+r-l+1] = 1
                    # dpb[i+r-l+1] = 1
                else:
                    ok = 0
                    break


print("Yes" if dpb[-1] else "No")


    
