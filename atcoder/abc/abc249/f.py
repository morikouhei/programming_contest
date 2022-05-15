from heapq import heappush,heappop
n,k = map(int,input().split())

Q = [[1,0]]+[list(map(int,input().split())) for i in range(n)]

ans = -10**20

h = []
left = k
add = 0
sub = 0
flag = 0
for t,y in Q[::-1]:
    if t == 2:
        if y >= 0:
            add += y

        else:
            if left:
                heappush(h,-y)
                left -= 1
            else:
                
                if h and h[0] < abs(y):
                    sub += heappop(h)
                    heappush(h,-y)
                else:
                    sub -= y
    else:
        if flag:
            if left:
                left -= 1
            elif h:
                sub += heappop(h)
            else:
                break

        ans = max(ans,y+add-sub)
        flag = 1


print(ans)