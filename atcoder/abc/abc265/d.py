n,p,q,r = map(int,input().split())
A = list(map(int,input().split()))

cum = [0]
for a in A:
    cum.append(cum[-1]+a)
l = [0,0,0]
need = [p,q,r]
nums = [0,0,0]

for i in range(n):
    a = A[i]

    li = i
    ads = 0
    for j in range(3):
        r = max(li,l[j])
        l[j] = r
        nums[j] = cum[r]-cum[li]
        while l[j] < n and nums[j] < need[j]:
            nums[j] += A[l[j]]
            ads += A[l[j]]
            l[j] += 1
        li = l[j]


    if need == nums:
        print("Yes")
        exit()
    nums[0] -= a
print("No")
