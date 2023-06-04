def solve():
    d,k,x = map(int,input().split())

    ans = 10**20

    nums = [0]
    po = 1
    for i in range(d+3):
        nums.append(nums[-1]+po)
        po *= k

    for i in range(1,d+2):
        count = 0
        if i != d+1:
            count = 1
        now = nums[i]
        if now < x:
            continue
        for j in range(i)[::-1]:
            edge = nums[j]
            dif = now-x
            if dif and edge != 0:
                count += dif//edge
                now -= edge*(dif//edge)
        # assert now == x
        ans = min(ans,count)
    return ans

t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)