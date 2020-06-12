t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    count = 0
    for i in range(n-1):
        a,b = map(int,input().split())
        if a == x or b == x:
            count += 1
    if count == 1or n%2 == 0:
        print("Ayush")
    else:
        print("Ashish")
        
