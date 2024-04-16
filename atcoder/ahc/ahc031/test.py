import subprocess
import time
import os
import random
import math
import matplotlib.pyplot as plt
import pandas as pd

# コードをコンパイルする(pythonなどの場合不要)

start = time.time()
N = int(input())
print("number test = ", N)

# パソコンのプロセス数
max_process = 5  # 要変更
proc_list = []
S_list = [str(i).zfill(4) for i in range(N)]

for i in range(N):
    # S = files[i]

    S = str(i).zfill(4)

    # proc = subprocess.Popen(f"cargo run -r --bin tester python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc029/a.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更

    command = f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc030/a.py < in/{S}.txt > out/{S}.txt"
    command = f"/Users/morikouhei/a.out < in/{S}.txt > out/{S}.txt 2> score/{S}.txt"

    proc = subprocess.Popen(
        command,
        shell=True,
    )  # 要変更

    proc_list.append(proc)
    if (i + 1) % max_process == 0 or (i + 1) == N:
        for subproc in proc_list:
            try:
                subproc.wait(timeout=100)
            except:
                print("stop")
        proc_list = []

print("time: ", time.time() - start)


freaqs = [0]*1000
E = [0]*100

plot_Y = []
def calc_score(input_path, output_path,score_path):

    with open(input_path) as f:
        lines = f.readlines()
        w,d,n = map(int,lines[0].replace("\n", "").split())
        w2 = w*w
        A = [
            list(map(int, lines[i].replace("\n", "").split()))
            for i in range(1,d+1)
        ]

        # turn = 0
        # day = 0
        # while day < d:
        #     turn += 1
        #     mas = A[day][:]
        #     nday = day+1
        #     while nday < d:
        #         for i,a in enumerate(A[nday]):
        #             mas[i] = max(mas[i],a)

        #         if sum(mas) > w2:
        #             break
        #         else:
        #             nday += 1
            
        #     day = nday

        # used = [[0]*n for i in range(d)]
        # sums = [sum(a) for a in A]
        # sA = []
        # for day in range(d):
        #     for i,a in enumerate(A[day]):
        #         sA.append([a,i,day])

        # sA.sort(reverse=True)

        # num = 0
        # use_a_list = [[] for i in range(d)]
        # mas = [0]
        # dist_min = 10**20
        # while True:
        #     min_dif = 10**20
        #     use_list = []

        #     for a,i,day in sA:
        #         if used[day][i]:
        #             continue

        #         ma = a
        #         use_cand = []
        #         min_cand = 10**20
        #         for di in range(d):
        #             for x in range(n)[::-1]:
        #                 if used[di][x]:
        #                     continue
        #                 if A[di][x] <= ma:
        #                     use_cand.append([A[di][x],x,di])
        #                     min_cand = min(min_cand,A[di][x])
        #                     break
                
        #         if len(use_cand) != d:
        #             break

        #         dif = ma - min_cand
        #         if dif < min_dif:
        #             min_dif = dif
        #             use_list = use_cand[:]

        #     if min_dif == 10**20:
        #         break
            
        #     for a,x,di in use_list:
        #         use_a_list[di].append(a)
        #         used[di][x] = 1
        #         sums[di] -= a

        #     lost = 0
        #     le = len(use_a_list[0])
        #     mas = [0]*le
        #     mis = [10**20]*le
        #     for i in range(d):
        #         use_a_list[i].sort()
        #         for j,a in enumerate(use_a_list[i]):
        #             mas[j] = max(mas[j],a)
        #             mis[j] = min(mis[j],a)

        #     for i in range(le):
        #         lost += mas[i]

        #     ok = 1
        #     dist_min = 10**20
        #     for i in range(d):
        #         if w*w-lost < sums[i]:
        #             ok = 0
        #         else:
        #             dist_min = min(dist_min,w*w-lost - sums[i])

        #     if ok:
        #         num += 1
        #     else:
        #         break
        
        # print("don't move num = ")
        # if num == 0:
        #     print(num,0)
        # else:
        #     cums = sum(mas)
        #     print(num,cums,cums/w/w,dist_min)


            


                





    #     w2 = w * w
    #     areas = []
    #     for a in A:
    #         areas.append(sum(a)*100//w2)
    #     print(areas,min(areas),max(areas))

    #     ma_each = [0]*n
    #     for a in A:
    #         for i,x in enumerate(a):
    #             ma_each[i] = max(ma_each[i],x)

    #     probs = [m*100/w2 for m in ma_each]
    #     accums = probs[:]
    #     for i in range(n-1)[::-1]:
    #         accums[i] += accums[i+1]
    #     plot_Y.append(accums[0])
    #     print(['{:.2f}'.format(n) for n in probs])
    #     print(['{:.2f}'.format(n) for n in accums])
            

    # return 
    pena_sum = 0
    with open(output_path) as f:
        lines = f.readlines()
        is_ok = 1

        for day in range(d):
            is_over = 0
            is_ok_turn = 1
            for i in range(n):
                lx,ly,rx,ry = map(int,lines[day*n+i].replace("\n","").split())
                area = (rx-lx) * (ry-ly)
                if area < A[day][i]:
                    is_ok_turn = 0
                    pena_sum += 100 * (A[day][i]-area)
                else:
                    is_over += area - A[day][i]
                
            if is_ok_turn == 0:
                # print(n,d,day,is_over)
                is_ok = 0
            



    #     score = int(lines[-1].replace("\n", "").split()[-1])
        
    #     t = float(lines[-2].replace("\n", "").split()[-1])
    #     # print(lines[-2].replace("\n",""))
    #     # print(lines[-1].replace("\n",""))

    with open(score_path) as f:
        lines = f.readlines()

        for line in lines:
            print(line.replace("\n",""))
        # print(lines[0].replace("\n",""))
        comp_num,comp_area,comp_rate = lines[0].replace("\n","").split()
        # line_num = int(lines[-2].replace("\n","").split()[-1])
        score = int(lines[-1].replace("\n", "").split()[-1])
        # print(f"d = {d} comp_d = {turn}")
        return score,d,n,0,0,is_ok,pena_sum,int(comp_num),comp_area,float(comp_rate)
        # print(lines[-2].replace("\n",""))
        # print(lines[-1].replace("\n",""))
    print()
    return score, N, M, eps, count,t,is_ok


