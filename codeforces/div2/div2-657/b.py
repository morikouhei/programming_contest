t = int(input())
for _ in range(t):
    l,r,m = map(int,input().split())
    dif = r-l

    for i in range(l,r+1):
        t = m%i
        if t == 0:
            print(i,l,l)
    
            break
        else:
            if i - t <= dif:
                print(i,r-i+t,r)
                
                break
            else:
                if m > i and t <= dif:
                    print(i,r,r-t)
                    
                    break
    