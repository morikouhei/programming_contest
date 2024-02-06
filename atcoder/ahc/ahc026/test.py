import subprocess
import time
import os
import random
import math
import matplotlib.pyplot as plt
import pandas as pd
#コードをコンパイルする(pythonなどの場合不要)

# N = len(files)
N = 100
print("number test = ",N)

start = time.time()
s = input()
if s == "1":
    #パソコンのプロセス数
    max_process = 5 #要変更
    proc_list = []
    S_list = [str(i).zfill(4) for i in range(N)]

    for i in range(N):
        # S = files[i]

        S = str(i).zfill(4)
        # command = f"rm out/{S}.txt"
        # subprocess.Popen(command,shell=True)
        # exit()
        # #自分のコードを実行するためのコマンド
        # proc = subprocess.Popen(f"cargo run --release --bin tester /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc021/a.out < in/{S}.txt > out/{S}.txt 2> score/{S}.txt", shell=True)#要変更

        # proc = subprocess.Popen(f"cargo run --release --bin tester python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc022/a.py < in/{S}.txt > out/{S}.txt 2> score/{S}.txt", shell=True)#要変更


        # local tester がないバージョン
        # proc = subprocess.Popen(f"/Users/morikouhei/github/programming_contest/atcoder/ahc/ahc021/a.out < in/{S}.txt > out/{S}.txt", shell=True)#要変更

        proc = subprocess.Popen(f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc026/a.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更
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
        N,M = map(int,lines[0].split())
        B = [[]] + [list(map(int,lines[i].replace('\n','').split())) for i in range(1,M+1)]


    with open(output_path) as f:
        lines = f.readlines()

        ans = [list(map(int,lines[i].replace('\n','').split())) for i in range(len(lines))]

    V = 0

    finished = 0

    for v,i in ans:

        
        
        
        bi = -1
        for j in range(1,M+1):
            if v in B[j]:
                bi = j
                break


        assert bi != -1

        if i == 0:
            assert v == finished+1
            finished += 1
            B[bi].pop()
            continue

        pop_list = []
        while True:
            pop_list.append(B[bi].pop())
            if pop_list[-1] == v:
                break
        
        V += len(pop_list)+1
        while pop_list:
            B[i].append(pop_list.pop())



    return max(1,10000-V)


sum_score = 0
best_sum_score = 0
scores = []
errors = []
num = N
plot_X = []
plot_Y = []
plot_X2 = []
plot_X3 = []

plot_Y_best = []
plot_XY = []
sort_average = [0]*101
sort_max = [0]*101
sort_num = [0]*101
for i in range(N):
    # S = files[i]
    S = str(i).zfill(4)

    input_path = f"in/{S}.txt"
    output_path = f"out/{S}.txt"
    output_best_path = f"out_best/{S}.txt"
    try:

        score = calc_score(input_path,output_path)
        plot_X.append(S)
        plot_Y.append(score)

        sum_score += score
        scores.append([score,S])
    except:
        print("error",i)
        num -= 1
        

# for i in range(30,101):
#     print(i,sort_max[i],sort_average[i]/sort_num[i])
# exit()

print("average =", sum_score / num,sum_score,best_sum_score/num,num)
scores.sort()
print(scores[:10])
print(scores[-10:])
