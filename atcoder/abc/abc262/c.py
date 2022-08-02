n = int(input())
A = list(map(int,input().split()))
ans = 0
num = 0
for i,a in enumerate(A,1):
    if a == i:
        ans += num
        num += 1
    else:
        if A[a-1] == i:
            ans += 1
print(ans)