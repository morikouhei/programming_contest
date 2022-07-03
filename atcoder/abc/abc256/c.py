L = list(map(int,input().split()))
H = L[:3]
W = L[3:]
if sum(H) != sum(W):
    print(0)
    exit()
ans = 0

     
for a11 in range(1,29):
    for a12 in range(1,29):
        for a21 in range(1,29):
            for a22 in range(1,29):
                x1 = H[0]-a11-a12
                x2 = H[1]-a21-a22
                
                y1 = W[0]-a11-a21
                y2 = W[1]-a12-a22

                x3 = H[2]-y1-y2
                y3 = W[2]-x1-x2

                if x1 > 0 and x2 > 0 and x3 > 0 and y1 > 0 and y2 > 0 and y3 > 0 :
                    ans += 1
print(ans)