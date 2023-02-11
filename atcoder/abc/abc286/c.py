n,a,b = map(int,input().split())
S = input()

ans = 10**20

for i in range(n):
    count = 0
    for j in range(n//2):
        if S[(j+i)%n] != S[(n-1-j+i)%n]:
            count += b
    count += i*a
    ans = min(ans,count)
print(ans)