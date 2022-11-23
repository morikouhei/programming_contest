import bisect
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

AB = [[a,b] for a,b in zip(A,B)]

ans = 0

for i in range(2):

    AB.sort(key=lambda x:x[i])

    lis = [-1]
    for j in range(n):
        a = AB[j][i^1]
        ind = bisect.bisect_left(lis,a)
        if ind == len(lis):
            lis.append(a)
        else:
            lis[ind] = a

    ans = max(ans,n+len(lis)-1)
print(ans)