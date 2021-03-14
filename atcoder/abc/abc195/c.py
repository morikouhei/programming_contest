n = int(input())
ans = 0
for i in range(10):
    M = 10**((i+1)*3)-1
    if M < n:
        ans += (M+1 - (10**(i*3)))*i
    else:
        ans += (n+1 - (10**(i*3)))*i
        break
print(ans)