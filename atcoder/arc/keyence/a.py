n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
na = 0
nb = 0
ans = 0
for i,j in zip(a,b):
    ans = max(ans,i*j,na*j)
    print(ans)
    na = max(na,i)
