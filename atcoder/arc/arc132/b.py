n = int(input())
P = list(map(int,input().split()))
ans = n+1

one = P.index(1)

if P[(one+1)%n] == 2:
    ans = n-one
else:
    ans = one+2
print(ans)