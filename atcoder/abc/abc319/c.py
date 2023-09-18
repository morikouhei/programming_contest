import itertools
C = [list(map(int,input().split())) for i in range(3)]

all_num = 0


bingo_lines = []
for i in range(3):
    bingo = []
    for j in range(3):
        bingo.append([i,j])
    bingo_lines.append(bingo)

for i in range(3):
    bingo = []
    for j in range(3):
        bingo.append([j,i])
    bingo_lines.append(bingo)

bingo = []
bingo2 = []
for i in range(3):
    bingo.append([i,i])
    bingo2.append([i,2-i])
bingo_lines.append(bingo)
bingo_lines.append(bingo2)

bingo_list = [[[] for i in range(3)] for j in range(3) ]
for i in range(3):
    for j in range(3):
        for bingo in bingo_lines:
            if [i,j] in bingo:
                bingo_list[i][j].append(bingo)

def check_bingo(seen,x,y):

    for bingo in bingo_list[x][y]:

        ok = 1
        for i,j in bingo:
            if seen[i][j] == 0:
                ok = 0
                continue
        
        if ok == 0:
            continue

        num = C[x][y]

        other = []

        for i,j in bingo:
            if (i,j) != (x,y):
                other.append(C[i][j])
        if other[0] == other[1] and other[0] != num:
            return 1 

    return 0


ans = 0
for p in itertools.permutations(range(9),9):
    all_num += 1

    seen = [[0]*3 for i in range(3)]
    count = 1
    for id in p:
        x,y = divmod(id,3)

        seen[x][y] = 1
        count -= check_bingo(seen,x,y)
        if count == 0:
            break
    ans += count

print(ans/all_num)

