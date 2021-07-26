n,x = map(int,input().split())
A = list(map(int,input().split()))
need = sum(A)-n//2
if x >= need:
    print("Yes")
else:
    print("No")