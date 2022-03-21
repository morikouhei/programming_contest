v,a,b,c = map(int,input().split())

for i in range(10**5*2):
    if i%3 == 0:
        if v < a:
            print("F")
            exit()
        v -= a
    if i%3 == 1:
        if v < b:
            print("M")
            exit()
        v -= b
    if i%3 == 2:
        if v < c:
            print("T")
            exit()
        v -= c