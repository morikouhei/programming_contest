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

    # command = f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc030/a.py < in/{S}.txt > out/{S}.txt"
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
    with open(score_path) as f:
        lines = f.readlines()

        score = int(lines[-1].replace("\n", "").split()[-1])
        # print(f"d = {d} comp_d = {turn}")
        return score



sum_score = 0
prob_score = 0
sum_pena = 0
scores = []
errors = []
num = N

out_num = num

for i in range(num):
    S = str(i).zfill(4)
    input_path = f"in/{S}.txt"
    output_path = f"out/{S}.txt"
    score_path = f"score/{S}.txt"
    # score, N, M, eps = calc_score(input_path, output_path)

    # print("S = ", S)
    # score,d,n,line_num,turn,is_ok,pena_sum = calc_score(input_path, output_path,score_path)
    
    # score,d,n,line_num,turn,is_ok,pena_sum,comp_num,comp_area,comp_rate = calc_score(input_path, output_path,score_path)

    try:
        score = calc_score(input_path, output_path,score_path)

        scores.append([score,S])
        sum_score += score


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
print("average =", sum_score / num, num)
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
