n = int(input())
R = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = []
q = int(input())
for _ in range(q):
    r,c = map(int,input().split())
    r,c = R[r-1],C[c-1]
    if c >= -r+n+1:
        ans.append("#")
    else:
        ans.append(".")
print("".join(ans))