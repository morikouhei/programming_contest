n = int(input())
XY = [list(map(int,input().split())) for i in range(n)]

def calc_area(a,b,c):
    x1,y1 = XY[a%n]
    x2,y2 = XY[b%n]
    x3,y3 = XY[c%n]

    area = (x1-x3)*(y2-y1) - (x1-x2)*(y3-y1)
    return abs(area)


base = 0
for i in range(2,n):
    base += calc_area(0,i-1,i)


def score(area):
    a1 = area*4
    a2 = (base-area)*4
    ans = min(abs(base-a1),abs(base-a2))
    return ans*8

ans = 10**20
now = 1
area = 0
for i in range(n):
 
    ans = min(ans,score(area))
    while area*4 <= base:
        area = area+calc_area(i,now,now+1)
        ans = min(ans,score(area))
        now += 1
        
    area -= calc_area(i,i+1,now)
        
print(ans//8)