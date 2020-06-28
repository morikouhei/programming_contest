n = int(input())
count = [1]*(n+1)
ans = 1
for i in range(2,n+1):
    for j in range(i,n+1,i):
        count[j] += 1
    ans += i*count[i]
    
print(ans)