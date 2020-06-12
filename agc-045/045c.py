n = int(input())
check = True
if n == 1:
    print("Not Prime")
    exit()
for i in range(2,int(n**0.5)+1):
    if n%i == 0:
        check = False
        break
if check:
    print("Prime")

else:
    x = n%10
    if x%2 != 0 and x != 5:
        count = 0
        while n > 0:
            count += n%10
            n //= 10
        if count %3 !=0:
            print("Prime")
            exit()
    print("Not Prime")