#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

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
using namespace std;

const int INF = 1e5;

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

Xorshift rng(998244353);
Timer timer;
double time_limit = 1.95;

int n;
long long base = 0;
int compress = 5;
int compress2 = 25;
vector<vector<int>> H;
vector<int> H_flat;
vector<int> H_flat_compress;
vector<int> X,Y;
vector<int> X_compress,Y_compress;
vector<vector<int>> dist;
vector<vector<int>> dist_compress;
vector<int> recocd_order;
// RDLU 用の配列
const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};
const char dir[4] = {'R', 'D', 'L', 'U'};


// DRUL 用の配列
const int rdx[4] = {1, 0, -1, 0};
const int rdy[4] = {0, 1, 0, -1};
const char rdir[4] = {'D', 'R', 'U', 'L'};

void Input() {
    cin >> n;
    H.resize(n, vector<int>(n));
    H_flat.resize(n*n);
    recocd_order.resize(5000);
    // compress マスをまとめて圧縮する
    H_flat_compress.resize(n*n/compress2);

    X.resize(n*n);
    Y.resize(n*n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> H[i][j];
            base += abs(H[i][j]);
            H_flat[i*n+j] = H[i][j];
            H_flat_compress[(i*n+j)/compress2] += H[i][j];
            
        }
    }
    for (int i = 0; i < n*n; i++){
        X[i] = i / n;
        Y[i] = i % n;
    }
    for (int i = 0; i < n; i+= compress){
        for (int j = 0; j < n; j+= compress){
            int pos = i*n+j;
            X_compress.push_back(i);
            Y_compress.push_back(j);
        }
    }

    dist.resize(n*n, vector<int>(n*n, INF));
    for (int i = 0; i < n*n; i++){
        for (int j = 0; j < n*n; j++){
            dist[i][j] = abs(X[i] - X[j]) + abs(Y[i] - Y[j]);
        }
    }

    dist_compress.resize(n*n/compress2, vector<int>(n*n/compress2, INF));
    for (int i = 0; i < n*n/compress2; i++){
        for (int j = 0; j < n*n/compress2; j++){
            dist_compress[i][j] = abs(X_compress[i] - X_compress[j]) + abs(Y_compress[i] - Y_compress[j]);
        }
    }
};

// grid の訪問順を state にする
struct State {
    vector<int> order;
    int order_end = 0;
    long long score;

    vector<int> best_order;
    long long best_score = 1e18;
    int best_order_end;

