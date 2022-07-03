import sys
n = int(input())

dis = [[-1]*(n+1) for i in range(n+1)]
cand_ans = 1000
adj = 1


for i in range(3,n+1):
    print("?",1,i)
    sys.stdout.flush()
    d1 = int(input())
    dis[1][i] = d1
    print("?",2,i)
    sys.stdout.flush()
    d2 = int(input())
    dis[2][i] = d2
    cand_ans = min(cand_ans,d1+d2)

    if abs(d1-d2) != 1:
        adj = 0
if adj:
    if n == 4:
        print("?",3,4)
        sys.stdout.flush()
        d1 = int(input())
        if d1 == 3:

            print("!",1)
        else:
            if dis[1][3]-dis[2][3] == dis[1][4]-dis[2][4]:
                print("!",1)
            else:
                print("!",3)
    else:
        print("!",1)
else:
    print("!",cand_ans)
sys.stdout.flush()