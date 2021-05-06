t = int(input())
for _ in range(t):
    n = int(input())
    B = list(map(int,input().split()))
    dic = {}
    for i,b in enumerate(B):
        if b in dic:
            dic[b].append(i)
        else:
            dic[b] = [i]
    s = sum(B)
    X = -1
    for b in B:
        if (s-b)%2 == 0 and (s-b)//2 in dic:
            if b == (s-b)//2:
                if len(dic[b]) == 1:
                    continue
                X = dic[b][0]
                Y = dic[b][1]
            else:
                X = dic[b][0]
                Y = dic[(s-b)//2][0]
            break

    if X == -1:
        print(-1)
        continue
    ans = []
    for i in range(n+2):
        if i == X or i == Y:
            continue
        ans.append(B[i])
    print(*ans)