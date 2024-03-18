import random
import copy
n = 10

A_base = []
for i in range(n):
    A_base.append([])
    for j in range(n):
        A_base[i].append(i*n+j)


leng = 100

is_swap_list = [random.randint(0,1) for i in range(leng)]

pos_list = []
while len(pos_list) < leng:
    x1 = random.randint(0,n-1)
    y1 = random.randint(0,n-1)
    x2 = random.randint(0,n-1)
    y2 = random.randint(0,n-1)
    if (x1 == x2 and y1 == y2):
        continue

    pos_list.append([x1,y1,x2,y2])


def make(turn):
    new_list = copy.deepcopy(A_base)

    for i in range(turn):
        if is_swap_list[i] == 0:
            continue

        x1,y1,x2,y2 = pos_list[i]

        
        new_list[x1][y1],new_list[x2][y2] = new_list[x2][y2],new_list[x1][y1]

    return new_list


base_list = make(leng)

while True:

    pos = random.randint(0,leng-1)


    process_list = make(pos)

    print(pos,is_swap_list[pos])

    x1,y1,x2,y2 = pos_list[pos]

    assert [x1,y1] != [x2,y2]

    new_list = []
    for i in range(n):
        for j in range(n):
            if base_list[i][j] in [process_list[x1][y1],process_list[x2][y2]]:
                new_list.append(i)
                new_list.append(j)


    assert len(new_list) == 4

    nx1,ny1,nx2,ny2 = new_list


    base_list[nx1][ny1],base_list[nx2][ny2] = base_list[nx2][ny2],base_list[nx1][ny1]
    
    is_swap_list[pos]^= 1

    new_list = make(leng)

    for i in base_list:
        print(*i)

    for ni in new_list:
        print(*ni)

    print()
    assert new_list == base_list
