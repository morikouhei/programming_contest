n = int(input())
A = list(map(int,input().split()))
A.sort()
for i,a in enumerate(A,1):
    if i != a:
        print("No")
        exit()
print("Yes")