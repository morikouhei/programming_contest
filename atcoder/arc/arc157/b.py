n,k = map(int,input().split())
S = input()

def solve(S,k):
    score = len(S)-1
    l = []

    num = 0
    n = len(S)
    if "Y" not in S:
        return score-k

    for i in range(n):
        if S[i] == "Y":
            num += i
            S = S[i:]
            break
    
    n = len(S)
    for i in range(n)[::-1]:
        if S[i] == "Y":
            num += n-1-i
            S = S[:i+1]
            break
    if num >= k:
        return score-k

    k -= num
    score -= num
    num = 0
    for s in S:
        if s == "Y":
            if num:
                l.append(num)
            num = 0
        
        else:
            num += 1
    l.sort(reverse=True)

    for x in l:
        if x < k:
            score -= x+1
            k -= x
        else:
            score -= k+1
            return score
    return score

if S.count("X") >= k:
    k = S.count("X") - k
    ans = solve(S,k)
else:
    k -= S.count("X")
    S = ["X" if s == "Y" else "Y" for s in S]
    ans = solve(S,k)

print(max(ans,0))