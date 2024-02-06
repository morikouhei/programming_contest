import time
import copy
TIME_LIM = 2
stime = time.time()

N,M = map(int,input().split())
LIM = 5000
class Environment:

    def __init__(self):
        self.B = [[]] + [list(map(int,input().split())) for i in range(M)]

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

environment = Environment()

class State:
    def __init__(self,parm_positive_compare_min,parm_negative_compare_min,parm_positive_compare_top):
        
        self.B = copy.deepcopy(environment.B)

        self.ans = []
        self.score = -10000

        self.parm_positive_compare_min = parm_positive_compare_min
        self.parm_negative_compare_min = parm_negative_compare_min

        self.parm_positive_compare_top = parm_positive_compare_top


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

            while move_B:
                B[nind].append(move_B.pop())

        
        return B,ans

    def pop(self,B,ans,pind,v):

        b = B[pind].pop()

        assert b == v

        ans.append([v,0])

        return B,ans


    def greedy_select(self,b,B,min_list):


        # pos = 1
        # while pos < M-1 and min_list[pos][0] < b:
        #     pos += 1
        # nind = min_list[pos][1]
        # return nind

        best = -10**10
        nind = -1

        for min_val,ind in min_list[1:]:

            top_val = 1000 if B[ind] == [] else B[ind][-1]

            pos_min = max(b - min_val,0)*1000
            neg_min = max(min_val-b,0)

            pos_top = max(b-top_val,0)
            
            score = pos_min * self.parm_positive_compare_min + neg_min * self.parm_negative_compare_min + pos_top * self.parm_positive_compare_top

            if score > best:
                best = score
                nind = ind

        return nind


    def greedy_search(self,base_B,V_lim,temp_B,nind,sid,pind):

        B = copy.deepcopy(base_B)


        V = len(temp_B) + 1
        lind = B[pind].index(temp_B[0])

        B,ans = self.move(B,[],pind,lind,nind)

        for id in range(sid,N+1):
            
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

                len_temp = 1
                
                mind = move_B.pop()
                nind = nind_list.pop()

                while move_B and nind_list[-1] == nind:
                    mind = move_B.pop()
                    nind_list.pop()
                    len_temp += 1

                
                lind = B[pind].index(mind)

                

                V += len_temp + 1

                if V > V_lim:
                    return V
                
                B,ans = self.move(B,[],pind,lind,nind)


            B,ans = self.pop(B,[],pind,id)


        return V


    def greedy(self):

        B = copy.deepcopy(self.B)
        ans = []

        V = 0
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

                temp_B = [mind]

                while move_B and nind_list[-1] == nind:
                    mind = move_B.pop()
                    temp_B.append(mind)
                    nind_list.pop()

                temp_B = temp_B[::-1]

                best_id = -1
                best_V = 10**10
                for cand_id in range(1,M+1):
                    if cand_id == pind:
                        continue
                    
                    cand_V = self.greedy_search(B,best_V,temp_B[:],cand_id,id,pind)

                    if cand_V < best_V:
                        best_V = cand_V
                        best_id = cand_id

                nind = best_id
                assert nind != -1
                
                lind = B[pind].index(mind)
                B,ans = self.move(B,ans,pind,lind,nind)


            B,ans = self.pop(B,ans,pind,id)


        return ans


class Solver:

    def __init__(self):
        # self.State = State(-90.4017219396674,-31.00490239736095,49.76106626964597,0.8885722529133832,-2.273673130310137)
        # self.State = State(-90,-18,75)
        self.State = State(-10,-1,0)


    def solve(self):

        ans = self.State.greedy()
        environment.out_ans(ans)
        

if __name__ == "__main__":
    solver = Solver()
    solver.solve()