import random
import time
import math

stime = time.time()
n,k = map(int,input().split())
A = list(map(int,input().split()))
XY = [list(map(int,input().split())) for i in range(n)]
XY.sort()
k = 100
LMin = -10**4
RMax = 10**4
W = RMax-LMin

areas = [[0]*55 for i in range(55)]

def check(x,y,lx,ly,rx,ry):
    if x == lx or x == rx or y == ly or y == ry:
        return 0
    if lx < x < rx and ly < y < ry:
        return 1
    return -1


def out_ans(X,Y):
    # print(len(X),len(Y))
    print(len(X)+len(Y))
    for i in X:
        print(i,LMin,i,RMax)
    for i in Y:
        print(LMin,i,RMax,i)
    exit()


def calc_lane(lx,rx,Y):
    lY = len(Y)
    count_l = [0]*lY

    for x,y in XY:
        if x <= lx:
            continue
        if x >= rx:
            break

        for i in range(lY-1):
            ly,ry = Y[i],Y[i+1]
            if ly < y < ry:
                count_l[i] += 1

    return count_l

def check_score(count_all):
    nums = 0
    for x,(i,a) in enumerate(zip(count_all,A)):
        nums += min(i,a)
        # else:
            # nums += min(i,a)*x

    return nums

def climbing(ly):

    w = W//(ly+2)
    Y = [LMin]
    ll = LMin
    for i in range(ly):
        ll += w
        Y.append(ll)
    Y.append(RMax)
    dic = {}
    w = W//(32)
    X = [LMin]
    ll = LMin
    for i in range(30):
        
        X.append(random.randint(LMin,RMax))
    X.append(RMax)
    X.sort()
    count_all = [0]*10

    for i in range(len(X)-1):
        lx,rx = X[i],X[i+1]
        l = calc_lane(lx,rx,Y)
        for j in l:
            if 1 <= j <= 10:
                count_all[j-1] += 1
        dic[(lx,rx)] = l

    
    temp_score = check_score(count_all)
    temp_X = X

    last = 0
    upd = 0
    while last < 100 and time.time() - stime < 2.7:

        action = random.randint(0,1)
        if action == 0: ### delete
            del_ind = random.randint(1,len(X)-2)
            count_temp = count_all[:]
            lx,x,rx = X[del_ind-1],X[del_ind],X[del_ind+1]
            for j in dic[(lx,x)]:
                if 1 <= j <= 10:
                    count_temp[j-1] -= 1
            for j in dic[(x,rx)]:
                if 1 <= j <= 10:
                    count_temp[j-1] -= 1

            new_l = calc_lane(lx,rx,Y)
            for j in new_l:
                if 1 <= j <= 10:
                    count_temp[j-1] += 1
            new_score = check_score(count_temp)
            if new_score > temp_score:
                temp_score = new_score
                del dic[(lx,x)],dic[(x,rx)]
                dic[(lx,rx)] = new_l
                # print(X,del_ind,x)
                X.pop(del_ind)
                # print(X)
                temp_X = X[:]
                upd += 1
            else:
                last += 1

        else: ### add
            new_x = random.randint(LMin,RMax)
            ins_ind = -1
            for i in range(len(X)-1):
                if X[i] < new_x < X[i+1]:
                    ins_ind = i
            if ins_ind == -1:
                continue

            lx,rx = X[ins_ind],X[ins_ind+1]
            count_temp = count_all[:]
            for j in dic[(lx,rx)]:
                if 1 <= j <= 10:
                    count_temp[j-1] -= 1

            new_l1 = calc_lane(lx,new_x,Y)
            for j in new_l1:
                if 1 <= j <= 10:
                    count_temp[j-1] += 1

            new_l2 = calc_lane(new_x,rx,Y)
            for j in new_l2:
                if 1 <= j <= 10:
                    count_temp[j-1] += 1

            new_score = check_score(count_temp)
            if new_score > temp_score:
                temp_score = new_score
                del dic[(lx,rx)]
                dic[(lx,new_x)] = new_l1
                dic[(new_x,rx)] = new_l2
                X.insert(ins_ind+1,new_x)
                temp_X = X[:]
                upd += 1
            else:
                last += 1

    return temp_score,temp_X,Y


