t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print("FastestFinger")
    elif n%2:
        print("Ashishgup")
    else:
        count = 0
        while n%2 == 0:
            count += 1
            n //= 2
        if n == 1:
            if count == 1:
                print("Ashishgup")
            else:
                print("FastestFinger")

        else:
            if count > 1:
                print("Ashishgup")
            else:
                count = 0
                for i in range(3,int(n**0.5)+1,2):
                    if n%i == 0:
                        while n%i == 0:
                            n //= i
                            count += 1
                if count > 1 or (count==1 and n > 1)  :
                    print("Ashishgup")
                else:
                    print("FastestFinger")
        