    State() {
        // 初期解を作る
        // 複数試して１番良いものを選ぶ

        // 中心に向かって渦巻きに見ていく
        {
            int x = 0, y = 0;
            int dir = 0;
            vector<vector<bool>> visited(n, vector<bool>(n));
            vector<int> temp_order;
            while (true){
                temp_order.push_back(x*n+y);
                visited[x][y] = true;
                if (0 <= x+dx[dir] && x+dx[dir] < n && 0 <= y+dy[dir] && y+dy[dir] < n && !visited[x+dx[dir]][y+dy[dir]]){
                    x += dx[dir];
                    y += dy[dir];
                } else {
                    dir = (dir + 1) % 4;
                    if (0 <= x+dx[dir] && x+dx[dir] < n && 0 <= y+dy[dir] && y+dy[dir] < n && !visited[x+dx[dir]][y+dy[dir]]){
                        x += dx[dir];
                        y += dy[dir];
                    } else {
                        break;
                    }
                }
            }
            int temp_order_end = temp_order.size();

            // 下から上に戻る
            for (int i = temp_order_end-1; i >= 0; i--){
                if (H_flat[temp_order[i]] < 0){
                    temp_order.push_back(temp_order[i]);
                }
            }

            score = calc_score(temp_order,temp_order_end);
            best_score = score;
            best_order = temp_order;
            best_order_end = temp_order_end;

        }
        
        {
            // 中心に向かって渦巻きに見ていく 逆
            int x = 0, y = 0;
            int dir = 0;
            vector<vector<bool>> visited(n, vector<bool>(n));
            vector<int> temp_order;
            while (true){
                temp_order.push_back(x*n+y);
                visited[x][y] = true;
                if (0 <= x+rdx[dir] && x+rdx[dir] < n && 0 <= y+rdy[dir] && y+rdy[dir] < n && !visited[x+rdx[dir]][y+rdy[dir]]){
                    x += rdx[dir];
                    y += rdy[dir];
                } else {
                    dir = (dir + 1) % 4;
                    if (0 <= x+rdx[dir] && x+rdx[dir] < n && 0 <= y+rdy[dir] && y+rdy[dir] < n && !visited[x+rdx[dir]][y+rdy[dir]]){
                        x += rdx[dir];
                        y += rdy[dir];
                    } else {
                        break;
                    }
                }
            }
            int temp_order_end = temp_order.size();

            // 下から上に戻る
            for (int i = temp_order_end-1; i >= 0; i--){
                if (H_flat[temp_order[i]] < 0){
                    temp_order.push_back(temp_order[i]);
                }
            }

            score = calc_score(temp_order,temp_order_end);
            if (score < best_score){
                best_score = score;
                best_order = temp_order;
                best_order_end = temp_order_end;
            }
        }

        {
            // 上からジグザグに見ていく
            vector<int> temp_order;
            for (int i = 0; i < n; i++){
                if (i % 2 == 0){
                    for (int j = 0; j < n; j++){
                        temp_order.push_back(i*n+j);
                    }
                } else {
                    for (int j = n-1; j >= 0; j--){
                        temp_order.push_back(i*n+j);
                    }
                }
            }
            int temp_order_end = temp_order.size();
            // 下から上に戻る
            for (int i = temp_order_end-1; i >= 0; i--){
                if (H_flat[temp_order[i]] < 0){
                    temp_order.push_back(temp_order[i]);
                }
            }

            score = calc_score(temp_order,temp_order_end);
            if (score < best_score){
                best_score = score;
                best_order = temp_order;
                best_order_end = temp_order_end;
            }
        }

        {
            // ジグザグ 左から右に見ていく
            vector<int> temp_order;
            for (int i = 0; i < n; i++){
                if (i % 2 == 0){
                    for (int j = 0; j < n; j++){
                        temp_order.push_back(j*n+i);
                    }
                } else {
                    for (int j = n-1; j >= 0; j--){
                        temp_order.push_back(j*n+i);
                    }
                }
            }
            int temp_order_end = temp_order.size();
            // 下から上に戻る
            for (int i = temp_order_end-1; i >= 0; i--){
                if (H_flat[temp_order[i]] < 0){
                    temp_order.push_back(temp_order[i]);
                }
            }

            score = calc_score(temp_order,temp_order_end);
            if (score < best_score){
                best_score = score;
                best_order = temp_order;
                best_order_end = temp_order_end;
            }

        }

        score = best_score;
        order = best_order;
        order_end = best_order_end;
        
    }


