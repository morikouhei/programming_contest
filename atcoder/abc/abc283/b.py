n = int(input())
A = list(map(int,input().split()))
q = int(input())
for _ in range(q):
    l = list(map(int,input().split()))
    if l[0] == 2:
        print(A[l[1]-1])
    
    else:
        _,k,x = l
        A[k-1] = x