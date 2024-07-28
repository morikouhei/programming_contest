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
double time_limit = 1.9;

int n,m,si,sj;
int tlen = 5;
int S;
vector<string> A,T;
vector<vector<int>> pos;
vector<vector<int>> same_length;
vector<vector<int>> dist;
// [m][n**2][tlen+1][n**2] の配列を作る
vector<vector<vector<vector<int>>>> dp;
vector<vector<vector<vector<int>>>> par;


void Input() {
    cin >> n >> m;
    cin >> si >> sj;
    S = si*n + sj;
    A.resize(n);
    pos.resize(26);
    for (int i = 0; i < n; i++){
        cin >> A[i];
        for (int j = 0; j < n; j++){
            pos[A[i][j]-'A'].push_back(i*n+j);
        }
    }
    T.resize(m);
    for (int i = 0; i < m; i++){
        cin >> T[i];
    }
    // T[i][j] = T[i]のsuffix と T[j] のprefix が何文字一致するか
    same_length.resize(m);
    for (int i = 0; i < m; i++){
        same_length[i].resize(m);
        for (int j = 0; j < m; j++){
            
            for (int same_len = 1;same_len <= tlen; same_len++){
                if (T[i].substr(tlen-same_len) == T[j].substr(0,same_len)){
                    same_length[i][j] = same_len;
                }
            }
        }
    }

    // dist[i][j] = i から j までのマンハッタン距離 
    dist.resize(n*n);
    for (int id1 = 0; id1 < n*n; id1++){
        dist[id1].resize(n*n);
        int i1 = id1/n;
        int j1 = id1%n;
        for (int id2 = 0; id2 < n*n; id2++){
            int i2 = id2/n;
            int j2 = id2%n;
            dist[id1][id2] = abs(i1-i2) + abs(j1-j2);
        }
    }

    // T[i] を pos から開始して 末尾 j 文字まで作ったときの npos での最小コスト
    // 復元用に par も作る
    dp.resize(m);
    par.resize(m);
    for (int i = 0; i < m; i++){
        dp[i].resize(n*n);
        par[i].resize(n*n);
        for (int j = 0; j < n*n; j++){
            dp[i][j].resize(tlen+1);
            par[i][j].resize(tlen+1);
            for (int k = 0; k <= tlen; k++){
                dp[i][j][k].resize(n*n,INF);
                par[i][j][k].resize(n*n,-1);
            }
        }
    }

    for (int i = 0; i < m; i++){
        for (int j = 0; j < n*n; j++){
            if (T[i][tlen-1] != A[j/n][j%n]) continue;
            dp[i][j][tlen][j] = 0;
            for (int ti = tlen; ti >= 1; ti--){
                for (auto fr: pos[T[i][ti-1]-'A']){
                    if (ti == 1){
                        for (int to = 0; to < n*n; to++){
                            if (dp[i][j][ti-1][to] > dp[i][j][ti][fr]+dist[fr][to]){
                                dp[i][j][ti-1][to] = dp[i][j][ti][fr]+dist[fr][to];
                                par[i][j][ti-1][to] = fr;
                            }
                        }
                    } else {
                        for (auto to: pos[T[i][ti-2]-'A']){
                            if (dp[i][j][ti-1][to] > dp[i][j][ti][fr]+dist[fr][to]){
                                dp[i][j][ti-1][to] = dp[i][j][ti][fr]+dist[fr][to];
                                par[i][j][ti-1][to] = fr;
                            }
                        }
                    }
                }
            }
        }
    }
};

// T の順列 と T[i] の終了位置の index を state に持つ
struct State {
    vector<int> order;
    vector<int> end_pos;
    int score;

    vector<int> best_order;
    vector<int> best_end_pos;
    int best_score;

    State() {
        // 初期解を作る
        order.resize(m);
        iota(order.begin(),order.end(),0);
        end_pos.resize(m);

        int start = S;
        int last = -1;

        for (auto nex: order){
            int same_len = (last == -1 ? 0 : same_length[last][nex]);
            int min_cost = INF;
            int min_pos = -1;
            for (auto fr: pos[T[nex][tlen-1]-'A']){
                if (dp[nex][fr][same_len][start] < min_cost){
                    min_cost = dp[nex][fr][same_len][start];
                    min_pos = fr;
                }
            }
            assert (min_pos != -1);
            end_pos[nex] = min_pos;
            last = nex;
            start = min_pos;
        }
        score = calc_score();
        best_order = order;
        best_end_pos = end_pos;
        best_score = score;
    }


    int calc_score(){
        int score = 0;

        int start = S;
        int last = -1;
        for (auto nex: order){

            int same_len = (last == -1 ? 0 : same_length[last][nex]);
            score += tlen - same_len;
            score += dp[nex][end_pos[nex]][same_len][start];
            last = nex;
            start = end_pos[nex];
        }

        return score;
    }

