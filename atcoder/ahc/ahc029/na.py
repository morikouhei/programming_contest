from enum import Enum
import os
import time
import random
import math
import copy

random.seed(998244353)
stime = time.time()
TIME_LIM = 2
TURN = 1000
INF = 1<<40
atcoder = 0
if os.getenv("ATCODER"):
    atcoder = 1


MAX_INVEST_LEVEL = 20


class CardType(Enum):
    WORK_SINGLE = 0
    WORK_ALL = 1
    CANCEL_SINGLE = 2
    CANCEL_ALL = 3
    INVEST = 4

def clamp(x,l,r):
    return min(max(x,l),r)

class Judge:

    def __init__(self, n: int, m: int, k: int):
        self.n = n
        self.m = m
        self.k = k

        self.project_index = 0
        self.card_index = 0
        self.turn = 0
        self.invest_level = 0
        self.cards_list = []
        self.projects_list = []

        self.has_project_list = []
        self.has_card_list = []
        self.money = 0

        self.use_card_index = -1
        self._build()

    def _build(self):

        if atcoder:
            return

        for i in range(self.m*(TURN+1)):
            h, v = map(int, input().split())
            self.projects_list.append([h,v])
        for i in range(self.n):
            t, w = map(int, input().split())
            self.cards_list.append([t,w,0])
        for i in range(self.k*TURN):
            t, w, p = map(int, input().split())
            self.cards_list.append([t,w,p])

    def read_initial_cards(self):
        cards = []
        
        if atcoder:
            for _ in range(self.n):
                t, w = map(int, input().split())
                cards.append([CardType(t), w, 0])

        else:
            for i in range(self.card_index,self.card_index+self.n):
                t_,w_,p_ = self.cards_list[i]
                t,w = t_ , w_ * (1<<self.invest_level)
                cards.append([CardType(t), w, 0])
            self.card_index += self.n

        self.has_card_list = cards[:]

        return cards

    def read_initial_projects(self):
        projects = []
        if atcoder:
            for _ in range(self.m):
                h, v = map(int, input().split())
                projects.append([h, v, h/v])

        else:
            for i in range(self.project_index,self.project_index+self.m):
                h_,v_ = self.projects_list[i]
                h,v = h_ * (1<<self.invest_level), v_ * (1<<self.invest_level)
                projects.append([h, v, h/v])
            self.project_index += self.m


        self.has_project_list = projects[:]

        return projects

    def read_projects(self):
        projects = []
        if atcoder:
            for _ in range(self.m):
                h, v = map(int, input().split())
                projects.append([h, v, h/v])

            self.has_project_list = projects[:]

        else:
            projects = self.has_project_list[:]

        return projects

    def _update_project(self,m):

        if atcoder:
            return
        else:
            h_,v_ = self.projects_list[self.project_index]
            h,v = h_ * (1<<self.invest_level), v_ * (1<<self.invest_level)
            self.has_project_list[m] = [h,v, h/v]
            self.project_index += 1


    def use_card(self, c: int, m: int):
        
        print(f"{c} {m}", flush=True)
        self.use_card_index = c

        cardtype,w,_ = self.has_card_list[c]

        if cardtype == CardType.WORK_SINGLE:
            self.has_project_list[m][0] -= w
            if self.has_project_list[m][0] <= 0:
                self.money += self.has_project_list[m][1]
                self._update_project(m)

        elif cardtype == CardType.WORK_ALL:
            # assert m == 0
            for i in range(self.m):
                self.has_project_list[i][0] -= w
                if self.has_project_list[i][0] <= 0:
                    self.money += self.has_project_list[i][1]
                    self._update_project(i)


        elif cardtype == CardType.CANCEL_SINGLE:
            self._update_project(m)

        elif cardtype == CardType.CANCEL_ALL:
            # assert m == 0
            for i in range(self.m):
                self._update_project(i)

        elif cardtype == CardType.INVEST:
            # assert m == 0

            self.invest_level += 1
            # assert self.invest_level <= MAX_INVEST_LEVEL


    def read_money(self):

        if atcoder:
            money = int(input())
            # assert money == self.money
        else:
            money = self.money
        return money


    def read_next_cards(self):
        cards = []
        if atcoder:
            for _ in range(self.k):
                t, w, p = map(int, input().split())
                cards.append([CardType(t), w, p])
        else:
            for i in range(self.card_index,self.card_index+self.k):
                t_,w_,p_ = self.cards_list[i]
                t,w,p = t_ , w_ * (1<<self.invest_level), p_ * (1<<self.invest_level)
                cards.append([CardType(t), w, p])
            self.card_index += self.k


        return cards


    def select_card(self, r, next_cards):
        print(r, flush=True)

        # assert self.use_card_index != -1
        self.has_card_list[self.use_card_index] = next_cards[r]
        
        self.money -= next_cards[r][2]

        self.use_card_index = -1

        # assert self.money >= 0

    def comment(self, message: str):
        print(f"# {message}")



