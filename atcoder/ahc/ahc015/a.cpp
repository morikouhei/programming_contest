#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

#include <cstring>
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cmath>
#include <complex>
#include <deque>
#include <forward_list>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <optional>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#include <cstdint>
using namespace std;

class Xorshift {
    public:
        Xorshift(uint32_t seed): x_(seed) {
            // assert(seed);
        }

        uint32_t randrange(uint32_t stop) {
            // [0, stop)
            // assert(stop > 0);
            next();
            return x_ % stop;
        }

        uint32_t randrange(uint32_t start, uint32_t stop) {
            // [start, stop)
            // assert(start < stop);
            next();
            return start + x_ % (stop - start);
        }

        uint32_t randint(uint32_t a, uint32_t b) {
            // [a, b]
            // assert(a <= b);
            return randrange(a, b + 1);
        }

        double random() {
            // [0.0, 1.0]
            next();
            return static_cast<double>(x_) * (1.0 / static_cast<double>(UINT32_MAX));
        }

        double uniform(double a, double b) {
            // [a, b] or [b, a]
            return a + (b - a) * random();
        }

    private:
        void next() {
            x_ ^= x_ << 13;
            x_ ^= x_ >> 17;
            x_ ^= x_ << 5;
        }

        uint32_t x_;
};

class Timer {
    public:
        Timer() {
            begin();
            elapsed_time_ = 0.0;
        }

        void begin() {
            start_time_ = chrono::system_clock::now();
        }

        double get_time() {
            chrono::system_clock::time_point end_time = chrono::system_clock::now();
            elapsed_time_ = chrono::duration_cast<chrono::nanoseconds>(end_time - start_time_).count();
            elapsed_time_ *= 1e-9; // nanoseconds -> seconds
            return elapsed_time_;
        }

        double get_last_time() const {
            return elapsed_time_;
        }

        double time_left(double time_limit) {
            return time_limit - get_time();
        }

        bool yet(double time_limit) {
            return get_time() < time_limit;
        }

        double progress(double time_limit) {
            return get_time() / time_limit;
        }

    private:
        chrono::system_clock::time_point start_time_;
        double elapsed_time_;
};

Xorshift rng(100);
Timer timer;
double time_limit = 1.99;
constexpr int EMPTY = 0;
int n = 10;
int n2 = n*n;
int TURN = 100;
int SIMULATE_MAX = 2000;
int SIMULATE_MIN = 500;
vector<vector<int>> random_simulate = vector<vector<int>>(SIMULATE_MAX, vector<int>(TURN));
vector<vector<int>> edges(n2);
int atcoder = 0;
string DIR = "FBLR";
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

vector<int> F(n2);
vector<int> visited(n2, 0);
int vis_count = 0;

int weight_sum = 0;
int candy_count[] = {0,0,0,0};
char state[100];

void Input() {
    // 環境変数に AtCoder があるかどうか
    if (getenv("ATCODER")) {
        atcoder = 1;
    }
    for (int i = 0; i < TURN; i++) {
        cin >> F[i];
        candy_count[F[i]]++;
    }
    for (int i = 1; i <= 3; i++) {
        weight_sum += candy_count[i] * candy_count[i];
    }

    for (int i = 0; i < SIMULATE_MAX; i++){
        for (int j = 0; j < TURN; j++){
            random_simulate[i][j] = rng.randrange(TURN-j);
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            int ind = i * n + j;
            for (int dir = 0; dir < 4; dir++){
                int ni = i + dx[dir];
                int nj = j + dy[dir];
                if (0 <= ni && ni < n && 0 <= nj && nj < n){
                    edges[ind].push_back(ni * n + nj);
                }
            }
        }
    }

};

struct Environment {
    vector<int> put_pos;
    int turn = 0;

    Environment() {
        put_pos = vector<int>(n2, 0);
        _init();
    }

    void _init() {
        if (!atcoder) {
            for (int i = 0; i < TURN; i++) {
                cin >> put_pos[i];
            }
        }
    }

    int get_res(){
        int res;
        assert (turn < TURN);
        if (atcoder) {
            cin >> res;
        } else {
            res = put_pos[turn];
        }
        turn++;
        res--;
        return res;
    }
    void out_res(char res){
        cout << res << endl;
    }

};

