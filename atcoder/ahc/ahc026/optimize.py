import time
import copy
import optuna
import random

random.seed(998244353)

TIME_LIM = 2
stime = time.time()

N,M = 200,10
LIM = 5000
random_list = [i for i in range(1,N+1)]

rep = 400

Bs = []
for i in range(rep):

    random.shuffle(random_list)

    B = []
    B.append([[]])
    id = 0
    for j in range(M):
        b = []
        for k in range(N//M):
            b.append(random_list[id])
            id += 1
        B.append(b)
    Bs.append(B)



           
class Environment:

    def __init__(self,B):
        self.B = [[]] + B

    def out_ans(self,ans):

        assert len(ans) <= LIM

        for v,i in ans:
            print(v,i)

        exit()

    def calc_score(self,ans):

        assert len(ans) <= LIM

        B = copy.deepcopy(self.B)
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

environment = Environment(B)

class State:
    def __init__(self,parm_positive_compare_min,parm_negative_compare_min,parm_positive_compare_top,parm_negative_compare_top,parm_inverse_sum,parm_line_length,B):
        
        self.B = copy.deepcopy(B)

        self.ans = []
        self.score = -10000

        self.V = 0
        self.parm_positive_compare_min = parm_positive_compare_min
        self.parm_negative_compare_min = parm_negative_compare_min

        self.parm_positive_compare_top = parm_positive_compare_top
        self.parm_negative_compare_top = parm_negative_compare_top

        self.parm_inverse_sum = parm_inverse_sum

        self.parm_line_length = parm_line_length


    def update(self,ans,score):

        if self.score < score:
            self.ans = ans[:]
            self.score = score
        

    def move(self,B,ans,pind,lind,nind):

    
        move_B = []

        for i in range(lind,len(B[pind]))[::-1]:
            move_B.append(B[pind].pop())

        if move_B:
            ans.append([move_B[-1],nind])
            self.V += len(move_B) + 1

            while move_B:
                B[nind].append(move_B.pop())

        
        return B,ans

    def pop(self,B,ans,pind,v):

        b = B[pind].pop()

        assert b == v

        ans.append([v,0])

        return B,ans


    def greedy_select(self,b,B,min_list):

        best = -10**10
        nind = -1

        for min_val,ind in min_list[1:]:

            top_val = 1000 if B[ind] == [] else B[ind][-1]

            pos_min = max(b - min_val,0) * 1000
            neg_min = max(min_val-b,0)

            pos_top = max(b-top_val,0)
            neg_top = max(top_val-b,0)
            

            inverse = 0
            # for nb in B[ind]:
            #     if nb > b:
            #         inverse += 1

            line_length = len(B[ind])
            
            score = pos_min * self.parm_positive_compare_min + neg_min * self.parm_negative_compare_min + pos_top * self.parm_positive_compare_top + neg_top * self.parm_negative_compare_top + inverse * self.parm_inverse_sum + line_length * self.parm_line_length

            if score > best:
                best = score
                nind = ind

        return nind


    def greedy(self):

        B = copy.deepcopy(self.B)
        ans = []

        for id in range(1,N+1):
            
            min_list = []
            for i in range(1,M+1):
                if B[i]:
                    min_list.append([min(B[i]),i])
                else:
                    min_list.append([10000,i])
            
            min_list.sort()

            pind = min_list[0][1]
            lind = B[pind].index(id)+1
            move_B = B[pind][lind:]

            nind_list = []
            for b in move_B:

                nind = self.greedy_select(b,B,min_list)
                nind_list.append(nind)

            
            while move_B:

                mind = move_B.pop()
                nind = nind_list.pop()

                while move_B and nind_list[-1] == nind:
                    mind = move_B.pop()
                    nind_list.pop()

                
                lind = B[pind].index(mind)
                self.move(B,ans,pind,lind,nind)

       
            
            # while move_B:

            #     mind = move_B.pop()
            #     temp_B = [mind]
            #     nind = self.greedy_select(mind,B,min_list)

            #     while move_B:
            #         nb = move_B[-1]
            #         if self.greedy_select(nb,B,min_list) != nind:
            #             break
            #         temp_B.append(move_B.pop())

                
            #     lind = B[pind].index(temp_B[-1])
            #     self.move(B,ans,pind,lind,nind)

            #     for i in range(M):
            #         if min_list[i][1] == nind:
            #             min_list[i][0] = min(min_list[i][0],min(temp_B))
            #             break
                # min_list.sort()


            self.pop(B,ans,pind,id)


        return max(1,10000-self.V)


class Solver:

    def __init__(self,parm_positive_compare_min,parm_negative_compare_min,parm_positive_compare_top,parm_negative_compare_top,parm_inverse_sum,parm_line_length,B):
        self.State = State(parm_positive_compare_min,parm_negative_compare_min,parm_positive_compare_top,parm_negative_compare_top,parm_inverse_sum,parm_line_length,B)
    def solve(self):

        ans = self.State.greedy()
        return ans
        # environment.out_ans(ans)
        

import optuna
import matplotlib.pyplot as plt

def objective(trial):
    parm_positive_compare_min = trial.suggest_float("parm_positive_compare_min",-100,0)
    parm_negative_compare_min = trial.suggest_float("parm_negative_compare_min",-100,0)

    parm_positive_compare_top = trial.suggest_float("parm_positive_compare_top",-100,100)

    parm_line_length = trial.suggest_float("parm_line_length",-100,100)
    # parm_negative_compare_top = trial.suggest_float("parm_negative_compare_top",-100,100)

    # parm_inverse_sum = trial.suggest_float("parm_inverse_sum",-100,100)
    
    score = 0

    for B in Bs:
        score += Solver(parm_positive_compare_min,parm_negative_compare_min,parm_positive_compare_top,0,0,parm_line_length,B).solve()

    return score/rep

study = optuna.create_study(direction="maximize")
study.optimize(objective,n_trials=1000)


epoches = []    # 試行回数格納用
values = []    # best_value格納用
best = 0   # 適当に最大値を格納しておく
# best更新を行う
for i in study.trials:
    if best < i.value:
        best = i.value
    epoches.append(i.number+1)
    values.append(best)


print(study.best_params)
# グラフ設定等
plt.plot(epoches, values, color="red")
plt.title("optuna")
plt.xlabel("trial")
plt.ylabel("value")
plt.show()