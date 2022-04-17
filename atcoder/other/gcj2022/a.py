def solve():
    r,c = map(int,input().split())
    ans = []
    ans.append(".."+"+-"*(c-1)+"+")
    ans.append("."+".|"*(c))
    for i in range(r):
        ans.append("+-"*c+"+")
        if i != r-1:
            ans.append("|."*c+"|")
    return ans


t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1))
    for i in ans:
        print(i)