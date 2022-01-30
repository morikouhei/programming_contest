n = int(input())
A = list(map(int,input().split()))

C = [0]*(n+1)
for a in A:
    C[a] += 1

for i in range(1,n+1):
    if C[i] != 4:
        print(i)
        exit()