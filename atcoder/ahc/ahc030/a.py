import random
import time
import sys
import os
import math

random.seed(998244353)
TIME_LIM = 3
INF = 1e9
stime = time.time()


DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]


# 正規分布の累積分布関数 (CDF)
def normal_cdf(x, mean, variance):
    z = (x - mean) / math.sqrt(variance)
    return (1 + math.erf(z / math.sqrt(2))) / 2


# 指定された区間内の確率を計算する関数
def probability_in_interval(start, end, mean, variance):
    return normal_cdf(end, mean, variance) - normal_cdf(start, mean, variance)


memo = {}


def get_normal_dist_interval(now_num, now_res, k):
    if (now_num, now_res) in memo:
        return memo[(now_num, now_res)]

    mu = (k - now_num) * eps + now_num * (1.0 - eps)
    sigma = k * eps * (1.0 - eps)
    # print(now_num, now_res, k)
    if now_res == 0:
        prob = normal_cdf(0.5, mu, sigma)

    else:
        prob = probability_in_interval(now_res - 0.5, now_res + 0.5, mu, sigma)
    # print(prob)
    # print(now_num, now_res, k, mu, sigma)
    if prob:
        prob = math.log(prob)
    else:
        prob = -100
    memo[(now_num, now_res)] = prob

    print("#c prob res = ", now_num, now_res, k, mu, sigma, prob)

    return prob


class Block:

    def __init__(self, l):
        self.block_size = l[0]
        self.max_x = 0
        self.max_y = 0

        self.block_list = []
        for i in range(self.block_size):
            x, y = l[2 * i + 1], l[2 * i + 2]
            self.block_list.append([x, y])
            self.max_x = max(x, self.max_x)
            self.max_y = max(y, self.max_y)


n, m, eps = input().split()
n = int(n)
m = int(m)
eps = float(eps)
Blocks = []
Block_sum = 0
n2 = n * n
atcoder = 0
if os.getenv("ATCODER"):
    atcoder = 1
for i in range(m):
    l = list(map(int, input().split()))
    Block_sum += l[0]
    Blocks.append(Block(l))


class Environment:

    def __init__(self):
        self.query_time = 0
        self.Block_pos_list = []
        self.V = []
        self.oil_num = 0
        self.errors = []
        self.cost = 0

        self._build()

    def _build(self):

        if atcoder:
            return

        for i in range(m):
            x, y = map(int, input().split())
            self.Block_pos_list.append([x, y])

        self.V = [list(map(int, input().split())) for i in range(n)]

        for v in self.V:
            for x in v:
                if x:
                    self.oil_num += 1

        self.errors = [float(input()) for i in range(2 * n2)]

    def ask_query(self, ask_list):

        self.query_time += 1

        assert self.query_time <= 2 * n2

        k = len(ask_list)
        if k == 1:
            self.cost += 1
        else:
            self.cost += 1 / (k) ** 0.5

        query = ["q", k]

        for x, y in ask_list:
            query.append(x)
            query.append(y)

            assert 0 <= x < n and 0 <= y < n

        print(*query)
        sys.stdout.flush()

        if atcoder:
            res = int(input())

        else:
            if k == 1:

                x, y = ask_list[0]

                res = self.V[x][y]

            else:
                count = 0
                for x, y in ask_list:
                    count += self.V[x][y]

                mu = (k - count) * eps + count * (1.0 - eps)
                sigma = (k * eps * (1.0 - eps)) ** 0.5

                res = max(round(mu + self.errors[self.query_time - 1] * sigma), 0)

        # self.comment(query + [" res = " + str(res)])
        return res

    def answer_query(self, ans_list):

        self.query_time += 1

        assert self.query_time <= 2 * n2

        k = len(ans_list)

        # self.cost += 1

        query = ["a", k]

        for x, y in ans_list:
            query.append(x)
            query.append(y)

            assert 0 <= x < n and 0 <= y < n

        print(*query)
        sys.stdout.flush()

        if atcoder:
            res = int(input())

        else:

            if k != self.oil_num:
                res = 0

            else:
                res = 1
                for x, y in ans_list:
                    if self.V[x][y] == 0:
                        res = 0

        if res:
            self.out_score()
            exit()

        self.cost += 1
        return res

    def comment(self, comment):
        # comment = "#c " + comment
        print("#c", comment)

    def out_score(self):
        cost = round(10**6 * max(1 / n, self.cost))
        self.comment(time.time() - stime)
        self.comment(f"cost = {cost}")


