n,x = map(int,input().split())
for i in range(26):
    if x <= n:
        print(chr(ord("A")+i))
        exit()
    x -= n