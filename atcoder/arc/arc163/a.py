def solve():
    n = int(input())
    S = input()
    s0 = S[0]

    for i in range(1,n):
        if S[i] > s0:
            return "Yes"
        
        if S[i] == s0:
            if S[:i] < S[i:]:
                return "Yes"
    return "No"

t = int(input())
for _ in range(t):
    print(solve())