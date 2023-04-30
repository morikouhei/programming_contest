def solve():
    n = int(input())
    S = list(map(int,input()))
    if sum(S)%2:
        return -1

    if sum(S) != 2:
        return sum(S)//2

    for i in range(n-1):
        s,ns = S[i],S[i+1]
        if s == ns == 1:
            if i > 1 or n-1-(i+1) >= 2:
                return 2
            if n == 4 and i == 1:
                return 3
            else:
                return -1
    
    return 1

t = int(input())
for _ in range(t):
    print(solve())