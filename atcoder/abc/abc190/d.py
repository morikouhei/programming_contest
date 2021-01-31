n = int(input())
n *= 2
ans = 0
for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        x = i
        y = n//i
        if x%2 != y%2:
            ans += 2
print(ans)