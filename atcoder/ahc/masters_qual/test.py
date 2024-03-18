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

    command = f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/masters_qual/a.py < in/{S}.txt > out/{S}.txt"
    command = f"/Users/morikouhei/a.out < in/{S}.txt > out/{S}.txt"

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

# exit()
def calc_score(input_path, output_path,score_path):

    command = f"cargo run -r --bin score {input_path} {output_path} > {score_path}"
    subprocess.Popen(
        command,
        shell=True,
    )

    with open(score_path) as f:
        


sum_score = 0
scores = []
errors = []
num = 400

sum_count = 0
plot_X = []
plot_Y = []
plot_X2 = []
plot_Y2 = []

count = [0]*300

count_dic = {}
for i in range(num):
    S = str(i).zfill(4)
    input_path = f"in/{S}.txt"
    output_path = f"out/{S}.txt"
    score_path = f"score/{S}.txt"
    # print(S)
    try:

        score, n, m, eps, count,t = calc_score(input_path, output_path)


        scores.append([score,S])
        sum_score += score
        plot_X.append(n)
        plot_Y.append(score)

    except:
        score = -1
        # print("error", i)
        num -= 1

    with open(score_path, "w") as f:
        f.write(str(score))




print("average =", sum_score / num, sum_score,  num)
scores.sort()
print(scores[:20])
print(scores[-20:])

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
ax.scatter(plot_X, plot_Y)

plt.show()