class Judge_playout:

    def __init__(self, n,m,k,freaqs,repeat):
        self.n = n
        self.m = m
        self.k = k
        self.freaqs = freaqs
        self.repeat = repeat
        self.cards_len = 0
        self.projects_len = 0

        self.project_index = 0
        self.card_index = 0
        self.turn = 0
        self.invest_level = 0
        self.cards_list = []
        self.projects_list = []

        self.has_project_list = []
        self.has_card_list = []
        self.money = 0

        self.use_card_index = -1
        self._build()

    def _build(self):

        self.random_list = []
        for i,f in enumerate(self.freaqs):
            for j in range(f):
                self.random_list.append(i)

        size = len(self.random_list)

        for i in range(self.m*10*(TURN+1)):

            b = random.uniform(2,8)

            h = int(2**b)
            v = int(2**clamp(random.gauss(b,0.5),0,10))
            self.projects_list.append([h,v])


        for i in range(10*TURN):

            cards_turn = [[0,1,0]]

            for j in range(self.k-1):
                t = self.random_list[random.randint(0,size-1)]

                if t == 0 or t == 1:
                    w = random.randint(1,50)

                    if t == 0:
                        p = clamp(int(random.gauss(w,w/3)),1,10000)
                    
                    elif t == 1:
                        p = clamp(int(random.gauss(w*self.m,w*self.m/3)),1,10000)

                elif t == 2 or t == 3:
                    w = 0
                    p = random.randint(0,10)
                else:
                    w = 0
                    p = random.randint(200,1000)
                    cards_turn.append([t,w,p])
            self.cards_list.append(cards_turn)

        self.cards_len = len(self.cards_list)
        self.projects_len = len(self.projects_list)

        self.random_cards_start_pos = [random.randint(0,10*TURN-1) for i in range(self.repeat)]
        self.random_projects_start_pos = [random.randint(0,self.projects_len-1) for i in range(self.repeat)]


    def reset(self,i,turn,play_cards,play_projects,play_money,invest_level):
        self.project_index = (self.random_projects_start_pos[i]+turn)%self.projects_len
        self.card_index = (self.random_cards_start_pos[i]+turn)%self.cards_len
        self.turn = turn
        self.has_project_list = play_projects[:]
        self.has_card_list = play_cards[:]
        self.money = play_money
        self.invest_level = invest_level


   
    def read_projects(self):
        projects = self.has_project_list[:]

        return projects

    def _update_project(self,m):

        h_,v_ = self.projects_list[self.project_index]
        h,v = h_ * (1<<self.invest_level), v_ * (1<<self.invest_level)
        self.has_project_list[m] = [h,v, h/v]
        self.project_index += 1
        if self.project_index == self.projects_len:
            self.project_index = 0


    def use_card(self, c: int, m: int):
        
        self.use_card_index = c

        cardtype,w,_ = self.has_card_list[c]

        if cardtype == CardType.WORK_SINGLE:
            self.has_project_list[m][0] -= w
            if self.has_project_list[m][0] <= 0:
                self.money += self.has_project_list[m][1]
                self._update_project(m)

        elif cardtype == CardType.WORK_ALL:
            # assert m == 0
            for i in range(self.m):
                self.has_project_list[i][0] -= w
                if self.has_project_list[i][0] <= 0:
                    self.money += self.has_project_list[i][1]
                    self._update_project(i)


        elif cardtype == CardType.CANCEL_SINGLE:
            self._update_project(m)

        elif cardtype == CardType.CANCEL_ALL:
            # assert m == 0
            for i in range(self.m):
                self._update_project(i)

        elif cardtype == CardType.INVEST:
            # assert m == 0

            self.invest_level += 1
            # assert self.invest_level <= MAX_INVEST_LEVEL


    def read_money(self):

        money = self.money
        return money


    def read_next_cards(self):
        cards = []
        for t_,w_,p_ in self.cards_list[self.card_index]:
            t,w,p = t_ , w_ * (1<<self.invest_level), p_ * (1<<self.invest_level)
            cards.append([CardType(t), w, p])
        
        self.card_index += 1
        if self.card_index == self.cards_len:
            self.card_index = 0
        return cards


    def select_card(self, r, next_cards):
        # assert self.use_card_index != -1
        self.has_card_list[self.use_card_index] = next_cards[r]
        
        self.money -= next_cards[r][2]

        self.use_card_index = -1

        # assert self.money >= 0

    def comment(self, message: str):
        print(f"# {message}")

