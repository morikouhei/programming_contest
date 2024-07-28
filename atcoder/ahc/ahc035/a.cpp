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
double time_limit = 1.9;
int atcoder = 0;
int n,m,t;
int m2;
int seed_count;
int board_num;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

vector<vector<int>> X;
vector<int> max_X;
vector<int> max_X_lim;

int score_iterate = 500;
// i,j と i,j+1 の mix のための 乱数 と
// i,j と i+1,j の mix のための 乱数 を用意
// score_iterate * n * n の 乱数テーブル
vector<vector<vector<int>>> rand_x(6, vector<vector<int>>(6, vector<int>(score_iterate)));
vector<vector<vector<int>>> rand_y(6, vector<vector<int>>(6, vector<int>(score_iterate)));
vector<vector<long long>> score_x(6, vector<long long>(6));
vector<vector<long long>> score_y(6, vector<long long>(6));
void Input() {
    // 環境変数に AtCoder があるかどうか
    if (getenv("ATCODER")) {
        atcoder = 1;
    }
    cin >> n >> m >> t;
    seed_count = 2 * n * (n-1);
    board_num = n*n;
    m2 = 1<<m;
    max_X = vector<int>(m, 0);
    max_X_lim = vector<int>(m, 0);
    X = vector<vector<int>>(seed_count, vector<int>(m, 0));
    for (int i = 0; i < seed_count; i++) {
        for (int j = 0; j < m; j++) {
            cin >> X[i][j];
            max_X[j] = max(max_X[j], X[i][j]);
        }
    }
    for (int i = 0; i < m; i++){
        max_X_lim[i] = (int) (max_X[i] * 0.85);
    
    }

};

struct State {
    vector<vector<int>> X_state;

    State(vector<vector<int>> X_state): X_state(X_state) {}
        
    int get_eval(int ind){
        int eval = 0;
        for (int i = 0; i < m; i++){
            eval += max_X[i] - X_state[ind][i];
            if (X_state[ind][i] == max_X[i]) eval -= 100;
            if (X_state[ind][i] >= max_X_lim[i]) eval -= 100;
        }
        return eval;
    }

    int get_eval_marge(int ind1, int ind2, int marge_bit){
        int eval = 0;
        for (int i = 0; i < m; i++){
            int x = ((marge_bit >> i) & 1) ? X_state[ind1][i] : X_state[ind2][i];

            eval += max_X[i] - x;
            
            if (x == max_X[i]) eval -= 100;
            if (x >= max_X_lim[i]) eval -= 100;
        }
        return eval;
    }


    void set(){
        for (int i = 0; i < seed_count; i++){
            for (int j = 0; j < m; j++){
                int x;
                cin >> x;
                X_state[i][j] = x;
            }
        }
    }


};

struct Solver {
    int turn = 0;