struct Solver {
    int turn = 0;
    Environment env;
    vector<char> select_dirs;

    int set(int ind, int candy){
        for (int i = 0; i < n2; i++){
            if (state[i] == EMPTY){
                if (ind == 0){
                    state[i] = candy;
                    return i;
                }
                ind--;
            }
        }
        return -1;
    }

    void move(char dir){
        // state を dir に従って移動する
        if (dir == 'F'){
            for (int i = 0; i < n; i++){
                int id = i;
                int nid = i;
                for (int j = 0; j < n; j++){
                    if (state[id] != EMPTY){
                        swap(state[id], state[nid]);
                        nid += n;
                    }
                    id += n;
                }
            }
        } else if (dir == 'B'){
            for (int i = 0; i < n; i++){
                int id = i + n * (n - 1);
                int nid = i + n * (n - 1);
                for (int j = n - 1; j >= 0; j--){
                    if (state[id] != EMPTY){
                        swap(state[id], state[nid]);
                        nid -= n;
                    }
                    id -= n;
                }
            }
        } else if (dir == 'L'){
            for (int i = 0; i < n; i++){
                int id = i * n;
                int nid = i * n;
                for (int j = 0; j < n; j++){
                    if (state[id] != EMPTY){
                        swap(state[id], state[nid]);
                        nid++;
                    }
                    id++;
                }
            }
        } else if (dir == 'R'){
            for (int i = 0; i < n; i++){
                int id = i * n + n - 1;
                int nid = i * n + n - 1;
                for (int j = n - 1; j >= 0; j--){
                    if (state[id] != EMPTY){
                        swap(state[id], state[nid]);
                        nid--;
                    }
                    id--;
                }
            }
        }
    }

    void move_only(char dir, int ind){
        int x = ind / n;
        int y = ind % n;
        if (dir == 'F'){
            for (int i = 0; i < x; i++){
                if (state[i*n+y] == EMPTY){
                    swap(state[i*n+y], state[ind]);
                    return;
                }
            }
        } else if (dir == 'B'){
            for (int i = n-1; i >= x; i--){
                if (state[i*n+y] == EMPTY){
                    swap(state[i*n+y], state[ind]);
                    return;
                }
            }
        } else if (dir == 'L'){
            for (int i = 0; i < y; i++){
                if (state[x*n+i] == EMPTY){
                    swap(state[x*n+i], state[ind]);
                    return;
                }
            }
        } else if (dir == 'R'){
            for (int i = n-1; i >= y; i--){
                if (state[x*n+i] == EMPTY){
                    swap(state[x*n+i], state[ind]);
                    return;
                }
            }
        }
    }

