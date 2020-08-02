t = int(input())
l = [6,10,14,15,21]
for _ in range(t):
    n = int(input())
    if n >= 31:
        
        x = n-6-10-14
        if x  not in [6,10,14]:
            print("YES")
            print(6,10,14,x)
        else:
            if x == 6:
                x = n-10-6-15
                if x > 0:
                    print("YES")
                    print(10,6,15,x)
                else:
                    print("NO")
            elif x == 10:
                x = n-6-10-15
                
                if x > 0:
                    print("YES")
                    print(6,10,15,x)
                else:
                    print("NO")
            elif x == 14:
                x = n-10-6-15
                if x > 0:
                    print("YES")
                    print(10,6,15,x)
                else:
                    print("NO")

    else:
        print("NO")