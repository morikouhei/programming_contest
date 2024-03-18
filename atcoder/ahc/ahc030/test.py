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
def calc_score(input_path, output_path):

    with open(input_path) as f:
        lines = f.readlines()
        N, M, eps = lines[0].replace("\n", "").split()
        N = int(N)
        M = int(M)
        V = [
            list(map(int, lines[i].replace("\n", "").split()))
            for i in range(2 * M + 1, 2 * M + 1 + N)
        ]
        count = 0
        for x in V:
            for y in x:
                if y:
                    count += 1

    with open(output_path) as f:
        lines = f.readlines()

        score = int(lines[-1].replace("\n", "").split()[-1])
        
        t = float(lines[-2].replace("\n", "").split()[-1])
        # print(lines[-2].replace("\n",""))
        # print(lines[-1].replace("\n",""))

    return score, N, M, eps, count,t


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
    # score, N, M, eps = calc_score(input_path, output_path)

    # print(S)
    try:

        score, n, m, eps, count,t = calc_score(input_path, output_path)
        # count_dic[score] = count_dic.get(score,0)+1
        if t > 3:
            print(f"S = {S} score = {score} N = {n} M = {m} t = {t}")

        # if m > 3:
        #     continue

        scores.append([score, n, m, eps, score / (n * n), S])
        sum_score += score
        sum_count += count / (n * n)
        rep = score // 10**6
        percent = rep / count
        # if m > 3:
        #     continue
        plot_X.append(n)
        plot_Y.append(percent)
        plot_X2.append(m)
        plot_Y2.append(score / n**2)

    except:
        score = -1
        # print("error", i)
        num -= 1

    with open(score_path, "w") as f:
        f.write(str(score))



# for key in sorted(count_dic.keys()):
#     print(key,count_dic[key])
# # print(count_dic)

# exit()
print("average =", sum_score / num, sum_score, sum_count / num, num)
scores.sort()
print(scores[:20])
print(scores[-20:])

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
ax.scatter(plot_X, plot_Y)

ax = fig.add_subplot(1, 2, 2)
ax.scatter(plot_X2, plot_Y2)

plt.show()