sum_score = 0
prob_score = 0
sum_pena = 0
scores = []
errors = []
num = 400

out_num = num

comps_num = 0
comps_rate = 0
for i in range(num):
    S = str(i).zfill(4)
    input_path = f"in/{S}.txt"
    output_path = f"out/{S}.txt"
    score_path = f"score/{S}.txt"
    # score, N, M, eps = calc_score(input_path, output_path)

    print("S = ", S)
    # score,d,n,line_num,turn,is_ok,pena_sum = calc_score(input_path, output_path,score_path)
    
    # score,d,n,line_num,turn,is_ok,pena_sum,comp_num,comp_area,comp_rate = calc_score(input_path, output_path,score_path)

    try:
        score,d,n,line_num,turn,is_ok,pena_sum,comp_num,comp_area,comp_rate = calc_score(input_path, output_path,score_path)
        if comp_num:
            comps_num += 1
            comps_rate += comp_rate
        out_num -= is_ok

        prob_score += (score-pena_sum) * turn/d
        scores.append([score/d,score,S,d,n])
        sum_score += score
        sum_pena += score - pena_sum
        score = int((score-pena_sum) * turn / d)

    except:
        score = -1
        print("error", i)
        num -= 1

    # with open(score_path, "w") as f:
    #     f.write(str(score))


# for key in sorted(count_dic.keys()):
#     print(key,count_dic[key])
# # print(count_dic)

# exit()
# print(comps_num,comps_rate/comps_num)
print("average =", sum_score / num, sum_pena/num ,prob_score/num , prob_score,sum_score, num, prob_score / sum_score,out_num)
scores.sort()
print(scores[:20])
print(scores[-20:])

# print(len(plot_Y),num)
# fig = plt.figure()
# ax = fig.add_subplot(1, 2, 1)
# ax.scatter(range(num), plot_Y)

# # ax = fig.add_subplot(1, 2, 2)
# # ax.scatter(range(50,100), E[50:])

# plt.show()
