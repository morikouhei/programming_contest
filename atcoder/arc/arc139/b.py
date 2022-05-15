def solve():
    n,a,b,x,y,z = map(int,input().split())

    lcm = a*b
    costs = [[lcm//di*i,i,di,j] for j,(i,di) in enumerate(zip([x,y,z],[1,a,b]))]
    cost = [lcm*x,lcm//a*y,lcm//b*z]
    
    if cost[0] == min(cost):
        return n*x

    costs.sort()
    if costs[1][3] == 0:
        i = costs[0][1]
        di = costs[0][2]
        return n//di*i + (n%di)*x

    ans = 10**30

    i = costs[0][1]
    di = costs[0][2]

    j = costs[1][1]
    dj = costs[1][2]
    num = n//di

    for k in range(num,max(-1,num-10**5),-1):
        rest = n-k*di
        if rest < 0:
            break

        count = k*i

        count += rest//dj*j
        count += (rest%dj)*x
        ans = min(ans,count)

    return ans


t = int(input())
for _ in range(t):
    print(solve())
        


    