n,k = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
nums = [0]*(n+5)
for a in A:
    if a <= n:
        nums[a] = 1

for i in range(n+1):
    if nums[i] == 0:
        print(i)
        exit()

    k -= 1
    
    if k < 0:
        print(i)
        exit()