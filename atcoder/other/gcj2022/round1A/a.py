def solve():
    S = input()
    ans = ""
    for s in S[::-1]:
        if ans == "":
            ans = s 
            continue

        cand1 = s+ans
        cand2 = s+s+ans
        if cand1 < cand2:
            ans = cand1
        else:
            ans = cand2
    return ans

t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1),end=" ")
    print(ans)