    int calc_score(){
        // H の copy を作る
        vector<int> H_copy = H_flat;
        long long score = 0;
        int weight = 0;
        int pos = 0;
        
        int accum = 0;
        for (int i = 0; i < order_end; i++){
            int npos = order[i];
            if (H_copy[npos] == 0) continue;   
            
            // nw = 積む or 降ろす 量の計算をする
            // 0 だったら通る必要がない
            int nw = 0;
            if (H_copy[npos] > 0){
                if (accum < 0){
                    nw = min(-accum, H_copy[npos]);
                    nw = H_copy[npos] - nw;
                } else {
                    nw = H_copy[npos];
                }
            } else{
                nw = min(-H_copy[npos], weight);
            }
            accum += H_copy[npos];
            if (nw == 0) continue;

            score += dist[pos][npos] * (100 + weight);
            if (H_copy[npos] > 0){
                weight += nw;
                score += nw;
                H_copy[npos] -= nw;
            } else{
                weight -= nw;
                score += nw;
                H_copy[npos] += nw;
            }
            
            pos = npos;
        }

        for (int i = order_end-1; i >= 0; i--){
            int npos = order[i];
            if (H_copy[npos] == 0) continue;

            score += dist[pos][npos] * (100 + weight);
            if (H_copy[npos] > 0){
                weight += H_copy[npos];
                score += H_copy[npos];
                H_copy[npos] = 0;
            } else {
                int nw = min(-H_copy[npos], weight);
                weight -= nw;
                score += nw;
                H_copy[npos] += nw;
            }
            pos = npos;
        }

        return score;
    }
    int calc_score(vector<int> &temp_order, int temp_order_end){
        // H の copy を作る
        vector<int> H_copy = H_flat;
        long long score = 0;
        int weight = 0;
        int pos = 0;
        int accum = 0;

        for (int i = 0; i < temp_order_end; i++){
            int npos = temp_order[i];
            if (H_copy[npos] == 0) continue;   
            
            // nw = 積む or 降ろす 量の計算をする
            // 0 だったら通る必要がない
            int nw = 0;
            if (H_copy[npos] > 0){
                if (accum < 0){
                    nw = min(-accum, H_copy[npos]);
                    nw = H_copy[npos] - nw;
                } else {
                    nw = H_copy[npos];
                }
            } else{
                nw = min(-H_copy[npos], weight);
            }

            accum += H_copy[npos];

            if (nw == 0) continue;

            score += dist[pos][npos] * (100 + weight);
            if (H_copy[npos] > 0){
                weight += nw;
                score += nw;
                H_copy[npos] -= nw;
            } else{
                weight -= nw;
                score += nw;
                H_copy[npos] += nw;
            }

            pos = npos;
        }

        for (int i = temp_order_end-1; i >= 0; i--){
            int npos = temp_order[i];
            if (H_copy[npos] == 0) continue;

            score += dist[pos][npos] * (100 + weight);
            if (H_copy[npos] > 0){
                weight += H_copy[npos];
                score += H_copy[npos];
                H_copy[npos] = 0;
            } else {
                int nw = min(-H_copy[npos], weight);
                weight -= nw;
                score += nw;
                H_copy[npos] += nw;
            }
            pos = npos;
        }
        return score;
    }

    void update_score(long long nex_score){
        score = nex_score;
        if (score < best_score){
            best_score = score;
            best_order = order;
        }
        
    }

    void out_ans(){
        vector<string> ans;
        vector<int> H_copy = H_flat;
        int weight = 0;
        int pos = 0;

        int accum = 0;
        for (int i = 0; i < best_order_end; i++){
            int npos = best_order[i];
            if (H_copy[npos] == 0) continue;

            // nw = 積む or 降ろす 量の計算をする
            // 0 だったら通る必要がない
            int nw = 0;
            if (H_copy[npos] > 0){
                if (accum < 0){
                    nw = min(-accum, H_copy[npos]);
                    nw = H_copy[npos] - nw;
                } else {
                    nw = H_copy[npos];
                }
            } else{
                nw = min(-H_copy[npos], weight);
            }
            accum += H_copy[npos];
            if (nw == 0) continue;

            int x = X[pos], y = Y[pos];
            int nx = X[npos], ny = Y[npos];

            if (npos != pos){
                while (x != nx){
                    if (nx > x){
                        ans.push_back("D");
                    } else {
                        ans.push_back("U");
                    }
                    x += (nx > x ? 1 : -1);
                }
                while (y != ny){
                    if (ny > y){
                        ans.push_back("R");
                    } else {
                        ans.push_back("L");
                    }
                    y += (ny > y ? 1 : -1);
                }
            }

            if (H_copy[npos] > 0){
                ans.push_back("+" + to_string(nw));
                weight += nw;
                H_copy[npos] -= nw;

            } else {
                assert (nw);
                ans.push_back("-" + to_string(nw));
                weight -= nw;
                H_copy[npos] += nw;
            }
            pos = npos;

        }

        for (int i = best_order_end-1; i >= 0; i--){
            int npos = best_order[i];
            if (H_copy[npos] == 0) continue;

            int x = X[pos], y = Y[pos];
            int nx = X[npos], ny = Y[npos];

            if (npos != pos){
                while (x != nx){
                    if (nx > x){
                        ans.push_back("D");
                    } else {
                        ans.push_back("U");
                    }
                    x += (nx > x ? 1 : -1);
                }
                while (y != ny){
                    if (ny > y){
                        ans.push_back("R");
                    } else {
                        ans.push_back("L");
                    }
                    y += (ny > y ? 1 : -1);
                }
            }

            if (H_copy[npos] > 0){
                ans.push_back("+" + to_string(H_copy[npos]));
                weight += H_copy[npos];
                H_copy[npos] = 0;
            } else {
                ans.push_back("-" + to_string(-H_copy[npos]));
                weight -= H_copy[npos];
                H_copy[npos] = 0;
            }


            pos = npos;
        }

        for (string s : ans) cout << s << endl;

        long long true_score = round(1e9 * base / best_score);
        cerr << "score = " << true_score << endl;

    }
};

