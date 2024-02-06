import time
import os
import sys
import random
import itertools
import math

TIME_LIM = 2
stime = time.time()
inf = 10**18
lam = 10**(-5)
atcoder = 0


if os.getenv("ATCODER"):
    atcoder = 1


def generate_exponential_random(lmbda,le):
    """
    指数分布に従って乱数を生成する関数
    
    Args:
    lmbda (float): 指数分布のパラメータ（平均）
    
    Returns:
    float: 指数分布に従う乱数
    """
    lis = [random.expovariate(lmbda) for i in range(le)]
    return lis

N,D,Q = map(int,input().split())

class Environment:

    def __init__(self):
        self.Weight = None
        self.query_times = Q
        self._build()
        self.cashe = {}
        self.order = [[] for i in range(N)]
        self.rorder = [[] for i in range(N)]
        self.single_ban = [0]*N
        self.double_ban = [[0]*N for i in range(N)]

    def _build(self):

        if atcoder != 1:
            self.Weight = list(map(int,input().split()))

    

    def order_search(self,sind):

        vis = set()
        vis.add(sind)

        q = [sind]
        while q:
            now = q.pop()
            for nex in self.order[now]:
                if nex not in vis:
                    vis.add(nex)
                    q.append(nex)

        return vis

    def rorder_search(self,sind):
    
        vis = set()
        vis.add(sind)

        q = [sind]
        while q:
            now = q.pop()
            for nex in self.rorder[now]:
                if nex not in vis:
                    vis.add(nex)
                    q.append(nex)

        return vis


    def ban_check(self,small_index,large_index):

        if len(small_index) > 1 or len(large_index) > 1:
            return 0

        
        if len(small_index) == 0:
            return self.single_ban_check(large_index)

        else:
            return self.double_ban_check(small_index,large_index)

    def ban_apply(self,small_index,large_index):
    
        if len(small_index) > 1 or len(large_index) > 1:
            return 0

        
        if len(small_index) == 0:
            return self.single_ban_apply(large_index)

        else:
            return self.double_ban_apply(small_index,large_index)

    def single_ban_check(self,large_index):

        assert len(large_index) == 1

        ind = list(large_index)[0]

        if self.single_ban[ind]:
            return 1

        vis = self.order_search(ind)
        for v in vis:
            if self.single_ban[v]:
                self.single_ban[ind] = 1
        
        return self.single_ban[ind]

    def single_ban_apply(self,large_index):

        assert len(large_index) == 1

        ind = list(large_index)[0]

        vis = self.rorder_search(ind)
        for v in vis:
            self.single_ban[v] = 1

        return
        
    def double_ban_check(self,small_index,large_index):
        assert len(small_index) == 1
        assert len(large_index) == 1

        lind = list(small_index)[0]
        rind = list(large_index)[0]


        if self.double_ban[lind][rind]:
            return 1

        lvis = self.rorder_search(lind)
        rvis = self.order_search(rind)

        for l in lvis:
            for r in rvis:
                if self.double_ban[l][r]:
                    self.double_ban[lind][rind] = 1

        
        return self.double_ban[lind][rind]

    def double_ban_apply(self,small_index,large_index):
    
        assert len(small_index) == 1
        assert len(large_index) == 1

        lind = list(small_index)[0]
        rind = list(large_index)[0]

        lvis = self.order_search(lind)
        rvis = self.rorder_search(rind)

        for l in lvis:
            for r in rvis:
                self.double_ban[l][r] = 1

        
        return 0
    def check(self,query):
        nl,nr,*query_split = query

        list_l = query_split[:nl]
        list_r = query_split[nl:]

        if nl * nr == 0 or max(nl,nr) > 5:
            return 0

        for f in range(2):

            if nl < nr:

                nl,nr = nr,nl
                list_l,list_r = list_r,list_l
                continue

            vis_list = [self.order_search(ind) for ind in list_l]
            
            assert nl >= nr
            for l in itertools.permutations(range(nl),nr):

                ok = 1
                for i,sind in enumerate(l):
                    if list_r[i] not in vis_list[sind]:
                        ok = 0
                
                if ok:
                    if f == 0:
                        return ">"
                    else:
                        return "<"
            
            nl,nr = nr,nl
            list_l,list_r = list_r,list_l

        return 0

    def memo(self,query,res):

        nl,nr,*query_split = query

        list_l = query_split[:nl]
        list_r = query_split[nl:]

        self.cashe[tuple(query)] = res

        query2 = [nr,nl] + list_r + list_l

        if res == ">":
            res = "<"
        elif res == "<":
            res = ">"

        self.cashe[tuple(query2)] = res



    def add_edge(self,large,small):
        self.order[large].append(small)
        self.rorder[small].append(large)

    def ask_query(self,query,force=False):

        if force:
            self.query_times -= 1
            print(*query)
            sys.stdout.flush()

            if atcoder == 1:
                res = input()
            else:
                res = "<"

            return res
            
        nl,nr,*query_split = query

        list_l = query_split[:nl]
        list_r = query_split[nl:]

        if tuple(query) in self.cashe:
            return self.cashe[tuple(query)]

        if nl == nr == 0:
            return "="
            
        if nl == 0:
            return "<"

        if nr == 0:
            return ">"

        check = self.check(query)
        if check:
            self.memo(query,check)
            return check

        if self.query_times == 0:
            return "?"

        self.query_times -= 1

        assert self.query_times >= 0

        
        if self.query_times >= 0:
            print(*query)
            sys.stdout.flush()

        if atcoder == 1:
            res = input()

        else:
            weight_l,weight_r = 0,0
            for i in list_l:
                weight_l += self.Weight[i]
            for i in list_r:
                weight_r += self.Weight[i]

            if weight_l < weight_r:
                res = "<"
            elif weight_l == weight_r:
                res = "="
            elif weight_l > weight_r:
                res = ">"

        self.memo(query,res)

        if nl == 1 and res != "<":
            i1 = list_l[0]
            for i2 in list_r:
                self.add_edge(i1,i2)

        if nr == 1 and res != ">":
            i1 = list_r[0]
            for i2 in list_l:
                self.add_edge(i1,i2)
        

        return self.cashe[tuple(query)]

    def answer_query(self,ans):
        if self.query_times:
            for i in range(self.query_times):
                self.ask_query([1,1,1,2],force=True)

            self.query_times = 0

        assert self.query_times == 0    

        print(*ans)
        sys.stdout.flush()


