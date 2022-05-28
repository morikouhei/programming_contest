n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
m = max(A)
for i,a in enumerate(A,1):
    if m != a:
        continue
    if i in B:
        print("Yes")
        exit()
 
print("No")