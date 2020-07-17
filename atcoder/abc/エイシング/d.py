n = int(input())
x = list(input())
c1 = x.count("1")+1
c2 = c1-2

now1 = 0
now2 = 0

for i in range(n):
    if x[-1-i] == "1":
        now1 += pow(2,i,c1)
        if c2 != 0:
            now2 += pow(2,i,c2)
        
    now1 %= c1
    if c2 != 0:
        now2 %= c2

for i in range(n):
    if x[i] == "1":
        if c2 == 0:
            print(0)
            continue
        now = (now2-pow(2,n-1-i,c2))%c2
        
        count = 1
        while now > 0:
            q = bin(now)
            y = q.count("1")
            now %= y
            count += 1
        print(count)
    else:
        
        now = (now1+pow(2,n-1-i,c1))%c1
        
        count = 1
        while now > 0:
            q = bin(now)
            y = q.count("1")
            now %= y
            count += 1
        print(count)
