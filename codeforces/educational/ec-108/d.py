n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cum = 0
for a,b in zip(A,B):
    cum += a*b
 
ans = cum
 
for i in range(n):
    count = cum
    for j in range(1,min(i,n-1-i)+1):
        count += (A[i-j]-A[i+j])*(B[i+j]-B[i-j])
        if ans < count:
            ans = count
 
for i in range(1,n):
    count = cum
    for j in range(1,min(i,n-i)+1):
        count += (A[i-j]-A[i+j-1])*(B[i+j-1]-B[i-j])
        if ans < count:
            ans = count
print(ans)