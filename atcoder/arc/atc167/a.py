n,m = map(int,input().split())
A = sorted(list(map(int,input().split())))

ans = [0]*m
for i in range(n):    
    rest = m - i
    rA = n - i
    if rest * 2 == rA:
        pos = i
        break

    ans[i] = A[n-1-i]
    A.pop()

for i in range(len(A)//2):
    ans[pos+i] += A[i] + A[-1-i]
res = 0
for a in ans:
    res += a**2
print(res)
