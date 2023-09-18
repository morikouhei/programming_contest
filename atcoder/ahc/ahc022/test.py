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

        proc = subprocess.Popen(f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc022/a.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更
        proc_list.append(proc)
        if (i + 1) % max_process == 0 or (i + 1) == N:
            for subproc in proc_list:
                try:
                    subproc.wait(timeout=40)
                except:
                    print("stop")
            proc_list = []


    print("time: ", time.time() - start)


sum_score = 0
scores = []
errors = []
num = N
plot_X = []
plot_Y = []
plot_Y2 = []
plot_X2 = []

plot_X3 = []
plot_Y3 = []

outall = []
for i in range(N):
    # S = files[i]
    S = str(i).zfill(4)

    # with open(f"out/{S}.txt") as f:
    print(f"SCORING {S}")
    output = []
    try:
        with open(f"in/{S}.txt") as f:

            lines = f.readlines()
            L,n,s = map(int,lines[0].split())

        
        # output.append(f"# all N = {n} S = {s}")

        with open(f"out/{S}.txt") as f:

            lines = f.readlines()

            last = lines[-7].split()
            if "Score" not in last:
                raise ValueError("error!")
            output.append([s,L])
            output.append(f"SCORING {S}")
            output.append(lines[0])
            output.append(lines[1])
            
            score = int(last[-1])
            wrong = lines[-5].split()
            wrong = int(wrong[-1])
            plot_Y.append(math.log10(score))
            plot_Y2.append(wrong/n)
            plot_X.append(int(s**0.5))
            plot_X2.append(L)

            placement = int(lines[-3].split()[-1])
            measure = int(lines[-2].split()[-1])
            plot_Y3.append(measure)
            plot_X3.append(placement)

            # score = int([lines[-1].split()[-1]])
            scores.append([score,S])
            sum_score += math.log10(score)
            
            for i in range(-7,0):
                line = lines[i]
                line = line.split("¥n")
                for l in line:
                    output.append(l)
        #     P = []
        #     num = 0
        #     for line in lines:
        #         if line.startswith("#"):
        #             continue
        #         P.append(list(map(int,line.split())))
        #         num += 1

        #         if num == L:
        #             break

        #     E = [int(lines[i]) for i in range(-n,0)]


        # case = 0
        # for i,e in enumerate(E):
        
        #     x,y = XY[e]
        #     est_temp = P[x][y]

        #     x,y = XY[A[i]]
        #     true_temp = P[x][y]
        #     if est_temp != true_temp:
        #         case += 1

        # print(f"# all N = {n} S = {s}")

        # with open(f"score/{S}.txt") as f:
        #     lines = f.readlines()
        #     last = lines[-5].split()
        #     # print(last)
        #     score = int(last[-1])

        #     wrong = lines[-4].split()
        #     wrong = int(wrong[-1])
        #     plot_Y.append(math.log10(score))
        #     plot_Y2.append(wrong/n)
        #     plot_X.append(int(s**0.5))
        #     plot_X2.append(L)

        #     placement = int(lines[-4].split()[-1])
        #     measure = int(lines[-2].split()[-1])
        #     plot_Y3.append(measure)
        #     plot_X3.append(placement)

        #     # score = int([lines[-1].split()[-1]])
        #     scores.append([score,S])
        #     sum_score += math.log10(score)
            
        #     for i in range(-5,0):
        #         output.append(lines[i])
     

        # error = int(lines[-3][4:])
        # errors.append(error)
        outall.append(output)
    except:
        print("error",i)
        num -= 1
        

outall.sort()
for output in outall:
    for o in output:
        print(o)
    print()

print("average =", sum_score / num,sum_score,num)
scores.sort()
print(scores[:10])
print(scores[-10:])


fig = plt.figure()

ax = fig.add_subplot(1,3,1)

ax.scatter(plot_X,plot_Y)

ax.set_title('first scatter plot')
ax.set_xlabel('S')
ax.set_ylabel('Score')
ax.set_ylim([0,9])

ax = fig.add_subplot(1,3,2)

ax.scatter(plot_X,plot_Y2)

ax.set_title('first scatter plot')
ax.set_xlabel('S')
ax.set_ylabel('error rate')

ax = fig.add_subplot(1,3,3)

ax.scatter(plot_X3,plot_Y3)

ax.set_title('first scatter plot')
ax.set_xlabel('placement')
# ax.set_xlim([0,1*10**7])
ax.set_ylabel('measure')
# ax.set_ylim([0,1*10**7])

plt.show()