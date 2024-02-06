import subprocess
import time
import os
import random
import math
import matplotlib.pyplot as plt
import pandas as pd
#コードをコンパイルする(pythonなどの場合不要)

start = time.time()
N = int(input())
print("number test = ",N)

#パソコンのプロセス数
max_process = 5 #要変更
proc_list = []
S_list = [str(i).zfill(4) for i in range(N)]

for i in range(N):
    # S = files[i]

    S = str(i).zfill(4)

    proc = subprocess.Popen(f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc028/a.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更
    proc_list.append(proc)
    if (i + 1) % max_process == 0 or (i + 1) == N:
        for subproc in proc_list:
            try:
                subproc.wait(timeout=10)
            except:
                print("stop")
        proc_list = []


print("time: ", time.time() - start)


def calc_score(input_path,output_path):
 
    with open(input_path) as f:
        lines = f.readlines()

        n,m = map(int,lines[0].replace("\n","").split())
        si,sj = map(int,lines[1].replace("\n","").split())

    x,y = si,sj
    score = 0
    with open(output_path) as f:
        lines = f.readlines()

        for l in lines:
            nx,ny = map(int,l.replace("\n","").split())
            score += abs(x-nx) + abs(y-ny) + 1
            x,y = nx,ny

    return max(10000-score,1001)
                

sum_score = 0
log_sum = 0
best_sum_score = 0
scores = []
errors = []
num = 400


plot_X = []
plot_Y = []
plot_X2 = []
for i in range(400):
    S = str(i).zfill(4)
    # print(S)
    input_path = f"in/{S}.txt"
    output_path = f"out/{S}.txt"
    score_path = f"score/{S}.txt"
    # calc_score(input_path,output_path)
    try:

        score = calc_score(input_path,output_path)
        scores.append([score,S])
        sum_score += score
    except:
        score = -1
        print("error",i)
        num -= 1

    with open(score_path,"w") as f:
        f.write(str(score))
        


# lis = []
# for key,value in count_dic.items():
#     lis.append([key,value])

# lis.sort(key=lambda x:x[1])

# for key,value in lis:
#     print(key,value)

print("average =", sum_score / num,sum_score,log_sum/num)
scores.sort()
print(scores[:20])
print(scores[-20:])

# fig = plt.figure()
# ax = fig.add_subplot(1,2,1)
# ax.scatter(plot_X,plot_Y)

# ax = fig.add_subplot(1,2,2)
# ax.scatter(plot_X2,plot_Y)

# plt.show()