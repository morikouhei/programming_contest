n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = sum(a)
even = sorted([b[i]-a[i] for i in range(0,n,2)],reverse=True)
odd = sorted([b[i]-a[i] for i in range(1,n,2)],reverse=True)
for i,j in zip(even,odd):
    if i + j > 0:
        ans += i+j
    
print(ans)