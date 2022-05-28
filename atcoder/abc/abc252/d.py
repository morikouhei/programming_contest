n = int(input())
A = list(map(int,input().split()))
M = 2*10**5+5
num = [0]*M
for a in A:
    num[a] += 1


ans = n*(n-1)*(n-2)//6

for i,x in enumerate(num):
    if x <= 1:
        continue

    ans -= x*(x-1)//2*(n-x)
    ans -= x*(x-1)*(x-2)//6
print(ans)