struct Solver {

    void solve() {

        // 初期状態を作る
        State state = State();
        // state.out_ans();
        // exit(0);
        // cout << endl;
        double start_temp = 1;
        double end_temp = 0.01;
        double temp = start_temp;
        double progress = 0.0;
        int loop = 0;
        cerr << "start at " << timer.get_time() << endl;

        while (true){
            // temp は log線形
            loop++;
            if ((loop & 255) == 0){

                progress = timer.progress(time_limit);
                if (progress >= 1.0) break;
                temp = pow(start_temp,1-progress) * pow(end_temp,progress);
                // temp = start_temp + (end_temp - start_temp) * progress;
                // temp = 0;

            }
            double rnd = rng.random();
            // rnd = 1;
            if (rnd < 0.2){
                neighbor1(state,temp);
                
            } else if (rnd < 0.6){
                neighbor2(state,temp);
            } else {
                neighbor3(state,temp);
            }
            
        }
        cerr << "loop = " << loop << endl;
        state.out_ans();
        
    }

    // temp と difscore から 近傍の採択を返す関数
    bool accept(double temp, int difscore){
        if (difscore < 0) return true;
        return exp(-difscore/temp) > rng.random();
    }


    void neighbor1(State &state, double temp){
        // 2つの順番を入れ替える
        int l = rng.randrange(state.order_end-1);
        int r = rng.randint(l+1, state.order_end-1);

        swap(state.order[l], state.order[r]);
        int difscore = state.calc_score() - state.score;
        if (accept(temp, difscore)){
            // cerr << "neighbor1 l = " << l << " r = " << r << " difscore = " << difscore << " time = " << timer.get_time() << endl;
            state.update_score(state.score + difscore);
        } else {
            swap(state.order[l], state.order[r]);
        }
       
    }

    // 2opt
    void neighbor2(State &state, double temp){
        int l = rng.randrange(state.order_end-1);
        int r = rng.randint(l+1, state.order_end-1);

        reverse(state.order.begin() + l, state.order.begin() + r);
        int difscore = state.calc_score() - state.score;
        if (accept(temp, difscore)){
            // cerr << "neighbor2 l = " << l << " r = " << r << " difscore = " << difscore << " time = " << timer.get_time() << endl;
            state.update_score(state.score + difscore);
        } else {
            reverse(state.order.begin() + l, state.order.begin() + r);
        }
    }

    // 3opt
    void neighbor3(State &state, double temp){
        int l = rng.randrange(state.order_end-2);
        int r = rng.randint(l+2, state.order_end);
        int c = rng.randint(l+1, r-1);
        
        for (int i = l; i < r; i++){
            recocd_order[i] = state.order[i];
        }
        rotate(state.order.begin() + l, state.order.begin() + c, state.order.begin() + r);

        int difscore = state.calc_score() - state.score;
        if (accept(temp, difscore)){
            // change log
            // cerr << "l = " << l << " r = " << r << " difscore = " << difscore << endl;
            // cerr << "l = " << l << " r = " << r << " c = " << c << " difscore = " << difscore << endl;
            state.update_score(state.score + difscore);
            // state.out_ans();
            // exit(0);
        } else {
            for (int i = l; i < r; i++){
                state.order[i] = recocd_order[i];
            }
        }
    }

    
};

int main() {
    Input();
    Solver solver = Solver();
    solver.solve();

    
    return 0;
}