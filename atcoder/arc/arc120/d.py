n = int(input())
A = list(map(int,input().split()))
sA = sorted([[a,i] for i,a in enumerate(A)])
col = [0]*(2*n)
for i in range(n):
    col[sA[i][1]] = 1

l = [[] for i in range(2)]
ans = ["("]*(2*n)
for i in range(2*n):
    x = col[i]
    if l[x^1]:
        l[x^1].pop()
        ans[i] = ")"
    else:
        l[x].append(i)
print(*ans,sep="") 