environment = Environment()


class State:

    def __init__(self):
        self.query_time = 0
        self.query_cost = 0
        self.query_size = 4
        self.query_info_list = [[[] for i in range(n)] for j in range(n)]
        self.V_fixed = [[-1] * n for i in range(n)]

        self.state = [[0] * n for i in range(n)]
        self.state_changes = [[0] * n for i in range(n)]
        self.state_pena = [[0] * n for i in range(n)]

        self.query_weight = []
        self.query_ans = []
        self.query_list = []
        self.query_changes = []
        self.block_pos_list = []
        self.query_score = []

        self.score = 0

        self._build()

    def can_put_block(self, ind, x, y):

        block = Blocks[ind]
        if block.max_x + x >= n or block.max_y + y >= n or x < 0 or y < 0:
            return 0

        return 1

    def get_state_pena(self, state, x, y):
        if self.V_fixed[x][y] == -1:
            return 0

        if self.V_fixed[x][y] == 0 and state:
            return -state * 1000
        return -abs(self.V_fixed[x][y] - state) * 100

    def query(self, query):

        self.query_time += 1
        k = len(query)
        if k == 1:
            self.query_cost += 1
        else:
            self.query_cost += 1 / k**0.5

        res = environment.ask_query(query)

        return res

    def _build(self):

        query_size = self.query_size

        for bdif in [0,2]:

            for i in range(n):

                if i * query_size + bdif >= n:
                    break

                for j in range(n):

                    if j * query_size + bdif >= n:
                        break

                    lx = i * query_size + bdif
                    rx = i * query_size + query_size + bdif

                    if rx > n:
                        dif = rx - n
                        lx -= dif
                        rx -= dif

                    ly = j * query_size + bdif
                    ry = j * query_size + query_size + bdif

                    if ry > n:
                        dif = ry - n
                        ly -= dif
                        ry -= dif

                    query = []
                    for x in range(lx, rx):
                        for y in range(ly, ry):
                            query.append([x, y])
                            self.query_info_list[x][y].append(self.query_time)

                    res = self.query(query)

                    self.query_ans.append(res)
                    self.query_weight.append(0)
                    self.query_list.append(query)
                    self.query_changes.append(0)

        for ind in range(m):

            while True:
                x = random.randint(0, n - 1)
                y = random.randint(0, n - 1)

                if self.can_put_block(ind, x, y):
                    self.block_pos_list.append([x, y])
                    break

            for nx, ny in Blocks[ind].block_list:
                self.state[x + nx][y + ny] += 1

        for i, (query) in enumerate(self.query_list):
            count = 0
            for x, y in query:
                count += self.state[x][y]

            self.query_weight[i] = count

            prob = get_normal_dist_interval(
                count, self.query_ans[i], self.query_size**2
            )
            self.query_score.append(prob)
            self.score += prob

    def get_change_info(self, query_change, state_change):
        score_dif = 0
        query_changes = []
        for qind in query_change:
            if self.query_changes[qind] == 0:
                continue

            nweight = self.query_weight[qind] + self.query_changes[qind]

            nprob = get_normal_dist_interval(
                nweight, self.query_ans[qind], self.query_size**2
            )

            score_dif += nprob - self.query_score[qind]
            query_changes.append([qind, nweight, nprob])

            self.query_changes[qind] = 0

        state_changes = []

        for px, py in state_change:
            if self.state_changes[px][py] == 0:
                continue

            nstate = self.state[px][py] + self.state_changes[px][py]
            npena = self.get_state_pena(nstate, px, py)
            score_dif += npena - self.state_pena[px][py]
            state_changes.append([[px, py], nstate, npena])

            self.state_changes[px][py] = 0

        return score_dif, query_changes, state_changes

    ## block1つをrandomに移動
    def neighbor1(self):

        bind = random.randint(0, m - 1)

        block = Blocks[bind]

        x, y = self.block_pos_list[bind]

        nx = random.randint(0, n - 1)
        ny = random.randint(0, n - 1)

        if x == nx and y == ny:
            return INF, []

        if not self.can_put_block(bind, nx, ny):
            return INF, []

        query_change = set()
        state_change = set()

        for bx, by in block.block_list:

            for qind in self.query_info_list[x + bx][y + by]:
                query_change.add(qind)
                self.query_changes[qind] -= 1

            self.state_changes[x + bx][y + by] -= 1
            state_change.add((x + bx, y + by))

            for qind in self.query_info_list[nx + bx][ny + by]:
                query_change.add(qind)
                self.query_changes[qind] += 1

            self.state_changes[nx + bx][ny + by] += 1
            state_change.add((nx + bx, ny + by))

        score_dif, query_changes, state_changes = self.get_change_info(
            query_change, state_change
        )

        return score_dif, [[[bind, [nx, ny]]], query_changes, state_changes]

    ## block2つをswap
    def neighbor2(self):

        bind1 = random.randint(0, m - 1)
        bind2 = random.randint(0, m - 1)

        if bind1 == bind2:
            return INF, []

        block1 = Blocks[bind1]
        block2 = Blocks[bind2]

        x, y = self.block_pos_list[bind1]
        nx, ny = self.block_pos_list[bind2]

        if not self.can_put_block(bind1, nx, ny):
            return INF, []

        if not self.can_put_block(bind2, x, y):
            return INF, []

        query_change = set()
        state_change = set()

        for bx, by in block1.block_list:

            for qind in self.query_info_list[x + bx][y + by]:
                query_change.add(qind)
                self.query_changes[qind] -= 1

            self.state_changes[x + bx][y + by] -= 1
            state_change.add((x + bx, y + by))

            for qind in self.query_info_list[nx + bx][ny + by]:
                query_change.add(qind)
                self.query_changes[qind] += 1

            self.state_changes[nx + bx][ny + by] += 1
            state_change.add((nx + bx, ny + by))

        for bx, by in block2.block_list:

            for qind in self.query_info_list[x + bx][y + by]:
                query_change.add(qind)
                self.query_changes[qind] += 1

            self.state_changes[x + bx][y + by] += 1
            state_change.add((x + bx, y + by))

            for qind in self.query_info_list[nx + bx][ny + by]:
                query_change.add(qind)
                self.query_changes[qind] -= 1

            self.state_changes[nx + bx][ny + by] -= 1
            state_change.add((nx + bx, ny + by))

        score_dif, query_changes, state_changes = self.get_change_info(
            query_change, state_change
        )

        return score_dif, [
            [[bind1, [nx, ny]], [bind2, [x, y]]],
            query_changes,
            state_changes,
        ]

    ## block1つを隣接に移動
    def neighbor3(self):

        bind = random.randint(0, m - 1)

        block = Blocks[bind]

        x, y = self.block_pos_list[bind]

        dir = random.randint(0, 3)
        nx = x + DX[dir]
        ny = y + DY[dir]

        if not self.can_put_block(bind, nx, ny):
            return INF, []

        query_change = set()
        state_change = set()

        for bx, by in block.block_list:

            for qind in self.query_info_list[x + bx][y + by]:
                query_change.add(qind)
                self.query_changes[qind] -= 1

            self.state_changes[x + bx][y + by] -= 1
            state_change.add((x + bx, y + by))

            for qind in self.query_info_list[nx + bx][ny + by]:
                query_change.add(qind)
                self.query_changes[qind] += 1

            self.state_changes[nx + bx][ny + by] += 1
            state_change.add((nx + bx, ny + by))

        score_dif, query_changes, state_changes = self.get_change_info(
            query_change, state_change
        )

        return score_dif, [[[bind, [nx, ny]]], query_changes, state_changes]

    def apply_query_res(self, res, x, y):
        self.V_fixed[x][y] = res
        self.score -= self.state_pena[x][y]
        self.state_pena[x][y] = self.get_state_pena(self.state[x][y], x, y)
        self.score += self.state_pena[x][y]

    def update_state(self, score_dif, update_info):

        self.score += score_dif

        block_changes, query_changes, state_changes = update_info

        for bind, nex in block_changes:
            self.block_pos_list[bind] = nex

        for qind, nweight, nprob in query_changes:
            self.query_weight[qind] = nweight
            self.query_score[qind] = nprob

        for nex, nstate, npena in state_changes:
            nx, ny = nex
            self.state[nx][ny] = nstate
            self.state_pena[nx][ny] = npena

    def query_choice(self):

        rand_list2 = []
        rand_list = [[] for i in range(5)]
        for i in range(n):
            for j in range(n):
                if self.V_fixed[i][j] != -1:
                    continue
                if self.state[i][j] == 0:
                    continue

                rand_list2.append([i, j])
                zero_num = 0
                for dx, dy in zip(DX, DY):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n and self.state[nx][ny] > 0:
                        continue
                    zero_num += 1
                rand_list[zero_num].append([i, j])

        # if rand_list2:
        #     return rand_list2[random.randint(0, len(rand_list2) - 1)]

        for i in range(5)[::-1]:
            if rand_list[i] == []:
                continue

            return rand_list[i][random.randint(0, len(rand_list[i]) - 1)]

        return self.greedy_choice()

    def state_log(self):
        for i in range(n):
            for j in range(n):
                v = self.V_fixed[i][j]
                s = self.state[i][j]

                if v == -1:
                    if s > 0:
                        environment.comment(f"{i} {j} green")
                    else:
                        environment.comment(f"{i} {j} white")

                elif v > 0:
                    environment.comment(f"{i} {j} red")
                else:
                    environment.comment(f"{i} {j} blue")

    def try_ans(self):
        ans_list = []
        for i in range(n):
            for j in range(n):
                v = self.V_fixed[i][j]
                s = self.state[i][j]

                if v != -1 and v != s:
                    return

                if s:
                    ans_list.append([i, j])

        res = environment.answer_query(ans_list)

        self.query_cost += 1
        self.query_time += 1

    def can_put_block_greedy(self, ind, x, y):
        block = Blocks[ind]
        if block.max_x + x >= n or block.max_y + y >= n:
            return 0

        for nx, ny in block.block_list:
            if self.V_fixed[x + nx][y + ny] == 0:
                return 0

        return 1

    def apply_block_greedy(self, ind, x, y, weight_list):
        block = Blocks[ind]

        size = block.block_size

        use_num = 0
        for nx, ny in block.block_list:
            if self.V_fixed[x + nx][y + ny] > 0:
                use_num += 1

        if use_num == size:
            return

        psize = size * (size / (size - use_num))

        for nx, ny in block.block_list:
            if self.V_fixed[x + nx][y + ny] == -1:
                weight_list[x + nx][y + ny] += psize

        return weight_list

    def greedy_choice(self):

        weight_list = [[0] * n for i in range(n)]
        for bind in range(m):

            for x in range(n):
                for y in range(n):
                    if self.can_put_block_greedy(bind, x, y) == 0:
                        continue
                    self.apply_block_greedy(bind, x, y, weight_list)

        weight_max = 0
        pos = [-1, -1]

        for x in range(n):
            for y in range(n):

                weight = weight_list[x][y]

                if weight > weight_max:
                    weight_max = weight
                    pos = [x, y]

        assert weight_max

        return pos


class Climbing:

    def __init__(self):
        self.state = State()
        # exit()

    def solve(self):

        find_oil_sum = 0

        ans_list = []

        for turn in range(2 * n2):

            for i in range(10000):
                rand = random.randint(0, 99)

                if rand <= 50:
                    score_dif, update_info = self.state.neighbor3()

                elif rand <= 80:
                    score_dif, update_info = self.state.neighbor1()

                elif rand <= 100:
                    score_dif, update_info = self.state.neighbor2()

                if score_dif == INF:
                    continue

                if score_dif >= 0:
                    self.state.update_state(score_dif, update_info)

            self.state.state_log()

            if turn % n == 0:
                self.state.try_ans()

            x, y = self.state.query_choice()
            res = self.state.query([[x, y]])

            environment.comment(self.state.score)
            find_oil_sum += res
            if res:
                ans_list.append([x, y])
            self.state.apply_query_res(res, x, y)

            if find_oil_sum == Block_sum:
                res = environment.answer_query(ans_list)


solver = Climbing()
solver.solve()
