h1,w1 = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h1)]

h2,w2 = map(int,input().split())
B = [list(map(int,input().split())) for i in range(h2)]

for i in range(1<<h1):
    if bin(i).count("1") != h2:
        continue

    for j in range(1<<w1):
        if bin(j).count("1") != w2:
            continue

        temp = []
        for h in range(h1):
            if i >> h & 1:
                l = []
                for w in range(w1):
                    if j >> w & 1:
                        l.append(A[h][w])
                temp.append(l)

        if B == temp:
            print("Yes")
            exit()
print("No")