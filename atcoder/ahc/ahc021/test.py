import subprocess
import time
import os
import random

# import matplotlib.pyplot as plt
# import pandas as pd
#コードをコンパイルする(pythonなどの場合不要)

# epss = ["eps"+str(5*i) for i in range(9)]
# ms = ["m"+str(10*i) for i in range(1,11)]
# epss = ["eps20"]
# ms = ["m"+str(i) for i in range(10,101)]
# files = []
# for eps in epss:
#     for m in ms:
#         S = os.path.join(eps,eps+"_"+m)
#         files.append(S)
# # print(epss)
# # print(ms)
# # print(files)

# for i in range(41):
#     path = os.path.join("out","eps"+str(i))
#     if not os.path.exists(path):
#         os.mkdir(path)

#     path = os.path.join("score","eps"+str(i))
#     if not os.path.exists(path):
#         os.mkdir(path)

# N = len(files)
N = 100
print("number test = ",N)

start = time.time()

#パソコンのプロセス数
max_process = 8 #要変更
proc_list = []
for i in range(N):
    # S = files[i]
    S = str(i).zfill(4)
    # print(S,"S",i)
    # while len(S) != 4:
    #     S = '0' + S


    # # #自分のコードを実行するためのコマンド
    # proc = subprocess.Popen(f"cargo run --release --bin tester /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc021/a.out < in/{S}.txt > out/{S}.txt 2> score/{S}.txt", shell=True)#要変更

    # proc = subprocess.Popen(f"cargo run --release --bin tester python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc021/a.py < in/{S}.txt > out/{S}.txt 2> score/{S}.txt", shell=True)#要変更


    # local tester がないバージョン
    # proc = subprocess.Popen(f"/Users/morikouhei/github/programming_contest/atcoder/ahc/ahc021/a.out < in/{S}.txt > out/{S}.txt", shell=True)#要変更

    proc = subprocess.Popen(f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc021/a.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更
    proc_list.append(proc)
    if (i + 1) % max_process == 0 or (i + 1) == N:
        for subproc in proc_list:
            subproc.wait()
        proc_list = []
print("time: ", time.time() - start)


sum_score = 0
scores = []
errors = []
num = N
for i in range(N):
    # S = files[i]
    S = str(i).zfill(4)

    with open(f"out/{S}.txt") as f:

    # with open(f"score/{S}.txt") as f:
        lines = f.readlines()
        try:
            # last = lines[-1]
            last = lines[-1].split()
            # print(last)
            score = int(last[-1])
            # score = int([lines[-1].split()[-1]])
            scores.append([score,S])
            sum_score += score
        except:
            print("error",i)
            num -= 1
        # error = int(lines[-3][4:])
        # errors.append(error)
        

print("average =", sum_score / num)
scores.sort()
print(scores[:10])
print(scores[-10:])

# X = [int(m[1:]) for m in ms]

# Ysscore = []
# Yserror = []
# dic = {}
# for i in range(N):
#     eps = files[i].split("/")[0]
#     if eps not in dic:
#         dic[eps] = []
#     dic[eps].append([scores[i][0],errors[i]])

# fig = plt.figure()
# ax1 = fig.add_subplot(1,2,1)
# for eps in sorted(dic.keys()):
    
#     Y = [v[0] for v in dic[eps]]
#     print(eps,Y)
#     ax1.plot(X,Y,label=eps)

# ax1.set_ylim(0,2.5*10**6)
# ax1.legend()

# ax2 = fig.add_subplot(1,2,2)
# for eps in sorted(dic.keys()):
#     Y = [v[1] for v in dic[eps]]
#     print(eps,Y)
#     ax2.plot(X,Y,label=eps)
# ax2.legend()

# plt.show()