k = int(input())
if k % 2 == 0:
    print(-1)
    exit()

ten = 1
now = 0
for i in range(10**8):
    x = (ten*7)%k
    now = (now+x)%k
    if now == 0:
        print(i+1)
        exit()
    ten = ten*10%k
print(-1)