environment = Environment()

class State:
    def __init__(self):
        
        self.AVERAGE = 100000
        self.ans = [0]*N
        self.predict_weight = [self.AVERAGE]*N
        self.ans_group = [[] for i in range(D)]
        self.sort_list = []



  
    def re_order(self,sort_group):
        ans_group = []
        for sg in sort_group:
            ans_group.append(self.ans_group[sg][:])

        self.ans_group = ans_group

        ans = [D-1]*N
        for i in range(D):
            for ind in ans_group[i]:
                ans[ind] = i

        if self.ans != ans:
            print("#c ",*ans)

        self.ans = ans[:]

        return [i for i in range(D)]



    def make_query(self,ask_l:list,ask_r:list):

        del_list = []
        for i in ask_l:
            if i in ask_r:
                del_list.append(i)

        for d in del_list:
            ask_l.remove(d)
            ask_r.remove(d)
        ask_l.sort()
        ask_r.sort()

        query = [len(ask_l),len(ask_r)] + ask_l + ask_r

        return query

    def merge_sort(self,sort_cand):

        def query(l,r):
            q = self.make_query(sort_cand[l],sort_cand[r])
            res = environment.ask_query(q)
            return res

        def union(list_L,list_R):

            ll = len(list_L)
            lr = len(list_R)

            list_LR = []
            now = 0
            for i in list_L:
                while now < lr:
                    res = query(i,list_R[now])

                    if res == "?":
                        return res

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

            if list_L == "?" or list_R == "?":
                return "?"
            list_LR = union(list_L,list_R)

            return list_LR

        
        sort_list = m_sort([i for i in range(len(sort_cand))])

        return sort_list        


    def binary_search(self,sort_order,sort_cand,insert_cand):

        l = -1
        r = len(sort_order)

        while r > l + 1:
            m = (r+l)//2

            query = self.make_query(insert_cand,sort_cand[sort_order[m]])

            res = environment.ask_query(query)

            if res == "?":
                return res

            if res == ">":
                l = m
            else:
                r = m

        return r

    def binary_search2(self,sort_order,sort_cand,insert_cand):
    
        l = -1
        r = len(sort_order)

        while r > l + 1:
            m = (r+l)//2

            query = self.make_query(insert_cand[0]+sort_cand[sort_order[m]][1],sort_cand[sort_order[m]][0] + insert_cand[1])

            res = environment.ask_query(query)

            if res == "?":
                return res

            if res == ">":
                l = m
            else:
                r = m

        return r
    def group_remove(self,group,remove_list):

        new_group = group[:]
        for r in remove_list:
            new_group.remove(r)

        return new_group

    def group_add(self,group,add_list):
    
        new_group = group[:]
        for a in add_list:
            new_group.append(a)

        return new_group

    
    ## swap one item from largest and smallest group
    def neighbor(self,small_chose,large_chose):
        # print("# neighbor2", environment.query_times)
        large_group = D-1
        small_group = 0

        if len(self.ans_group[large_group]) == 1:
            large_group -= 1

        large_size = len(self.ans_group[large_group])
        move_large_index = set()
        for i in range(large_chose):
            move_large_index.add(self.ans_group[large_group][random.randint(0,large_size-1)])

        small_size = len(self.ans_group[small_group])
        move_small_index = set()
        for i in range(small_chose):
            move_small_index.add(self.ans_group[small_group][random.randint(0,small_size-1)])

        move_large_index = list(move_large_index)
        move_small_index = list(move_small_index)

        if environment.ban_check(move_small_index,move_large_index):
            return 0


        query = self.make_query(move_small_index,move_large_index)

        res = environment.ask_query(query)

        if res == "?":
            return 0

        if res != "<":
            environment.ban_apply(move_small_index,move_large_index)
            return 0


        nex_large_group = self.group_remove(self.ans_group[large_group],move_large_index)
        nex_small_group = self.group_remove(self.ans_group[small_group],move_small_index)

        query = self.make_query(nex_small_group,nex_large_group)

        res = environment.ask_query(query)

        if res == "?":
            return 0

        if res != "<":
            return 0

        sort_group = [i for i in range(D)]
        sort_group.remove(large_group)
        sort_group.remove(small_group)

        self.ans_group[small_group] = self.group_add(nex_small_group,move_large_index)
        self.ans_group[large_group] = self.group_add(nex_large_group,move_small_index)

        r = self.binary_search(sort_group,self.ans_group,self.ans_group[small_group])

        if r == "?":
            return 0

        sort_group.insert(r,small_group)

        r = self.binary_search(sort_group,self.ans_group,self.ans_group[large_group])

        if r == "?":
            return 0
            
        sort_group.insert(r,large_group)

        sort_group = self.re_order(sort_group)

        return 0

    def largest_differencing_method(self,group1,group2):
        index_list = []
        for ind in self.ans_group[group1] + self.ans_group[group2]:
            index_list.append(ind)

        sort_index_list = self.merge_sort([[ind] for ind in index_list])

        if sort_index_list == "?":
            return 0

        heap_list = [[[index_list[i]],[]] for i in sort_index_list]

        while len(heap_list) > 1:
            h1 = heap_list.pop()
            h2 = heap_list.pop()

            h1[0] += h2[1]
            h1[1] += h2[0]

            r = self.binary_search2([i for i in range(len(heap_list))],heap_list,h1)
            if r == "?":
                return 0
            
            heap_list.insert(r,h1)

        h = heap_list[0]
        # print("# largest differencing", h)
        sort_group = [i for i in range(D)]
        sort_group.remove(group1)
        sort_group.remove(group2)

        self.ans_group[group1] = h[0]
        self.ans_group[group2] = h[1]


        upd = 0
        r = self.binary_search(sort_group,self.ans_group,self.ans_group[group1])
        rs = []
        rs.append(r)
        if r != D-2:
            upd += 1
        if r == "?":
            return 0

        sort_group.insert(r,group1)

        r = self.binary_search(sort_group,self.ans_group,self.ans_group[group2])
        rs.append(r)
        if r != 0:
            upd += 1
        if r == "?":
            return 0
            
        sort_group.insert(r,group2)

        sort_group = self.re_order(sort_group)

        # print("# largest",rs)
        return upd

    def climbing(self):

        loop_count = 0
        last_upd = -1
        while environment.query_times and time.time() - stime <= TIME_LIM - 0.3:
            loop_count += 1

            if True:
                nind = random.randint(1,2)


                if nind == 1:
                    upd = self.neighbor(0,1)

                elif nind == 2:
                    upd = self.neighbor(1,1)

            else:
                nind = random.randint(1,3)

                if nind == 1:
                    upd = self.neighbor1()

                elif nind == 2:
                    upd = self.neighbor2()
                
                else:
                    upd = self.neighbor2(2,3)

            
            if upd:
                last_upd = loop_count

            if loop_count - last_upd > 2*N:
                group1 = -1
                for i in range(D)[::-1]:
                    if len(self.ans_group[i]) > 1:
                        group1 = i
                        break
                
                upd = self.largest_differencing_method(group1,0)


                if upd:
                    last_upd = loop_count
                    continue

                if D == 2:
                    last_upd = loop_count
                    continue
            
                group2 = random.randint(1,group1-1)
                
                upd = self.largest_differencing_method(group1,group2)
                    
                last_upd = loop_count
                # break



    def solve_large(self):

        sort_cand = [[i] for i in range(N)]

        sort_list = self.merge_sort(sort_cand)

        # for i in range(N):
        #     self.ans_group[i%D].append(i)

        # sort_group = self.merge_sort(self.ans_group)

        # sort_group = self.re_order(sort_group)

        sort_group = [i for i in range(D)]

        self.sort_list = sort_list[:]

        sort_list = sort_list[::-1]

        for i in range(N):
            ind = sort_list[i]
            if i < D:
                self.ans_group[-1-i].append(ind)
                continue

            sort_group.remove(0)
            self.ans_group[0].append(ind)

            pos_r = self.binary_search(sort_group,self.ans_group,self.ans_group[0])
            sort_group.insert(pos_r,0)
            sort_group = self.re_order(sort_group)

        self.climbing()


        return self.ans

    def solve_small(self):

        for i in range(N):
            self.ans_group[i%D].append(i)

        sort_group = self.merge_sort(self.ans_group)

        sort_group = self.re_order(sort_group)


        self.climbing()

        return self.ans

class Solver:

    def __init__(self):
        self.State = State()
    def solve(self):


        if Q >= N*math.log2(N) + N*math.log2(D) + 2:
            ans = self.State.solve_large()
        else:
            ans = self.State.solve_small()

        environment.answer_query(ans)

if __name__ == "__main__":
    solver = Solver()
    solver.solve()