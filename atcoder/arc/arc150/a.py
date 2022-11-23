def solve():
    n,k = map(int,input().split())
    S = list(input())
    
    cum0 = [0]
    cum1 = [0]
    for s in S:
        if s == "1":
            cum1.append(cum1[-1]+1)
        else:
            cum1.append(cum1[-1])

        if s == "0":
            cum0.append(cum0[-1]+1)
        else:
            cum0.append(cum0[-1])

    num = 0
    for i in range(n-k+1):
        if cum1[i+k]-cum1[i] == cum1[-1] and cum0[i+k] - cum0[i] == 0:
            num += 1
    
    return "Yes" if num == 1 else "No"
t = int(input())
for _ in range(t):
    print(solve())