n = int(input())
for x in [2,3]:
    while n%x == 0:
        n //= x

print("Yes" if n == 1 else "No")