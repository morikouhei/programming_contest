def solve():
    n = input()
    ni = int(n)
    le = len(n)

    ans = int("9"*(le-1))
    for i in range(1,le):
        if le%i:
            continue

        top = n[:i]
        cand = str(int(top)-1)*(le//i)
        cand = int(cand)
        
        if ans < cand:
            ans = cand

        cand = top*(le//i)
        cand = int(cand)
        
        if ans < cand <= ni:
            ans = cand
        
    return ans


t = int(input())
for _ in range(t):
    print(solve())