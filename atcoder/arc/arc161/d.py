n,d = map(int,input().split())

if n*(n-1)//2 < n*d:
    print("No")
    exit()

nums = [0]*n

print("Yes")

for i in range(n):
    for j in range(1,d+1):
        print(i+1,(i+j)%n+1)