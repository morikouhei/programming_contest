t = int(input())

for i in range(t):
    n,a,b = map(int,input().split())
    s =""
    j = 0
    k = 0
    while j < n:
        s += chr(ord("a")+j%b)
        j += 1
    print(s)
