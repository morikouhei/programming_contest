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

    # proc = subprocess.Popen(f"cargo run -r --bin tester python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc029/a.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更
    proc = subprocess.Popen(f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc029/a.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更

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
        N,M,K,T = map(int,lines[0].replace("\n","").split())

    with open(output_path) as f:
        lines = f.readlines()
        
        L = lines[-1].replace("\n","")
        invest_level = int(lines[-2].replace("\n","").split()[-1])
        score = int(L.split()[-1])
        process_score = int(lines[-3].replace("\n","").split()[-1])
    
    # for i in range(-7,0):
    #     l = lines[i].replace("\n","")
    #     print(l)
    return score,N,M,K,invest_level,process_score

  


sum_score = 0
log_sum = 0
best_sum_score = 0
process_sum = 0
scores = []
errors = []
num = 1000


plot_X = []
plot_Y = []
plot_X2 = []
for i in range(num):
    S = str(i).zfill(4)
    input_path = f"in/{S}.txt"
    output_path = f"out/{S}.txt"
    score_path = f"score/{S}.txt"
    # print(S)
    try:

        score,n,m,k,invest_level,process_score = calc_score(input_path,output_path)
        # print(f"score = {score} N = {n} M = {m} K = {k} invest = {invest_level}")
        scores.append([score,n,m,k,invest_level,process_score,S])
        log_score = math.log2(score)
        log_process_score = math.log2(process_score)
        sum_score += log_score
        process_sum += log_process_score
        plot_X.append(invest_level)
        plot_Y.append(log_score)
        plot_X2.append(log_process_score)
        
    except:
        score = -1
        print("error",i)
        num -= 1


    with open(score_path,"w") as f:
        f.write(str(score))
        


print("average =", sum_score / num,sum_score,process_sum/num)
scores.sort()
print(scores[:20])
print(scores[-20:])

fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.scatter(plot_X,plot_Y)

ax = fig.add_subplot(1,2,2)
ax.scatter(plot_X,plot_X2)

plt.show()