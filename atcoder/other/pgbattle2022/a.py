n = int(input())
B = list(map(int,input().split()))
B.sort()
dif = B[-1]-B[0]

p = dif//n

ans = [B[0]]
for b,nb in zip(B,B[1:]):
    if b+p != nb:
        print(b+p)
        exit()