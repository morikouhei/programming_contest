import subprocess
import time
import os
import random
import math
import matplotlib.pyplot as plt
import pandas as pd
#コードをコンパイルする(pythonなどの場合不要)

# N = len(files)
N = 400
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

        proc = subprocess.Popen(f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc024/a.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更
        proc_list.append(proc)
        if (i + 1) % max_process == 0 or (i + 1) == N:
            for subproc in proc_list:
                try:
                    subproc.wait(timeout=10)
                except:
                    print("stop")
            proc_list = []


    print("time: ", time.time() - start)


nums = [0]*(101)
nums_all = [0]*(101)
plot_X2 = []
plot_Y2 = []

freqs = [0]*100
def calc_score(input_path,output_path):

    
    with open(input_path) as f:
        lines = f.readlines()
        n,m = map(int,lines[0].split())
        C = [list(map(int,lines[i].replace('\n','').split())) for i in range(1,n+1)]


    around = [set() for i in range(m)]

    for x in range(n):
        for y in range(n):
            c = C[x][y]

            for dx,dy in [[1,0],[0,1],[0,-1],[-1,0]]:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < n and C[nx][ny] != c:
                    around[c-1].add(C[nx][ny])


    for a in around:
        freqs[len(a)] += 1
    # with open(output_path) as f:
    #     lines = f.readlines()

    #     m = int(lines[0])
    #     KIJS = [list(map(int,lines[i].split())) for i in range(1,m+1)]

    


sum_score = 0
scores = []
errors = []
num = N
plot_X = []
plot_Y = []

plot_X3 = []
plot_Y3 = []

mod_score = [0]*4
mod_num = [0]*4
outall = []
for i in range(N):
    # S = files[i]
    S = str(i).zfill(4)

    # with open(f"out/{S}.txt") as f:
    # print(f"SCORING {S}")
    output = []

    input_path = f"in/{S}.txt"
    output_path = f"out/{S}.txt"
    calc_score(input_path,output_path)

    # score,wall_rate,harvest_rate = calc_score(input_path,output_path)
    # mod_score[i%4] += score
    # mod_num[i%4] += 1
    # sum_score += score
    # scores.append([score,S])
    # plot_X.append(wall_rate)
    # plot_Y.append(score)
    # try:
    #     score = calc_score(input_path,output_path)

    #     sum_score += score
    #     scores.append([score,S])

    # except:
    #     print("error",i)
    #     num -= 1
        

# outall.sort()
# for output in outall:
#     for o in output:
#         print(o)
#     print()

# print("average =", sum_score / num,sum_score,num)
# print([x/y for x,y in zip(mod_score,mod_num)])
# scores.sort()
# print(scores[:10])
# print(scores[-10:])

fig = plt.figure()

ax = fig.add_subplot(1,1,1)

ma = 0
for i in range(100):
    if freqs[i]:
        ma = i
plot_X = [i for i in range(ma+1)]
print(freqs[:ma+1])
print(ma)
freqs = freqs[:ma+1]

ax.scatter(plot_X,freqs)

ax.set_title('first scatter plot')
ax.set_xlabel('wall rate')
ax.set_ylabel('Score')

# ax.set_ylim([0,9])

# # plot_X2 = [i for i in range(100)]
# for i in range(101):
#     if nums_all[i] == 0:
#         continue
#     plot_X2.append(i)
#     plot_Y2.append(nums[i]/nums_all[i])

# all_sum = sum(nums_all)


# # plot_Y2 = [x/y for y,x in zip(nums[1:],nums_all[1:])]
# ax = fig.add_subplot(1,3,2)

# ax.scatter(plot_X2,plot_Y2)

# ax.set_title('first scatter plot')
# ax.set_xlabel('S')
# ax.set_ylabel('length')

# plot_X3 = [i for i in range(101)]
# plot_Y3 = [i/all_sum for i in nums_all]
# ax = fig.add_subplot(1,3,3)

# ax.scatter(plot_X3,plot_Y3)

# ax.set_title('first scatter plot')
# ax.set_xlabel('placement')
# # ax.set_xlim([0,1*10**7])
# ax.set_ylabel('measure')
# # ax.set_ylim([0,1*10**7])

plt.show()