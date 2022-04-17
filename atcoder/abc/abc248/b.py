a,b,k = map(int,input().split())
for i in range(100):
    if a >= b:
        print(i)
        exit()
    a *= k
