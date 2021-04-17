t = int(input())
for _ in range(t):
    n = int(input())
    two = 0
    while n%2 == 0:
        two += 1
        n //= 2
    if two == 1:
        print("Same")
    elif two==0:
        print("Odd")
    else:
        print("Even")
