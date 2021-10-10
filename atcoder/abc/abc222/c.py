n,m = map(int,input().split())
A = [list(input()) for i in range(2*n)]

wins = [[0,i] for i in range(2*n)]
for i in range(m):
    
    for j in range(n):
        x = wins[2*j][1]
        y = wins[2*j+1][1]
        nx = A[x][i]
        ny = A[y][i]
        if (nx == "G" and ny == "C") or (nx == "C" and ny == "P") or (nx == "P" and ny == "G"):
            wins[2*j][0] += 1
        elif (ny == "G" and nx == "C") or (ny == "C" and nx == "P") or (ny == "P" and nx == "G"):
            wins[2*j+1][0] += 1
    wins.sort(key=lambda x:(-x[0],x[1]))

for i in range(2*n):
    print(wins[i][1]+1)