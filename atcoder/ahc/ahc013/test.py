import subprocess
import time

#コードをコンパイルする(pythonなどの場合不要)
print("input number test")
N = int(input())

start = time.time()

#パソコンのプロセス数
max_process = 100#要変更
proc_list = []
for i in range(N):
    S = str(i)
    while len(S) != 4:
        S = '0' + S
    #自分のコードを実行するためのコマンド
    proc = subprocess.Popen(f"/usr/bin/python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc013/a.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更
    proc_list.append(proc)
    if (i + 1) % max_process == 0 or (i + 1) == N:
        for subproc in proc_list:
            subproc.wait()
        proc_list = []

print("time: ", time.time() - start)

sum_score = 0
scores = []
err = []
for i in range(N):
    S = str(i)
    while len(S) != 4:
        S = '0' + S
    with open(f"out/{S}.txt") as f:
        lines = f.readlines()
        # print(S)
        score = int(lines[0])
        if score == -1:
            err.append(S)
        scores.append([score,S])
        sum_score += score
print("average =", sum_score / N)
scores.sort()
print(scores[:10])
for i in err:
    print(i)
print(len(err))