    int calc_score(){
        int score = 0;

        return score;

    }
    void print(vector<vector<int>> &board){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                cout << board[i][j] << " ";
            }
            cout << endl;
        }


    }
    vector<vector<int>> climbing(State &state, double turn_time_limit, vector<vector<int>> &board){
        double start_time = timer.get_time();

        long long base_score = 0;

        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                for (int k = 0; k < score_iterate; k++){
                    rand_x[i][j][k] = rng.randrange(m2);
                    rand_y[i][j][k] = rng.randrange(m2);
                }
            }
        }

        for (int x = 0; x < n; x++){
            for (int y = 0; y < n; y++){
                score_x[x][y] = 0;
                score_y[x][y] = 0;
                for (int k = 0; k < score_iterate; k++){
                    if (x < n-1){
                        score_x[x][y] += state.get_eval_marge(board[x][y], board[x+1][y], rand_x[x][y][k]);
                    }
                    if (y < n-1){
                        score_y[x][y] += state.get_eval_marge(board[x][y], board[x][y+1], rand_y[x][y][k]);
                    }
                }
                base_score += score_x[x][y] + score_y[x][y];
            }
        }

        vector<vector<int>> best_board = board;
        long long best_score = base_score;
        int iter = 0;

        double temp1 = 0.01;
        double temp2 = 0.00001;
        double temp = temp1;
        while (timer.get_time() - start_time < turn_time_limit){

            // board の 2点を swap して score を計算
            int ind1 = rng.randint(0, n*n-1);
            int ind2 = rng.randint(0, n*n-1);
            if (ind1 == ind2) continue;

            // exp の温度関数で temp を更新
            double progress = (timer.get_time() - start_time) / turn_time_limit;
            // temp = pow(temp1,1-progress) * pow(temp2,progress);
            temp = 0;

            
            iter++;

            int x1 = ind1 / n;
            int y1 = ind1 % n;
            int x2 = ind2 / n;
            int y2 = ind2 % n;

            long long dif_score = 0;
            // ind1,2 の周りのスコアの差分
            for (int i = 0; i < score_iterate; i++){
                if (x1 < n-1){
                    dif_score -= state.get_eval_marge(board[x1][y1], board[x1+1][y1], rand_x[x1][y1][i]);
                }
                if (x1 > 0){
                    dif_score -= state.get_eval_marge(board[x1-1][y1], board[x1][y1], rand_x[x1-1][y1][i]);
                }
                if (y1 < n-1){
                    dif_score -= state.get_eval_marge(board[x1][y1], board[x1][y1+1], rand_y[x1][y1][i]);
                }
                if (y1 > 0){
                    dif_score -= state.get_eval_marge(board[x1][y1-1], board[x1][y1], rand_y[x1][y1-1][i]);
                }

                if (x2 < n-1 && (x2+1 != x1 || y2 != y1)){
                    dif_score -= state.get_eval_marge(board[x2][y2], board[x2+1][y2], rand_x[x2][y2][i]);
                }
                if (x2 > 0 && (x2-1 != x1 || y2 != y1)){
                    dif_score -= state.get_eval_marge(board[x2-1][y2], board[x2][y2], rand_x[x2-1][y2][i]);
                }
                if (y2 < n-1 && (x2 != x1 || y2+1 != y1)){
                    dif_score -= state.get_eval_marge(board[x2][y2], board[x2][y2+1], rand_y[x2][y2][i]);
                }
                if (y2 > 0 && (x2 != x1 || y2-1 != y1)){
                    dif_score -= state.get_eval_marge(board[x2][y2-1], board[x2][y2], rand_y[x2][y2-1][i]);
                }
            }

            swap(board[x1][y1], board[x2][y2]);

            // ind1,2 の周りのスコアの差分
            for (int i = 0; i < score_iterate; i++){
                if (x1 < n-1){
                    dif_score += state.get_eval_marge(board[x1][y1], board[x1+1][y1], rand_x[x1][y1][i]);
                }
                if (x1 > 0){
                    dif_score += state.get_eval_marge(board[x1-1][y1], board[x1][y1], rand_x[x1-1][y1][i]);
                }
                if (y1 < n-1){
                    dif_score += state.get_eval_marge(board[x1][y1], board[x1][y1+1], rand_y[x1][y1][i]);
                }
                if (y1 > 0){
                    dif_score += state.get_eval_marge(board[x1][y1-1], board[x1][y1], rand_y[x1][y1-1][i]);
                }

                if (x2 < n-1 && (x2+1 != x1 || y2 != y1)){
                    dif_score += state.get_eval_marge(board[x2][y2], board[x2+1][y2], rand_x[x2][y2][i]);
                }
                if (x2 > 0 && (x2-1 != x1 || y2 != y1)){
                    dif_score += state.get_eval_marge(board[x2-1][y2], board[x2][y2], rand_x[x2-1][y2][i]);
                }
                if (y2 < n-1 && (x2 != x1 || y2+1 != y1)){
                    dif_score += state.get_eval_marge(board[x2][y2], board[x2][y2+1], rand_y[x2][y2][i]);
                }
                if (y2 > 0 && (x2 != x1 || y2-1 != y1)){
                    dif_score += state.get_eval_marge(board[x2][y2-1], board[x2][y2], rand_y[x2][y2-1][i]);
                }   
            }

            if (dif_score < 0 || rng.random() < exp(-dif_score / temp)){
                if (base_score + dif_score < best_score){
                    best_score = base_score + dif_score;
                    best_board = board;
                }
                base_score += dif_score;

            } else {
                swap(board[x1][y1], board[x2][y2]);
            }
            
        }
        cerr << "iter: " << iter << " best_score: " << best_score << " base_score: " << base_score << endl;

        return best_board;
    }

    void solve() {
        
        State state = State(X);

        

        // 渦巻きに配置
        vector<vector<int>> board(n, vector<int>(n, -1));
        int x = 0, y = 0;
        int dir = 0;
        vector<pair<int,int>> put_pos;
        for (int i = 0; i < board_num; i++){
            put_pos.push_back({x,y});
            board[x][y] = 0;
            for (int count = 0; count < 4; count++){
                int nx = x + dx[dir];
                int ny = y + dy[dir];
                if (nx < 0 || nx >= n || ny < 0 || ny >= n || board[nx][ny] != -1){
                    dir = (dir + 1) % 4;
                } else {
                    x = nx;
                    y = ny;
                    break;
                }
            }    
        }
        
        reverse(put_pos.begin(), put_pos.end());
        
        for (int turn = 0; turn < t; turn++){

            vector<pair<int,int>> evals;
            for (int i = 0; i < seed_count; i++){
                evals.push_back({state.get_eval(i), i});
            }
            sort(evals.begin(), evals.end());
            vector<vector<int>> board(n, vector<int>(n, -1));
            for (int i = 0; i < board_num; i++){
                int x = put_pos[i].first;
                int y = put_pos[i].second;
                board[x][y] = evals[i].second;
            }
            double turn_time_limit = timer.time_left(time_limit) / (t-turn);

            cerr << "turn = " << turn << " turn_time_limit = " << turn_time_limit << endl;
            board = climbing(state, turn_time_limit, board);

            print(board);
            state.set();
        }

        int score = calc_score();
        // cerr << "end at " << timer.get_time() << "sec" << endl;
        // cerr << "score: " << score << endl;
    }

};

int main() {
    Input();
    Solver solver = Solver();
    solver.solve();
    return 0;
}