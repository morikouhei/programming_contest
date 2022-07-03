n,l,r = map(int,input().split())

A = [i for i in range(n+1)]
ans = []


now = 0
last = 0
for i in range(1,n+1):
    nnow = n-i + now
    now = nnow
    if l <= nnow:
        
        s = nnow-l
        nnum = l
        for j in range(n-s,n+1):
            A[i],A[j] = A[j],A[i]

            nnum += 1
            if nnum > r:
                print(*A[1:])
                exit()
        for j in range(1,i+1):
            ans.append(A[j])
            A[j] = 0
        last = i

        break



last += 1
mi = 0
for i in range(last,n+1):

    nnow = n-i+now

    if nnow < r:
        ans.append(A.pop())
        mi += 1
        now = nnow
    else:
        num = r-now
        for j in range(num):
            A[last],A[last+1+j] = A[last+1+j],A[last]

        for j in A:
            if j > 0:
                ans.append(j)
        break
print(*ans)
