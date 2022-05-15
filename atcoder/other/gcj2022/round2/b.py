import math
from decimal import Decimal, ROUND_HALF_DOWN

def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p

def solve():
    R = int(input())
    g = [[0]*(2*R+1) for i in range(2*R+1)]

    def draw_circle_perimeter(R):
        for x in range(-R,R+1):
            y = math.sqrt(R*R-x*x)
            y = my_round(y)
            # y = Decimal(y)
            # y = y.quantize(Decimal('0'), rounding=ROUND_HALF_DOWN)
            y = int(y)  # round to nearest integer, breaking ties towards zero
            g[x][y] = 1
            g[x][-y] = 1
            g[y][x] = 1
            g[-y][x] = 1


    for r in range(R+1):
        draw_circle_perimeter(r)

    g2 = [[0]*(2*R+1) for i in range(2*R+1)]
    for x in range(-R,R+1):
        for y in range(-R,R+1):
            r = math.sqrt(x**2+y**2)
            r = my_round(r)
            # r = Decimal(r)
            # r = r.quantize(Decimal('0'), rounding=ROUND_HALF_DOWN)
            if r <= R:
                g2[x][y] = 1


    ans = 0
    for i in range(2*R+1):
        for j in range(2*R+1):

            if g[i][j] != g2[i][j]:
                ans += 1
    return ans
t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1),end=" ")
    print(ans)