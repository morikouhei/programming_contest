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

        proc = subprocess.Popen(f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc025/a.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更
        proc_list.append(proc)
        if (i + 1) % max_process == 0 or (i + 1) == N:
            for subproc in proc_list:
                try:
                    subproc.wait(timeout=10)
                except:
                    print("stop")
            proc_list = []


    print("time: ", time.time() - start)



Weight_list = []

Weight = []
query_time = 0
def merge_sort(input_path,output_path):
    global Weight
    global query_time
    with open(input_path) as f:
        lines = f.readlines()
        N,D,Q = map(int,lines[0].split())
        Weight_line = list(map(int,lines[1].replace('\n','').split()))

    Weight = Weight_line[:]
    query_time = 0  


    def query(l,r):
        global Weight
        global query_time
        query_time += 1
        if Weight[l] > Weight[r]:
            return ">"
        else:
            return "<"

    def union(list_L,list_R):

        global query_time

        ll = len(list_L)
        lr = len(list_R)

        list_LR = []
        now = 0
        for i in list_L:
            while now < lr:
                res = query(i,list_R[now])

                if res == "<":
                    break
                else:
                    list_LR.append(list_R[now])
                    now += 1
            
            list_LR.append(i)

        for i in range(now,lr):
            list_LR.append(list_R[i])
                

        return list_LR

    
    def m_sort(lis):

        if len(lis) == 1:
            return lis

        le = len(lis)
        list_L,list_R = lis[:le//2],lis[le//2:]

        list_L = m_sort(list_L)
        list_R = m_sort(list_R)

        list_LR = union(list_L,list_R)

        return list_LR

    
    sort_list = m_sort([i for i in range(N)])

    check_line = [[w,i] for i,w in enumerate(Weight)]
    check_line.sort()

    check_list = [i for _,i in check_line]

    assert sort_list == check_list

    return query_time,N,D,Q


def quick_sort(input_path,output_path):
    global Weight
    global query_time
    with open(input_path) as f:
        lines = f.readlines()
        N,D,Q = map(int,lines[0].split())
        Weight_line = list(map(int,lines[1].replace('\n','').split()))

    Weight = Weight_line[:]
    query_time = 0  


    def query(l,r):
        global Weight
        global query_time
        query_time += 1
        if Weight[l] > Weight[r]:
            return ">"
        else:
            return "<"
    
    def split(lis):

        list_L = []
        list_R = []

        center = lis[0]
        lis = lis[1:]

        for i in lis:
            res = query(center,i)

            if res == ">":
                list_L.append(i)
            else:
                list_R.append(i)
        
        return list_L,center,list_R


    def m_sort(lis):

        if len(lis) <= 1:
            return lis


        list_L,center,list_R = split(lis)

        list_L = m_sort(list_L)
        list_R = m_sort(list_R)

        list_LR = list_L + [center] + list_R

        return list_LR
        

    
    sort_list = m_sort([i for i in range(N)])
    # print(sort_list)
    
    check_line = [[w,i] for i,w in enumerate(Weight)]
    check_line.sort()

    check_list = [i for _,i in check_line]
    # print(check_list)
    assert sort_list == check_list,f"{check_list}, {sort_list}"

    return query_time,N,D,Q



def quick_sort_fake(input_path,output_path):
    global Weight
    global query_time
    with open(input_path) as f:
        lines = f.readlines()
        N,D,Q = map(int,lines[0].split())
        Weight_line = list(map(int,lines[1].replace('\n','').split()))

    Weight = Weight_line[:]
    query_time = 0  


    def query(l,r):
        global Weight
        global query_time
        query_time += 1
        if Weight[l] > Weight[r]:
            return ">"
        else:
            return "<"
    
    def split(lis):

        list_L = []
        list_R = []

        center = lis[0]
        lis = lis[1:]

        for i in lis:
            res = query(center,i)

            if res == ">":
                list_L.append(i)
            else:
                list_R.append(i)
        
        return list_L,center,list_R


    def m_sort(lis):

        if len(lis) <= 10:
            return lis


        list_L,center,list_R = split(lis)

        list_L = m_sort(list_L)
        list_R = m_sort(list_R)

        list_LR = list_L + [center] + list_R

        return list_LR
        

    
    sort_list = m_sort([i for i in range(N)])
    # print(sort_list)
    
    check_line = [[w,i] for i,w in enumerate(Weight)]
    check_line.sort()

    check_list = [i for _,i in check_line]
    # print(check_list)
    # assert sort_list == check_list,f"{check_list}, {sort_list}"

    return query_time,N,D,Q


def calc_score(input_path,output_path):
 
    with open(input_path) as f:
        lines = f.readlines()
        N,D,Q = map(int,lines[0].split())
        Weight = list(map(int,lines[1].replace('\n','').split()))


    Weight_list.append(Weight)
    with open(output_path) as f:
        lines = f.readlines()

        ans = list(map(int,lines[-1].replace('\n','').split()))

    
    ave = sum(Weight)/D

    score = 0

    d_weight = [0]*D

    for i in range(N):
        ind = ans[i]
        d_weight[ind] += Weight[i]

    
    for i in range(D):
        score += (d_weight[i] - ave) ** 2
    
    score /= D
    base_score = score

    return 1 + (int(100*score**0.5)),N,D,Q,base_score



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
        # query_num,n,d,q = merge_sort(input_path,output_path)
        # query_num_quick,n,d,q = quick_sort(input_path,output_path)
        # query_num_quick_fake,n,d,q = quick_sort_fake(input_path,output_path)

        # low = "<" if query_num < query_num_quick_fake else ">"
        # print(query_num/n,low,query_num_quick_fake/n,n)
        # sort_max[n] = max(sort_max[n],query_num/n)
        # sort_num[n] += 1
        # sort_average[n] += query_num/n

        score,n,d,q,base_score = calc_score(input_path,output_path)
        score_best,_,_,_,_ = calc_score(input_path,output_best_path)
        plot_X.append(q/n)
        plot_X2.append(n)
        plot_X3.append(d)
        plot_Y.append(score)
        plot_Y_best.append(score_best)

        sum_score += score
        scores.append([score,S,n,d,score_best])
        plot_XY.append([q/n,n,score,score_best])
        best_sum_score += score_best
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
fig = plt.figure()


ax = fig.add_subplot(1,2,1)


ax.scatter(plot_X,plot_Y)
# ax.scatter(plot_X,plot_Y_best)
ax.set_title('first scatter plot')
ax.set_xlabel('Q/D')
ax.set_ylabel('Score')
# ax.set_ylim(0,5*10**6)

plot_XY.sort()

ax = fig.add_subplot(1,2,2)

plot_Y_now = [score for _,_,score,_ in plot_XY]
plot_Y_best = [score for _,_,_,score in plot_XY]

plot_X_ind = [i for i in range(len(plot_Y_now))]
ax.scatter(plot_X_ind,plot_Y_now)
# ax.scatter(plot_X_ind,plot_Y_best)
# ax.set_ylim(0,3*10**6)

# ax.scatter(plot_X2,plot_Y)


# ax.set_title('first scatter plot')
# ax.set_xlabel('N')
# ax.set_ylabel('Score')

# ax = fig.add_subplot(1,3,3)

# ax.scatter(plot_X3,plot_Y)

# ax.set_title('first scatter plot')
# ax.set_xlabel('D')
# ax.set_ylabel('Score')
plt.show()