    int calc_score(){
        int score = 0;
        vis_count++;
        vector<int> q;
        for (int x = 0; x < n2; x++){
            if (visited[x] == vis_count) continue;
            auto candy = state[x];
            // state[x][y] = candy の連結成分を探す
            q.push_back(x);
            visited[x] = vis_count;
            int cnt = 1;
            while (!q.empty()){
                auto i = q.back();
                q.pop_back();
                for (auto j : edges[i]){
                    if (state[j] == candy && visited[j] != vis_count){
                        visited[j] = vis_count;
                        q.push_back(j);
                        cnt++;
                    }
                }
            }
            score += cnt * cnt;
            
        }
        return score;

    }
    void print(){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                cerr << static_cast<int>(state[i*n+j]);
            }
            cerr << endl;
        }
    }

    char greedy_select(int turn,vector<char> select_list){

        // 次のturnの F[i] に対して, select_listの対応する方向を選択する
        if (turn >= TURN-1) {
            return 'F';
        }

        if (select_list[F[turn+1]] == 'F'){
            return 'F';
        }
        if (select_list[F[turn]] == 'F'){
            return select_list[0];
        }

        if (F[turn] == F[turn+1] && select_dirs.size() && select_dirs.back() == select_list[F[turn]]){
            return select_list[0];
        }
        
        return select_list[F[turn+1]];
    }

    char monte_carlo_select(int turn, vector<char> select_list, double time_turn){
        vector<long long> score(4, 0);
        double timer_start = timer.get_time();
        int simulate_count = 0;
        cerr << "turn = " << turn << endl;
        int simulate_max = (turn < 30) ? 750:250;
        int simulate_min = 500;
        vector<int> is_skip(4);

        char base_state[100];
        memcpy(base_state, state, sizeof(base_state));
        // while (simulate_count < simulate_max){
        while (simulate_count < simulate_max || timer.get_time() - timer_start < time_turn){
            
            for (int i = 0; i < 4; i++){
                // if (is_skip[i]) continue;
                move(DIR[i]);
                select_dirs[turn] = DIR[i];
                for (int j = turn+1; j < TURN; j++){
                    int ind = set(random_simulate[simulate_count][j], F[j]);
                    if (select_dirs[j] == select_dirs[j-1]){
                        move_only(select_dirs[j], ind);
                    } else {
                        move(select_dirs[j]);
                    }
                    // move(select_dirs[j]);
                }
                score[i] += calc_score();
                memcpy(state, base_state, sizeof(state));
            }
            simulate_count++;
           
        }

        long long max_score = -1;
        char max_dir = 'F';
        for (int i = 0; i < 4; i++){
            if (score[i] > max_score){
                max_score = score[i];
                max_dir = DIR[i];
            }
        }


        cerr << "simulate_count: " << simulate_count << " max_score: " << (double)max_score/simulate_count << " max_dir: " << max_dir << endl;
        return max_dir;
    }

    vector<char> decide_select_list(){
        // select_list を 6通り試す
        // F,L,R を入れ替える
        vector<char> select_list = {'B', 'F', 'L', 'R'};
        vector<int> select_list_score(6, 0);
        int loop_turn = 100;

        int max_score = -1;
        vector<char> best_select_list;
        char base_state[100];
        memset(base_state, EMPTY, sizeof(base_state));
        for (int i = 0; i < 6; i++){
            select_list = {'B', 'F', 'L', 'R'};
            if (i & 1) swap(select_list[1], select_list[2]);
            if (i & 2) swap(select_list[1], select_list[3]);
            if (i & 4) swap(select_list[2], select_list[3]);

            for (int j = 0; j < TURN; j++){
                char dir = greedy_select(j, select_list);
                select_dirs.push_back(dir);
            }
            for (int j = 0; j < loop_turn; j++){
                for (int k = 0; k < TURN; k++){
                    int ind = set(random_simulate[j][k], F[k]);
                    if (k && select_dirs[k] == select_dirs[k-1]){
                        move_only(select_dirs[k], ind);
                    } else {
                        move(select_dirs[k]);
                    }
                    // move(select_dirs[k]);
                }
                select_list_score[i] += calc_score();
                
                memcpy(state, base_state, sizeof(base_state));
            }
            select_dirs.clear();
            if (select_list_score[i] > max_score){
                max_score = select_list_score[i];
                best_select_list = select_list;
            }
        }

        return best_select_list;


    }
    void solve() {
        memset(state, EMPTY, sizeof(state));
        vector<char> select_list = decide_select_list();
        while (turn < TURN) {
            char dir = greedy_select(turn, select_list);
            select_dirs.push_back(dir);
            turn++;
        }

        turn = 0;
        // dir を モンテカルロで探索
        while (turn < TURN-1) {
            // ターンの time limit を決める
            double rate = (double)(n2 + 10 - turn) / ((n2 - turn) * (n2 + 21 - turn) / 2);
            double time_turn = timer.time_left(time_limit) * rate;
            int ind = env.get_res();
            set(ind, F[turn]);
            char dir = monte_carlo_select(turn, select_list, time_turn);
            select_dirs[turn] = dir;
            move(dir);
            env.out_res(dir);
            turn++;

        }
        set(0, F[turn+1]);
        env.out_res('F');

        int score = calc_score();
        cerr << "end at " << timer.get_time() << "sec" << endl;
        cerr << "score: " << score << endl;
    }

};

int main() {
    Input();
    Solver solver = Solver();
    solver.solve();
    return 0;
}