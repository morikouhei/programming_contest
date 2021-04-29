n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
count = 0
for a,b in zip(A,B):
    count += abs(a-b)
if count <= k and (k-count)%2 == 0:
    print("Yes")
else:
    print("No")