def sa(ly):
    START_TEMP = 2000
    END_TEMP = 100
    END_TIME = 2.7
    w = W//(ly+2)
    Y = [LMin]
    ll = LMin
    for i in range(ly):
        ll += w
        Y.append(ll)
    Y.append(RMax)
    dic = {}
    w = W//(32)
    X = [LMin]
    ll = LMin
    for i in range(30):
        
        X.append(random.randint(LMin,RMax))
    X.append(RMax)
    X.sort()
    count_all = [0]*10

    for i in range(len(X)-1):
        lx,rx = X[i],X[i+1]
        l = calc_lane(lx,rx,Y)
        for j in l:
            if 1 <= j <= 10:
                count_all[j-1] += 1
        dic[(lx,rx)] = l

    
    temp_score = check_score(count_all)
    temp_X = X
    best_X = X[:]
    last = 0
    upd = 0
    while time.time() - stime < 2.7:

        pratio = time.time()/END_TIME
        temp = START_TEMP + (END_TEMP-START_TEMP) * pratio

        action = random.randint(0,1)
        if action == 0: ### delete
            if len(X) < 20:
                continue
            del_ind = random.randint(1,len(X)-2)
            count_temp = count_all[:]
            lx,x,rx = X[del_ind-1],X[del_ind],X[del_ind+1]
            for j in dic[(lx,x)]:
                if 1 <= j <= 10:
                    count_temp[j-1] -= 1
            for j in dic[(x,rx)]:
                if 1 <= j <= 10:
                    count_temp[j-1] -= 1

            new_l = calc_lane(lx,rx,Y)
            for j in new_l:
                if 1 <= j <= 10:
                    count_temp[j-1] += 1
            new_score = check_score(count_temp)
            delta = (new_score-temp_score)*10000
            probability = math.exp(delta/temp)
            
            if probability > random.random():
                temp_score = new_score
                del dic[(lx,x)],dic[(x,rx)]
                dic[(lx,rx)] = new_l
                # print(X,del_ind,x)
                X.pop(del_ind)
                # print(X)
                temp_X = X[:]
                upd += 1
                count_all = count_temp
                # print(delta,temp,probability)
                
            else:
                
                last += 1

        else: ### add
            if len(X) >= 50:
                continue
            new_x = random.randint(LMin,RMax)
            ins_ind = -1
            for i in range(len(X)-1):
                if X[i] < new_x < X[i+1]:
                    ins_ind = i
            if ins_ind == -1:
                continue

            lx,rx = X[ins_ind],X[ins_ind+1]
            count_temp = count_all[:]
            for j in dic[(lx,rx)]:
                if 1 <= j <= 10:
                    count_temp[j-1] -= 1

            new_l1 = calc_lane(lx,new_x,Y)
            for j in new_l1:
                if 1 <= j <= 10:
                    count_temp[j-1] += 1

            new_l2 = calc_lane(new_x,rx,Y)
            for j in new_l2:
                if 1 <= j <= 10:
                    count_temp[j-1] += 1

            new_score = check_score(count_temp)
            delta = (new_score-temp_score)*10000
            probability = math.exp(delta/temp)
            
            if probability > random.random():
                temp_score = new_score
                del dic[(lx,rx)]
                dic[(lx,new_x)] = new_l1
                dic[(new_x,rx)] = new_l2
                X.insert(ins_ind+1,new_x)
                temp_X = X[:]
                upd += 1
                count_all = count_temp
                # print(delta,temp,probability)
            else:
                last += 1
        # print(X)
    return temp_score,temp_X,Y


temp_score,temp_X,temp_Y = sa(45)
# while time.time() - stime < 2.7:
#     new_score,new_X,new_Y = climbing(random.randint(40,50))
#     if temp_score < new_score:
#         temp_score = new_score
#         temp_X = new_X
#         temp_Y = new_Y
print(int(temp_score/sum(A)*10**6))
out_ans(temp_X[1:-1],temp_Y[1:-1])