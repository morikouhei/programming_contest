t = int(input())
for _ in range(t):
    n = int(input())
    
    ans = 0
    two = 1
    for i in range(63):
        ans += (n)//two
        two *= 2
    print(ans)