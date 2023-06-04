n = int(input())
A = list(map(int,input().split()))
A.sort()

low = A[:n//2+1]
high = A[n//2+1:]

ans = [0]*n
for x,l in enumerate(low):
    ans[2*x] = l

for x,h in enumerate(high):
    ans[2*x+1] = h

for i in range(1,n,2):
    if ans[i] > ans[i-1] and ans[i] > ans[i+1]:
        continue
    print("No")
    exit()
print("Yes")