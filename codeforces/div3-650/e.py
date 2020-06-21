import math

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = list(input())
    l = [0]*26
    
    for i in s:
        l[ord(i)-ord("a")] += 1
    
    for i in range(n,0,-1):
        x = math.gcd(i,k)
        p = i//x
        count = 0
        for j in l:
            if j >= p:
                count += j//p*p
        if count >= i:
            print(i)
            break
    