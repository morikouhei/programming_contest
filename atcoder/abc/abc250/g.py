L = list(map(int,input().split()))
V = L[:4]
n = L[-1]
water = [V[0]]+[0]*3
for i in range(n):
    nwater = [0]*n

    w1 = water[i%4]
    can = min(w1,V[(i+1)%4]-water[(i+1)%4])
    water[i%4] -= can
    water[(i+1)%4] += can
    print(water)