class Solver:

    def __init__(self, n: int, m: int, k: int, t: int):
        self.n = n
        self.m = m
        self.k = k
        self.t = t
        self.judge = Judge(n, m, k)
        self.playout_judge = None
        self.card_freaqs = [0]*5

        self.RANDOM_PLAYOUT_TURN = 800
        self.RANDOM_PLAYOUT_REPEAT = 100


    def _log_info(self):

        for i,project in enumerate(self.projects):
            self.judge.comment(f"project {i} , h = {project[0]} v = {project[1]}")

        for i,card in enumerate(self.cards):
            self.judge.comment(f"card {i} , t = {card[0]} w = {card[1]}")
        self.judge.comment(f"turn = {self.turn} money = {self.money}")

    def _log_summary(self):

        self.judge.comment(f"use card stats = {self.use_card_stats}")
        self.judge.comment(f"bought card stats = {self.bought_card_stats}")
        self.judge.comment(f"bought card cost = {self.bought_card_cost}")

        self.judge.comment(f"project gain = {self.project_gain} card gain = {self.card_gain} dif = {self.money - self.project_gain - self.card_gain}") 
        self.judge.comment(f"finish project = {self.finish_project} process max = {self.process_max}")
        self.judge.comment(f"invest_level = {self.invest_level}")

        self.judge.comment(f"score = {self.money}")
    

    def get_cutoff_limit(self):

        progress = self.turn / TURN
        if self.k <= 3:
            return 1.1
        else:
            return 1.2

        # return 1.1 + (1.2-1.1)*progress
    def solve(self):
        self.turn = 0
        self.money = 0
        self.invest_level = 0
        self.cards = self.judge.read_initial_cards()
        self.projects = self.judge.read_initial_projects()

        self.use_card_stats = [0]*6
        self.bought_card_stats = [0]*6
        self.bought_card_cost = [0]*6


        self.project_gain = 0
        self.card_gain = 0
        self.process_max = 0
        self.finish_project = 0

        for _ in range(self.t):

            # Card を選ぶ
            use_card_i, use_target = self._select_action(self.cards,self.projects,TURN-self.turn,self.invest_level)
            if self.cards[use_card_i][0] == CardType.INVEST:
                self.invest_level += 1

            # example for comments
            self.judge.comment(f"used {self.cards[use_card_i]} to target {use_target}")
            self.judge.use_card(use_card_i, use_target)
            # assert self.invest_level <= MAX_INVEST_LEVEL

            # Project が更新される
            self.projects = self._apply_projects(use_card_i,use_target)
            self.money = self.judge.read_money()


            # 次のCard を選ぶ
            next_cards = self.judge.read_next_cards()
            select_card_i = self._select_next_card(next_cards,self.projects,TURN-self.turn,self.invest_level,self.money)

            # # has_invest = 0
            # for t,w,p in next_cards:
            #     if t == CardType.INVEST and p <= self.money:
            #         has_invest = 1

            # if self.turn > self.RANDOM_PLAYOUT_TURN and has_invest:
            #     select_card_i = self._select_next_card_random_playput(self.cards,self.projects,TURN-self.turn,self.invest_level,self.money,next_cards,use_card_i)
            # else:
            #     select_card_i = self._select_next_card(next_cards,self.projects,TURN-self.turn,self.invest_level,self.money)

            self.cards[use_card_i] = next_cards[select_card_i]
            self.judge.select_card(select_card_i,next_cards)

            self._apply_cards(next_cards,select_card_i)

            self.money -= next_cards[select_card_i][2]
            # assert self.money >= 0

            self.process_max = max(self.process_max,self.money)


            self.turn += 1

            # if self.turn == self.RANDOM_PLAYOUT_TURN:
            #     self.playout_judge = Judge_playout(self.n,self.m,self.k,self.card_freaqs,self.RANDOM_PLAYOUT_REPEAT)

            self._log_info()
            

        self._log_summary()

        return self.money
    
    def _random_playput(self,play_cards,play_projects,play_money,turn_left,invest_level):

        score = 0
        
        for i in range(self.RANDOM_PLAYOUT_REPEAT):

            now_cards = [card[:] for card in play_cards]
            now_projects = [project[:] for project in play_projects]
            now_money = play_money
            now_invest_level = invest_level

            self.playout_judge.reset(i,turn_left,now_cards,now_projects,now_money,now_invest_level)

            for turn in range(turn_left+1)[::-1]:
    
                # Card を選ぶ
                use_card_i, use_target = self._select_action(now_cards,now_projects,turn,now_invest_level)
                if now_cards[use_card_i][0] == CardType.INVEST:
                    now_invest_level += 1

                # assert now_invest_level <= MAX_INVEST_LEVEL

                # Project が更新される
                self.playout_judge.use_card(use_card_i, use_target)
                now_projects = self.playout_judge.read_projects()
                now_money = self.playout_judge.read_money()


                # 次のCard を選ぶ
                next_cards = self.playout_judge.read_next_cards()
                select_card_i = self._select_next_card(next_cards,now_projects,turn,now_invest_level,now_money,True)
                now_cards[use_card_i] = next_cards[select_card_i]
                self.playout_judge.select_card(select_card_i,next_cards)

                now_money -= next_cards[select_card_i][2]
                # assert now_money >= 0
            score += now_money
            # score += math.log2(now_money)

        return score

    def _select_next_card_random_playput(self,now_cards,now_projects,turn_left,invest_level,now_money,next_cards,use_card_i):
        can_buy_cards = []
        for i,(t,w,p) in enumerate(next_cards):
            if p > self.money:
                continue
     
            if t == CardType.WORK_SINGLE:
                gain = w-p
                if gain < 0:
                    continue

            elif t == CardType.WORK_ALL:
                gain = w*self.m - p
                if gain < 0:
                    continue

            elif t == CardType.CANCEL_SINGLE:
    
                if (p >> invest_level) > 1:
                    continue
            elif t == CardType.CANCEL_ALL:

                if (p >> invest_level) > 1:
                    continue

            
            can_buy_cards.append([i,t,w,p])

        # assert can_buy_cards

        if len(can_buy_cards) == 1:
            return can_buy_cards[0][0]

        select_card_i = -1
        select_card_best = -1
        cand = []
        invest_i = -1
        invest_best = -1
        for i,t,w,p in can_buy_cards:

            play_money = now_money - p
            play_cards = now_cards[:]
            play_cards[use_card_i] = next_cards[i][:]
            play_projects = now_projects[:]

            play_score = self._random_playput(play_cards,play_projects,play_money,turn_left-1,invest_level)
            cand.append([t,w,p,play_score])
            if play_score > select_card_best:
                select_card_best = play_score
                select_card_i = i

            if t == CardType.INVEST:
                if play_score > invest_best:
                    invest_best = play_score
                    invest_i = i

        # self.judge.comment(f"playout result = {cand}")
        if select_card_i == invest_i:
            return select_card_i

        dif = (select_card_best-invest_best)/self.RANDOM_PLAYOUT_REPEAT / (1 << invest_level)
        # self.judge.comment(f"dif = {dif}")
        if dif > 10:
            return select_card_i
        else:
            return invest_i

    def _apply_projects(self,c,m):

        cardtype,w,p = self.cards[c]

        if cardtype == CardType.WORK_SINGLE:
            if p == 0:
                self.use_card_stats[0] += 1
            else:
                self.use_card_stats[1] += 1

            if self.projects[m][0] <= w:

                self.project_gain += self.projects[m][1]
                self.finish_project += 1

        elif cardtype == CardType.WORK_ALL:

            # assert m == 0
            for i in range(self.m):
                if self.projects[i][0] <= w:
                    self.project_gain += self.projects[i][1]


            self.use_card_stats[2] += 1


        elif cardtype == CardType.CANCEL_SINGLE:
            self.use_card_stats[3] += 1

        elif cardtype == CardType.CANCEL_ALL:
            self.use_card_stats[4] += 1

        elif cardtype == CardType.INVEST:
            self.use_card_stats[5] += 1

        return self.judge.read_projects()

    def _apply_cards(self,next_cards,select_card_i):
        next_card = next_cards[select_card_i]
        cardtype,w,p = next_card

        for t,_,_ in next_cards[1:]:

            if t == CardType.WORK_SINGLE:
                self.card_freaqs[0] += 1
            elif t == CardType.WORK_ALL:
                self.card_freaqs[1] += 1
            elif t == CardType.CANCEL_SINGLE:
                self.card_freaqs[2] += 1
            elif t == CardType.CANCEL_ALL:
                self.card_freaqs[3] += 1
            else:
                self.card_freaqs[4] += 1

        if cardtype == CardType.WORK_SINGLE:
            if p == 0:
                self.bought_card_stats[0] += 1
            else:
                self.bought_card_stats[1] += 1
                self.bought_card_cost[1] += p

            self.card_gain += w - p

        elif cardtype == CardType.WORK_ALL:

            self.bought_card_stats[2] += 1
            self.bought_card_cost[2] += p

            self.card_gain += self.m * w - p


        elif cardtype == CardType.CANCEL_SINGLE:
            self.bought_card_stats[3] += 1
            self.bought_card_cost[3] += p

        elif cardtype == CardType.CANCEL_ALL:
            self.bought_card_stats[4] += 1
            self.bought_card_cost[4] += p

        elif cardtype == CardType.INVEST:
            self.bought_card_stats[5] += 1
            self.bought_card_cost[5] += p

    def _select_action(self,now_cards,now_projects,turn_left,invest_level):

        card_cand = [[] for i in range(5)]
        for i in range(self.n):
            t = now_cards[i][0]
            target = -1
            if t == CardType.WORK_SINGLE:
                target = 0

            elif t == CardType.WORK_ALL:
                target = 1
            
            elif t == CardType.CANCEL_SINGLE:
                target = 2
            
            elif t == CardType.CANCEL_ALL:
                target = 3

            elif t == CardType.INVEST:
                target = 4

            card_cand[target].append(i)
            
        # INVEST があれば使う
        if card_cand[4]:
            return (card_cand[4][0],0)

        replace_project_cand = []
        work_project_cand = []
        worst_cand = -1
        worst_gain = 0

        # h > v * 1.2 かつ h > 15 コスパが悪くターンも必要なものを間引く

        cutoff = self.get_cutoff_limit()
        for i in range(self.m):
            gain = now_projects[i][0] / now_projects[i][1]
            if (gain >= cutoff and now_projects[i][0] / (1<<invest_level) > 15):
                replace_project_cand.append(i)
                if worst_gain < gain:
                    worst_gain = gain
                    worst_cand = i
            else:
                work_project_cand.append(i)

        # CANCEL を使うか判定
        if card_cand[2] or card_cand[3]:

            if len(replace_project_cand) >= 0.75*self.m and card_cand[3]:
                return (card_cand[3][0],0)

            if card_cand[2] and worst_cand != -1:
                return (card_cand[2][0],worst_cand)

        # WORK_ALL を使うか
        # 達成予定のプロジェクトで 80%以上有効活用出来るか 無駄が大きいなら後で使う
        work_all_best = -1
        work_all_max = 0
        if work_project_cand and card_cand[1]:

            for work_all_ind in card_cand[1]:

                work_gain = 0
                work_all_m = now_cards[work_all_ind][1]

                for ind in work_project_cand:
                    work_gain += min(now_projects[ind][0],work_all_m)


                work_gain /= len(work_project_cand) * work_all_m

                if work_gain > work_all_max:
                    work_all_max = work_gain
                    work_all_best = work_all_ind
                
            if work_all_best != -1:
                
                if (work_all_max > 0.8 and len(work_project_cand)/self.m >= 0.5) or turn_left < 20 or (self.money < 50<<self.invest_level and work_all_max > 0.8):
                    return (work_all_best,0)


        next_project = -1
        next_gain = 0
        project_list = []
        for i in range(self.m):
            gain = now_projects[i][1] / now_projects[i][0]
            project_list.append([gain,i])
            if gain > next_gain:
                next_gain = gain
                next_project = i


        # 残りターンが少ないなら強い手札を積極的に使う
        if turn_left < 20:

            if card_cand[1]:
                work_all_best = -1
                work_all_max = 0
                for work_all_ind in card_cand[1]:
    
                    work_gain = 0
                    work_all_m = now_cards[work_all_ind][1]

                    for ind in range(self.m):
                        work_gain += min(now_projects[ind][0],work_all_m)


                    work_gain /= self.m * work_all_m

                    if work_gain > work_all_max:
                        work_all_max = work_gain
                        work_all_best = work_all_ind

                if work_all_best != -1:
                    return (work_all_best,0)


            if card_cand[0]:
                select_cand = []
                for card_ind in card_cand[0]:
                    card_m = now_cards[card_ind][1]

                    for work_ind in work_project_cand + [next_project]:
                        work_m = now_projects[work_ind][0]

                        turn = (work_m+card_m-1)//card_m
                        if card_m >= work_m:
                            select_cand.append([turn,card_m-work_m,card_ind,work_ind])

                        else:
                            select_cand.append([turn,work_m-card_m,card_ind,work_ind])

                # assert select_cand

                select_cand.sort()

                for turn,gain,card_ind,work_ind in select_cand:

                    if turn == 1:
                        return (card_ind,work_ind)

                    else:
                        return (card_ind,work_ind)

                # assert False


        # 達成したいプロジェクトがない時 
        if work_project_cand == []:
            # CANCEL ALL 出来るならしてしまう
            if card_cand[3]:
                return (card_cand[3][0],0)

            # CANCEL SINGLE はない
            # assert card_cand[2] == []

            # 弱い WORK SINGLE を使う
            work_single_ind = -1
            work_single_min = INF

            for ind in card_cand[0]:
                if now_cards[ind][1] < work_single_min:
                    work_single_min = now_cards[ind][1]
                    work_single_ind = ind

            
            if work_single_ind != -1:
                return (work_single_ind,next_project)

            # 弱い WORL ALL を使う            
            # assert card_cand[1]

            work_all_ind = -1
            work_all_min = INF

            for ind in card_cand[1]:
                if now_cards[ind][1] < work_all_min:
                    work_all_min = now_cards[ind][1]
                    work_all_ind = ind


            if work_all_ind != -1:
                return (work_all_ind,0)


            # assert False

        # WORK SINGLE がない時
        if card_cand[0] == []:

            # CANCEL ALL or WORK ALL しかない

            # WORK ALL があるなら使う
            if card_cand[1]:
                # assert work_all_best != -1

                return (work_all_best,0)
            
            if card_cand[2]:
                project_list.sort()
                return (card_cand[2][0],project_list[0][1])

            # CANCEL ALL を使う
            # assert card_cand[3],now_cards

            return (card_cand[3][0],0)


        # WORK SINGLE を使う
        # 必要ターンが短く 利用効率の良い WORK を選択

        select_cand = []
        for card_ind in card_cand[0]:
            card_m = now_cards[card_ind][1]

            for work_ind in work_project_cand:
                work_m = now_projects[work_ind][0]

                turn = (work_m+card_m-1)//card_m
                if card_m >= work_m:
                    select_cand.append([turn,card_m-work_m,card_ind,work_ind])

                else:
                    select_cand.append([turn,work_m-card_m,card_ind,work_ind])

        # assert select_cand

        select_cand.sort()

        for turn,gain,card_ind,work_ind in select_cand:

            if turn == 1:
                if gain < 3 << invest_level or gain < 0.25 * now_cards[card_ind][1]:
                    return (card_ind,work_ind)

                if self.k == 2:
                    continue

                if self.m <= 5 and now_projects[work_ind][0] > 3<<self.invest_level and gain < 0.5 * now_cards[card_ind][1]:
                    return (card_ind,work_ind)

                elif self.m > 5 and now_projects[work_ind][0] > 5<<self.invest_level and gain < 0.4 * now_cards[card_ind][1]:
                    return (card_ind,work_ind)

            else:
                return (card_ind,work_ind)

        return (select_cand[0][2],select_cand[0][3])
  

    def _select_next_card(self, next_cards,now_projects,turn_left,invest_level,money,playout=False):

        cand_invest = -1
        cand_min = INF

        can_buy_cards = []
        for i,(t,w,p) in enumerate(next_cards):
            if p <= money:
                can_buy_cards.append([i,t,w,p])


        # assert can_buy_cards

        work_cards = []

        cancel_single = []
        cancel_all = []

        card_now = [0]*5

        for i,t,w,p in can_buy_cards:
            
            if t == CardType.INVEST:

                if cand_min > p:
                    cand_min = p
                    cand_invest = i

            # WORK は gain が大きいものから購入を検討
            elif t == CardType.WORK_SINGLE:
                
                gain = w - p

                work_cards.append([-gain,i,t,w,p])

            elif t == CardType.WORK_ALL:
                gain = w*self.m - p

                work_cards.append([-gain-0.5,i,t,w,p])


            # CANCEL は random が 0 or 1 なら購入検討
            elif t == CardType.CANCEL_SINGLE:

                if (p >> invest_level) <= 1:
                    cancel_single.append([p,i,t,w,p])

            elif t == CardType.CANCEL_ALL:

                if (p >> invest_level) <= 1:
                    cancel_all.append([p,i,t,w,p])

        
        if cand_invest != -1 and invest_level < MAX_INVEST_LEVEL and playout == False:

            # if turn_left > 200:
            #     return cand_invest
            if turn_left > 150:# and (self.money-cand_min) > 20<<self.invest_level:
                return cand_invest


        replace_project_cand = []
        work_project_cand = []
        worst_cand = -1
        worst_gain = 0

        # h > v * 1.2 かつ h > 15 コスパが悪くターンも必要なものを間引く
        cutoff = self.get_cutoff_limit()
        for i in range(self.m):
            gain = now_projects[i][0] / now_projects[i][1]
            if gain >= cutoff and now_projects[i][0] / (1<<invest_level) > 15:
                replace_project_cand.append(i)

                if worst_gain < gain:
                    worst_gain = gain
                    worst_cand = i
            else:
                work_project_cand.append(i)


        # CANCEL したいプロジェクトが多いなら キャンセルを優先

        if cancel_all and len(replace_project_cand) >= 0.75*self.m:
            cancel_all.sort()
            return cancel_all[0][1]



        work_cards.sort()
        future_best_card = -1
        future_best_prob = 1

        gain_card_list = []
        # self.judge.comment(f"{work_cards} {work_project_cand}")
        for gain,i,t,w,p in work_cards:

            if p == 0:
                break

            if t == CardType.WORK_ALL and work_project_cand:
                work_gain = 0
                work_all_m = w
                until_gain_time = 0
                for ind in work_project_cand:
                    work_gain += min(now_projects[ind][0],work_all_m)
                    until_gain_time += 1 + (now_projects[ind][0]-w)//w * 2

                work_loss = work_all_m * len(work_project_cand) - work_gain
                work_gain /= len(work_project_cand) * self.m
                if work_gain > 0.8 and work_loss < -gain:

                    gain_card_list.append([i,work_gain,until_gain_time])
                

            elif t == CardType.WORK_SINGLE and work_project_cand:

                use_project = 0
                use_max = 0
                until_gain_time = INF
                for ind in work_project_cand:
                    if now_projects[ind][0] >= 0.8 * w:
                        until_gain_time = min(until_gain_time,1 + (now_projects[ind][0]-w)//w * 2)
                        use_project = 1
                        use_max = max(use_max,min(now_projects[ind][0],w))

                if use_project:
                    gain_card_list.append([i,use_max / w,until_gain_time])

            
            if t == CardType.WORK_SINGLE:
                rare = p / w

            elif t == CardType.WORK_ALL:
                rare = p / (self.m * w)

            
            if rare < 0.5 and future_best_card == -1:
                future_best_prob = rare
                future_best_card = i

        for now_best_card,now_best_gain,until_gain_time in gain_card_list:

            if until_gain_time > turn_left:
                continue

            if future_best_card == -1:
                return now_best_card

            if now_best_gain > 0.9 or future_best_prob > 0.3:
                return now_best_card

            # 終わりに近いと実利優先
            if turn_left < 50:
                return now_best_card

            if future_best_prob < 0.3:
                return future_best_card

            return now_best_card

        if future_best_card != -1 and future_best_prob < 0.5:
            return future_best_card
        # CANCEL を購入するか
        if cancel_single:

            if cancel_single and worst_cand != -1:
                cancel_single.sort()
                return cancel_single[0][1]

        ncard = -1
        ngain = -1
        for gain,i,t,w,p in work_cards:

            if p == 0:
                ncard = i
                ngain = p-w

            # if ngain == -1:
            #     continue

            # if t != CardType.WORK_SINGLE:
            #     continue

            
            # for work_ind in work_project_cand:
            #     if now_projects[work_ind][0] > w or now_projects[work_ind][0] < 0.7*w or now_projects[work_ind][0] < 20<<self.invest_level:
            #         continue

            #     plus = now_projects[work_ind][1] - p - (w-now_projects[work_ind][0])
            #     if plus > ngain:
            #         ngain = plus
            #         ncard = i





        return ncard

        
def main():
    n, m, k, t = map(int, input().split())


    solver = Solver(n, m, k, t)
    score = solver.solve()

if __name__ == "__main__":
    main()
