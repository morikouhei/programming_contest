t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    count = 0
    now = 0
    for i in range(2*n):
        if l[i]%2:
            if now == 0:
                now += i+1
            else:
                print(now,i+1)
                count += 1
                now = 0
        if count == n-1:
            break
    if count < n-1:
        now = 0
        for i in range(2*n):
            if l[i]%2==0:
                if now == 0:
                    now += i+1
                else:
                    print(now,i+1)
                    count += 1
                    now = 0
            if count == n-1:
                break
