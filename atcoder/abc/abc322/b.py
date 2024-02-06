n,m = map(int,input().split())
S = input()
T = input()
ans = 3
if T.startswith(S):
    ans -= 2
if T.endswith(S):
    ans -= 1
print(ans)