    void update_score(int nex_score){
        score = nex_score;
        if (score < best_score){
            best_order = order;
            best_end_pos = end_pos;
            best_score = score;
        }
        // for (int i = 0; i < m; i++){
        //     assert (A[end_pos[i]/n][end_pos[i]%n] == T[i][tlen-1]);
        // }
        // cout << "check ans score = " << score << endl;
        // out_ans();

        // if (score != calc_score()){
        //     cerr << "score = " << score << " calc_score = " << calc_score() << endl;
        //     out_ans();
        // }   
        // assert (score == calc_score());
    }

    void out_ans(){
        int start = S;
        int last = -1;
        for (auto nex: order){
            int same_len = (last == -1 ? 0 : same_length[last][nex]);

            for (int i = same_len; i < tlen; i++){
                start = par[nex][end_pos[nex]][i][start];
                cout << start/n << " " << start%n << endl;
            }
            start = end_pos[nex];
            last = nex;
        }

        cerr << "score = " << score << endl;
    }
};
// Simulated Annealing
struct Solver {
    void solve() {
        // 初期状態を作る
        State state = State();
        // state.out_ans();
        // cout << endl;
        double start_temp = 10;
        double end_temp = 0;
        double temp = start_temp;
        double progress = 0.0;
        int loop = 0;
        cerr << "start at " << timer.get_time() << endl;

        while (true){
            // temp は log線形
            loop++;
            if ((loop & 127) == 0){

                progress = timer.progress(time_limit);
                if (progress >= 1.0) break;
                // temp = pow(start_temp,1-progress) * pow(end_temp,progress);
                temp = start_temp + (end_temp - start_temp) * progress;
                // temp = 0;

            }
           

            if (rng.random() < 0.8){
                neighbor1(state,temp);
            } else {
                neighbor2(state,temp);
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

    // order[l] と order[r] のコスト
    int dif_cost(State &state, int l, int r){
        
        int difcost = 0;
        int same_len = same_length[state.order[l]][state.order[r]];
        difcost += tlen - same_len;
        difcost += dp[state.order[r]][state.end_pos[state.order[r]]][same_len][state.end_pos[state.order[l]]];
        return difcost;
    }

    // 近傍1 order の 3opt
    void neighbor1(State &state, double temp){
        
        int l = rng.randint(0,m-2);
        int r = rng.randint(l+2,min(m,l+10));
        int c = rng.randint(l+1,r-1);

        // order[l,c) と order[c,r) を反転
        // score差分を先に計算
        int difscore = 0;
        
        // order[l-1] から order[l] → order[l-1] から order[c] に変わる
        if (l > 0){
            difscore -= dif_cost(state,l-1,l);
            difscore += dif_cost(state,l-1,c);
        } else {
            difscore -= dp[state.order[l]][state.end_pos[state.order[l]]][0][S];
            difscore += dp[state.order[c]][state.end_pos[state.order[c]]][0][S];
        }
        // order[c-1] から order[c] → order[r-1] から order[l] に変わる
        difscore -= dif_cost(state,c-1,c);
        difscore += dif_cost(state,r-1,l);

        // order[r-1] から order[r] → order[c-1] から order[r] に変わる
        if (r < m){
            difscore -= dif_cost(state,r-1,r);
            difscore += dif_cost(state,c-1,r);
        }

        if (!accept(temp,difscore)) return;



        rotate(state.order.begin()+l,state.order.begin()+c,state.order.begin()+r);
        state.update_score(state.score+difscore);

    }

    // 近傍2 end_pos の変更
    void neighbor2(State &state, double temp){
        
        int l = rng.randint(0,m-2);
        int lind = state.order[l];
        int rind = state.order[l+1];

        int difscore = 0;
        difscore -= dif_cost(state,l,l+1);
        if (l){
            difscore -= dif_cost(state,l-1,l);
        } else{
            difscore -= dp[lind][state.end_pos[lind]][0][S];
        }
        int bef = state.end_pos[lind];
        state.end_pos[lind] = pos[T[lind][tlen-1]-'A'][rng.randint(0,pos[T[lind][tlen-1]-'A'].size()-1)];

        difscore += dif_cost(state,l,l+1);
        if (l){
            difscore += dif_cost(state,l-1,l);
        } else{
            difscore += dp[lind][state.end_pos[lind]][0][S];
        }

        if (!accept(temp,difscore)){
            state.end_pos[lind] = bef;
        } else {
            // cerr << "l = " << l << " " << T[lind] << " lind = " << lind << " rind = " << rind << " update pos = (" << state.end_pos[lind]/n << " " << state.end_pos[lind]%n << ") from (" << bef/n << " " << bef%n  << ") difscore = " << difscore << endl;
            state.update_score(state.score+difscore);
            // state.out_ans();
            // exit(0);
        }
    }
};

int main() {
    Input();
    Solver solver = Solver();
    solver.solve();

    
    return 0;
}