n,l = map(int,input().split())
A = list(map(int,input().split()))
now = 0
finish = 0
for a in A:
    if finish:
        if a == 2:
            print("No")
            exit()
        continue

    if l-now >= a+1:
        now += a+1
    else:
        now += a
    print(a,now,finish)
    if now > l:
        print("No")
        exit()
    elif now == l:
        finish = 1
print("Yes")