
turn = 0
def solve():
    n = int(input())
    P = list(map(int,input().split()))
    ans = []
    turn = 0
    if n == 2:
        if P[0] > P[1]:
            print(1)
            print(1)
        else:
            print(0)
        exit()
    def swap(x):
        P[x],P[x+1] = P[x+1],P[x]
        ans.append(x+1)

    for i in range(n,4,-1):
        for j in range(n):
            if P[j] == i:
                ind = j
        if ind+1 >= i:
            continue
        if turn%2 and ind%2 == 0:
            if ind != 2:
                swap(1)
            else:
                swap(3)
            turn += 1
        elif turn%2 == 0 and ind%2:
            if ind > 1:
                swap(0)
            else:
                swap(2)
            turn += 1
        for j in range(ind,i-1):
            swap(j)
            turn += 1
    if n >= 4:
        for j in range(4):
            if P[j] == 4:
                ind = j

        if ind == 0:
            if turn%2:
                swap(1)
                turn += 1
            for j in range(ind,3):
                swap(j)
            turn += 3
        if ind == 1:
            if turn%2 == 0:
                swap(2)
                turn += 1
            for j in range(ind,3):
                swap(j)
            turn += 2
        if ind == 2:
            if turn%2:
                swap(1)
                swap(2)
                swap(1)
                swap(2)
                turn += 4
            else:
                swap(2)
                turn += 1
    while True:
        if P[0]+2 == P[1]+1 == P[2]:
            break
        if turn%2:
            swap(1)
        else:
            swap(0)
        turn += 1


    print(turn)
    print(*ans)


t = int(input())
for _ in range(t):
    solve()