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

const double INF = 1e5;
const int MAX_T = 10000;


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
double time_limit = 2.97;

int n;
vector<vector<int>> A;
vector<int> target_row;

vector<vector<vector<pair<int,int>>>> bfs_dist(500,vector<vector<pair<int,int>>>(5,vector<pair<int,int>>(5,{-1,-1})));
vector<vector<vector<array<int,3>>>> bfs_par(500,vector<vector<array<int,3>>>(5,vector<array<int,3>>(5,{-1,-1,-1})));

vector<vector<vector<int>>> bfs_vis(500,vector<vector<int>>(5,vector<int>(5,-1)));
int vis_count = 0;

void Input() {
    cin >> n;
    target_row.resize(n*n);
    for (int i = 0; i < n*n; i++){
        target_row[i] = i/n;
    }
    A.resize(n);
    for (int i = 0; i < n; i++){
        A[i].resize(n);
        for (auto &a: A[i]) cin >> a;
    }

};

const vector<pair<int, int>> DIJ = {{-1, 0}, {1, 0}, {0, -1}, {0, 1},{0,0}};
const vector<char> DIR = {'U', 'D', 'L', 'R','.'};
const vector<char> REVDIR = {'D', 'U', 'R', 'L','.'};
array<int,3> no_record = {-1,-1,-1};

struct update_info{
    int success;
    int clane_id;
    int turn;
    int end_turn;
    int target_x;
    int target_y;
    vector<pair<int,int>> history;
    vector<char> move_ans;

    update_info(int success,int clane_id,int turn, int end_turn, int target_x,int target_y, vector<pair<int,int>> history,vector<char> move_ans) : 
    success(success),clane_id(clane_id),turn(turn),end_turn(end_turn),target_x(target_x),target_y(target_y),history(history),move_ans(move_ans) {}


};


struct State {
    int n;
    vector<vector<int>> board;
    vector<vector<int>> A;
    vector<vector<int>> B;
    vector<array<int, 3>> pos;
    vector<array<int, 3>> to;
    vector<int> next_B;
    vector<int> finish_list;
    int done;
    long long turn;

    State(int n, const vector<vector<int>>& input_A) : n(n), done(0), turn(0) {
        board.resize(n, vector<int>(n, -1));
        A = input_A;
        for (auto& row : A) {
            reverse(row.begin(), row.end());
        }
        for (int i = 0; i < n; ++i) {
            board[i][0] = A[i].back();
            A[i].pop_back();
        }
        B.resize(n);
        pos.resize(n);
        next_B.resize(n);
        // finish_list.resize(n*n);
        for (int i = 0; i < n; i++){
            next_B[i] = n*i;
        }
        for (int i = 0; i < n; ++i) {
            pos[i] = {i, 0, -1};
        }
    }

    bool apply(const vector<char>& mv) {
        ++turn;
        vector<array<int, 3>> to(n, {-1, -1, -1});

        for (int i = 0; i < n; ++i) {
            int x = pos[i][0];
            int y = pos[i][1];
            int z = pos[i][2];

            if (x == -1){
                if (mv[i] != '.') return false;
            }
            else if (mv[i] == 'P'){
                if (x == -1) return false; //throw runtime_error("Crane " + to_string(i) + " has already bombed.");
                if (z != -1) return false; //throw runtime_error("Crane " + to_string(i) + " holds a container.");
                if (board[x][y] == -1) return false; //throw runtime_error("No container at (" + to_string(x) + ", " + to_string(y) + ").");
                z = board[x][y];
                board[x][y] = -1;
            }
            else if (mv[i] == 'Q'){
                if (x == -1) return false; //throw runtime_error("Crane " + to_string(i) + " has already bombed.");
                if (z == -1) return false; //throw runtime_error("Crane " + to_string(i) + " does not hold a container.");
                if (board[x][y] != -1) return false; //throw runtime_error("Container already exists at (" + to_string(x) + ", " + to_string(y) + ").");
                board[x][y] = z;
                z = -1;
            }
            else if (mv[i] == 'B'){
                if (x == -1) return false; //throw runtime_error("Crane " + to_string(i) + " has already bombed.");
                if (z != -1) return false; //throw runtime_error("Crane " + to_string(i) + " holds a container.");
                x = -1;
                y = -1;     
            }
            else if (mv[i] == '.'){

            }

            else if (mv[i] == 'U'){
                if (x == -1) return false; //throw runtime_error("Crane " + to_string(i) + " has already bombed.");
                int dir = -1;
                for (int num = 0; num < 5; num++){
                    if (mv[i] == DIR[num]) dir = num;
                }
                // auto dir = distance(DIR.begin(), find(DIR.begin(), DIR.end(), mv[i]));
                auto [dx, dy] = DIJ[dir];
                x += dx;
                y += dy;
                if (x >= n || y >= n) return false; //throw runtime_error("Crane " + to_string(i) + " moved out of the board.");
                if (x == -1 || y == -1) return false;
                if (i > 0 && z != -1 && board[x][y] != -1) return false; //throw runtime_error("Cranes " + to_string(i) + " cannot move to a square that contains a container.");
            }
            else if (mv[i] == 'D'){
                if (x == -1) return false; //throw runtime_error("Crane " + to_string(i) + " has already bombed.");
                int dir = -1;
                for (int num = 0; num < 5; num++){
                    if (mv[i] == DIR[num]) dir = num;
                }
                // auto dir = distance(DIR.begin(), find(DIR.begin(), DIR.end(), mv[i]));
                auto [dx, dy] = DIJ[dir];
                x += dx;
                y += dy;
                if (x >= n || y >= n) return false; //throw runtime_error("Crane " + to_string(i) + " moved out of the board.");
                if (x == -1 || y == -1) return false;
                if (i > 0 && z != -1 && board[x][y] != -1) return false; //throw runtime_error("Cranes " + to_string(i) + " cannot move to a square that contains a container.");
            }
            else if (mv[i] == 'L'){
                if (x == -1) return false; //throw runtime_error("Crane " + to_string(i) + " has already bombed.");
                int dir = -1;
                for (int num = 0; num < 5; num++){
                    if (mv[i] == DIR[num]) dir = num;
                }
                // auto dir = distance(DIR.begin(), find(DIR.begin(), DIR.end(), mv[i]));
                auto [dx, dy] = DIJ[dir];
                x += dx;
                y += dy;
                if (x >= n || y >= n) return false; //throw runtime_error("Crane " + to_string(i) + " moved out of the board.");
                if (x == -1 || y == -1) return false;
                if (i > 0 && z != -1 && board[x][y] != -1) return false; //throw runtime_error("Cranes " + to_string(i) + " cannot move to a square that contains a container.");
            }
            else if (mv[i] == 'R'){
                if (x == -1) return false; //throw runtime_error("Crane " + to_string(i) + " has already bombed.");
                int dir = -1;
                for (int num = 0; num < 5; num++){
                    if (mv[i] == DIR[num]) dir = num;
                }
                // auto dir = distance(DIR.begin(), find(DIR.begin(), DIR.end(), mv[i]));
                auto [dx, dy] = DIJ[dir];
                x += dx;
                y += dy;
                if (x >= n || y >= n) return false; //throw runtime_error("Crane " + to_string(i) + " moved out of the board.");
                if (x == -1 || y == -1) return false;
                if (i > 0 && z != -1 && board[x][y] != -1) return false; //throw runtime_error("Cranes " + to_string(i) + " cannot move to a square that contains a container.");
            }
            else{
                return false;
            }

            to[i] = {x, y, z};
            // cerr << "i move by " << mv[i] << " from [" << pos[i][0] << " " << pos[i][1] << " " << pos[i][2] << "] to [" << to[i][0] << " " << to[i][1] << " " << to[i][2] << "]" << endl;
        }

        for (int i = 0; i < n; ++i) {
            if (to[i][0] == -1) continue;
            for (int j = 0; j < i; ++j) {
                if (to[j][0] == -1) continue;
                if (pair(to[i][0], to[i][1]) == pair(to[j][0], to[j][1]))
                    return false;//throw runtime_error("Crane " + to_string(j) + " and " + to_string(i) + " collided.");
                if (pair(to[i][0], to[i][1]) == pair(pos[j][0], pos[j][1]) && 
                    pair(to[j][0], to[j][1]) == pair(pos[i][0], pos[i][1]))
                    return false;//throw runtime_error("Crane " + to_string(i) + " and " + to_string(j) + " collided.");
            }
        }

        pos = to;

        for (int i = 0; i < n; ++i) {
            if (board[i][0] == -1 && !A[i].empty()){
                bool ok = true;
                for (int j = 0; j < n; j++){
                    if (pos[j][2] >= 0 && pair(pos[j][0],pos[j][1]) == pair(i,0)) ok = false;
                }
                if (ok){
                    board[i][0] = A[i].back();
                    A[i].pop_back();
                }
            }
                
            if (board[i][n - 1] != -1) {
                ++done;
                if (n * i <= board[i][n - 1] && board[i][n - 1] < n * (i + 1)) {
                    B[i].push_back(board[i][n - 1]);
                    // finish_list[board[i][n-1]] = 1;

                    // while (next_B[i]/n == i && finish_list[next_B[i]] == 1){
                    //     next_B[i]++;
                    // }
                }
                board[i][n-1] = -1;

                // finish_list[board[i][n-1]] = 1;

            }
        }
        return true;
    }

    bool is_end() {
        return done == n*n;
    }

    long long score() const {
        long long A = turn;
        long long B_P = 0;
        long long C = done;
        long long D = n * n - done;
        for (const auto& row : B) {
            C -= row.size();
            for (size_t a = 0; a < row.size(); ++a) {
                for (size_t b = a + 1; b < row.size(); ++b) {
                    if (row[a] > row[b]) ++B_P;
                }
            }
        }
        return A + B_P * 100 + C * 10000 + D * 1000000;
    }
};


struct Solver{

    long long best_score = 1e18;
    vector<vector<char>> best_ans;

    array<int,3> update_target_single(int cid, State &state){
        
        // 荷物を持ってるなら運ぶ
        if (state.pos[cid][2] >= 0){

            auto [x,y,b] = state.pos[cid];

            int target = state.pos[cid][2]/n;
            if (state.next_B[target] == state.pos[cid][2]){
                return {state.pos[cid][2]/n,n-1,-1};
            }
            


            for (int j = 1; j < n-1; j++){
                if (state.board[target][j] == -1){
                    return {target,j,-1};
                }
            }

            auto [l,r] = minmax({x,target});

            int best = 100;
            array<int,3> nex = {-1,-1,-1};

            for (int i = 0; i < n; i++){
                for (int j = 1; j < n-1; j++){
                    if (state.board[i][j] != -1) continue;
                    int dist = -state.next_B[i]+ n*i;
                    if (i < l){
                        dist += 10*(l-i);
                    }
                    if (i > r){
                        dist += 10*(i-r);
                    }
                    if (dist < best){
                        best = dist;
                        nex = {i,j,-1};
                    }

                }
            }

            // 中継できるなら置く
            if (best < 100){
                return nex;
            }

            // 中継が無理なら搬出する
            return {state.pos[cid][2]/n,n-1,-1};

        }

        // 既に出ているものから探す

        array<int,3> nex;
        int best = 100;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (state.board[i][j] == -1) continue;
                
                int target = state.board[i][j]/n;
                if (state.next_B[target] != state.board[i][j]) continue;

                auto [l1,r1] = minmax({target,i});
                auto [l2,r2] = minmax({i,state.pos[cid][0]});

                int loss = max(0,min(r1,r2)-max(l1,l2));
                int dist = r1-l1 + r2-l2 + loss;

                if (dist < best){
                    best = dist;
                    nex = {i,j,state.board[i][j]};
                }
            }
        }

        if (best < 100){
            return nex;
        }

        // boardに次運ぶものがないので 荷物を増やす
        int target_row = -1;
        int need = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < state.A[i].size(); j++){
                int target = state.A[i][j]/n;
                if (state.next_B[target] == state.A[i][j]){
                    int dist = (state.A[i].size()-j)*10 + abs(state.pos[cid][0] - i);
                    if (dist < best){
                        best = dist;
                        need = state.A[i].size()-j;
                        target_row = i;
                    }
                }
            }
        }

        assert (target_row != -1);

        int space = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (state.board[i][j] == -1 && j != n-1) space++;
            }
        }

        if (need <= space){
            return {target_row,0,state.board[target_row][0]};
        }

        best = 100;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n-1; j++){
                if (state.board[i][j] == -1) continue;
                int dist = state.board[i][j]%n;
                if (dist < best){
                    best = dist;
                    nex = {i,j,state.board[i][j]};
                }
            }
        }

        return nex;

    }

    char get_move_single(int cid, array<int,3> target, State &state){

        auto [x,y,b] = state.pos[cid];

        auto [tx,ty,tb] = target;

        assert (state.pos[cid] != target);

        // 目標にいる
        if (x == tx && y == ty){
            // 置く
            if (b >= 0 && tb == -1){
                return 'Q';
            }
            if (b == -1 && tb >= 0){
                return 'P';
            }
        }

        if (x > tx){
            return 'U';
        } else if (x < tx){
            return 'D';
        } else if (y > ty){
            return 'L';
        } else if (y < ty){
            return 'R';
        }
        assert (false);
    }

    // 基本 clane 0 だけで動かす愚直
    void solve_greedy_single(){

        State state(n,A);
        vector<vector<char>> ans(n);

        vector<array<int,3>> targets(n,{-1,-1,-1});
        for (int i = 0; i < n; i++){
            targets[i] = {i,0,-1};
        }

        for (int i = 0; i < 3; i++){

            // target を各列の先頭に
            for (int cid = 0; cid < n; cid++){
                targets[cid] = {cid,0,state.board[cid][0]};
            }
            while (targets[0] != state.pos[0]){
                vector<char> moves(n,'.');
                for (int cid = 0; cid < n; cid++){
                    moves[cid] = get_move_single(cid,targets[cid],state);
                }
                state.apply(moves);
                for (int cid = 0; cid < n; cid++){
                    ans[cid].push_back(moves[cid]);
                }
            }

            // 右に動かす
            for (int cid = 0; cid < n; cid++){
                targets[cid] = {cid,3-i,-1};
            }
            while (targets[0] != state.pos[0]){
                vector<char> moves(n,'.');
                for (int cid = 0; cid < n; cid++){
                    moves[cid] = get_move_single(cid,targets[cid],state);
                }
                state.apply(moves);
                for (int cid = 0; cid < n; cid++){
                    ans[cid].push_back(moves[cid]);
                }
            }

            // 左に戻る
            for (int cid = 0; cid < n; cid++){
                targets[cid] = {cid,0,-1};
            }
            while (targets[0] != state.pos[0]){
                vector<char> moves(n,'.');
                for (int cid = 0; cid < n; cid++){
                    moves[cid] = get_move_single(cid,targets[cid],state);
                }
                state.apply(moves);
                for (int cid = 0; cid < n; cid++){
                    ans[cid].push_back(moves[cid]);
                }
            }


        }
        for (int turn = 0; turn < MAX_T; turn++){
            if (state.is_end()){
                break;
            }
            vector<char> moves(n,'.');

            for (int cid = 0; cid < n; cid++){
                if (state.pos[cid][0] == -1){
                    continue;
                }
                if (cid){
                    moves[cid] = 'B';
                    continue;
                }

                if (targets[cid] == state.pos[cid]){
                    // target を更新
                    targets[cid] = update_target_single(cid,state);
                }

                // move を取得して moves を更新
                moves[cid] = get_move_single(cid,targets[cid],state);

            }

            state.apply(moves);
            for (int cid = 0; cid < n; cid++){
                ans[cid].push_back(moves[cid]);
            }
        }

        long long score = state.score();
        if (score < best_score){
            best_score = score;
            best_ans = ans;
        }

    }


    double evaluate(int ind1, int ind2, int ind3, int ind4, int ind5, int update_ind){
        
        vector<int> used(n*n,-1);
        vector<int> use_ind = {ind1,ind2,ind3,ind4,ind5};

        for (int i = 0; i < n; i++){
            int le = use_ind[i];

            for (int j = 0; j < le; j++){
                used[A[i][j]] = i;
            }
        }

        int left = 0;

        vector<int> pos(n);
        vector<int> next_target;

        for (int i = 0; i < n; i++){
            int target = i*n;
            int ok = 1;
            for (int j = 0; j < n; j++){
                if (used[i*n+j] == -1){
                    ok = 0;
                } 
                else{
                    if (ok) target++;
                    else {
                        left++;
                        pos[i]++;
                    }
                }

            }
            next_target.push_back(target);
        }

        double eval = 0;
        
        // 追加する荷物がすぐ出せるか
        int na = A[update_ind][use_ind[update_ind]];
        // まだ順番じゃないなら + 
        if (next_target[na/n] != na){
            left++;
            eval += 100;
            pos[na/n]++;
        } else{
            // 順番だけど道が塞がってるなら クレーン0を使うしかない
            if (left > 8){
                eval += 100;
            }
            int target = na/n;
            na++;
            while (na/n == target && used[na] >= 0){
                left--;
                pos[na/n]--;
                na++;
            }

            
        }

        eval += left*left;

        // それぞれの搬出に寄せて置きたいので偏ると嬉しくない
        for (auto c: pos){
            eval += c*c;
        }

        return eval;

    }

    // 搬入する順番をdpで決める
    vector<int> get_order_dp(){

        vector<vector<vector<vector<vector<double>>>>> dp(
        n+1, vector<vector<vector<vector<double>>>>(
            n+1, vector<vector<vector<double>>>(
                n+1, vector<vector<double>>(
                    n+1, vector<double>(n+1, INF)))));

        vector<vector<vector<vector<vector<int>>>>> parent(
            n+1, vector<vector<vector<vector<int>>>>(
                n+1, vector<vector<vector<int>>>(
                    n+1, vector<vector<int>>(
                        n+1, vector<int>(n+1, -1)))));


        // 初期状態を設定 (必要に応じて)
        dp[0][0][0][0][0] = 0;  // 例: 初期状態が0の場合

        // DPの更新
        for (int ind1 = 0; ind1 < n+1; ++ind1) {
            for (int ind2 = 0; ind2 < n+1; ++ind2) {
                for (int ind3 = 0; ind3 < n+1; ++ind3) {
                    for (int ind4 = 0; ind4 < n+1; ++ind4) {
                        for (int ind5 = 0; ind5 < n+1; ++ind5) {
                            double current_value = dp[ind1][ind2][ind3][ind4][ind5];
                            int p = parent[ind1][ind2][ind3][ind4][ind5];
                            if (ind1 + 1 < n+1) {
                                double next_value = current_value + evaluate(ind1, ind2, ind3, ind4, ind5, 0) + (p == 0) * 20;
                                if (next_value < dp[ind1 + 1][ind2][ind3][ind4][ind5] || (next_value == dp[ind1 + 1][ind2][ind3][ind4][ind5] &&  parent[ind1 + 1][ind2][ind3][ind4][ind5] != 0)) {
                                    dp[ind1 + 1][ind2][ind3][ind4][ind5] = next_value;
                                    parent[ind1 + 1][ind2][ind3][ind4][ind5] = 0;
                                }
                            }
                            if (ind2 + 1 < n+1) {
                                double next_value = current_value + evaluate(ind1, ind2, ind3, ind4, ind5, 1) + (p == 1) * 20;
                                if (next_value < dp[ind1][ind2 + 1][ind3][ind4][ind5] || (next_value == dp[ind1][ind2 + 1][ind3][ind4][ind5] &&  parent[ind1][ind2 + 1][ind3][ind4][ind5] != 1)) {
                                    dp[ind1][ind2 + 1][ind3][ind4][ind5] = next_value;
                                    parent[ind1][ind2 + 1][ind3][ind4][ind5] = 1;
                                }
                            }
                            if (ind3 + 1 < n+1) {
                                double next_value = current_value + evaluate(ind1, ind2, ind3, ind4, ind5, 2) + (p == 2) * 20;
                                if (next_value < dp[ind1][ind2][ind3 + 1][ind4][ind5] || (next_value == dp[ind1][ind2][ind3 + 1][ind4][ind5] &&  parent[ind1][ind2][ind3 + 1][ind4][ind5] != 2)) {
                                    dp[ind1][ind2][ind3 + 1][ind4][ind5] = next_value;
                                    parent[ind1][ind2][ind3 + 1][ind4][ind5] = 2;
                                }
                            }
                            if (ind4 + 1 < n+1) {
                                double next_value = current_value + evaluate(ind1, ind2, ind3, ind4, ind5, 3) + (p == 3) * 20;
                                if (next_value < dp[ind1][ind2][ind3][ind4 + 1][ind5] || (next_value == dp[ind1][ind2][ind3][ind4 + 1][ind5] &&  parent[ind1][ind2][ind3][ind4 + 1][ind5] != 3)) {
                                    dp[ind1][ind2][ind3][ind4 + 1][ind5] = next_value;
                                    parent[ind1][ind2][ind3][ind4 + 1][ind5] = 3;
                                }
                            }
                            if (ind5 + 1 < n+1) {
                                double next_value = current_value + evaluate(ind1, ind2, ind3, ind4, ind5, 4) + (p == 4) * 20;
                                if (next_value < dp[ind1][ind2][ind3][ind4][ind5 + 1] || (next_value == dp[ind1][ind2][ind3][ind4][ind5 + 1] &&  parent[ind1][ind2][ind3][ind4][ind5 + 1] != 4)) {
                                    dp[ind1][ind2][ind3][ind4][ind5 + 1] = next_value;
                                    parent[ind1][ind2][ind3][ind4][ind5 + 1] = 4;
                                }
                            }
                        }
                    }
                }
            }
        }

        cerr << "Get score" << dp[n][n][n][n][n] << endl;
        // 復元
        vector<int> path;
        int ind1 = n, ind2 = n, ind3 = n, ind4 = n, ind5 = n;
        while (ind1 > 0 || ind2 > 0 || ind3 > 0 || ind4 > 0 || ind5 > 0) {
            int move = parent[ind1][ind2][ind3][ind4][ind5];
            path.push_back(move);
            if (move == 0) --ind1;
            else if (move == 1) --ind2;
            else if (move == 2) --ind3;
            else if (move == 3) --ind4;
            else if (move == 4) --ind5;
        }

        // パスを逆順に出力
        reverse(path.begin(), path.end());
        for (int move : path) {
            cerr << move << " ";
        }
        cerr << endl;

        return path;

    }


    vector<array<int,5>> get_tasks(vector<int> &order){

        vector<array<int,5>> tasks;
        vector<int> next_target(n);
        vector<pair<int,int>> put_pos(n*n,{-1,-1});
        for (int i = 0; i < n; i++){
            next_target[i] = i*n;
        }
        vector<int> use_A(n);
        vector<vector<int>> state(n,vector<int>(n,-1));

        for (int i = 0; i < n; i++){
            state[i][0] = A[i][0];
        }
        for (auto row: order){
            int a = A[row][use_A[row]];

            if (next_target[target_row[a]] == a){
                tasks.push_back({a,row,0,target_row[a],n-1});

                next_target[target_row[a]]++;
                while (next_target[target_row[a]]/n == target_row[a] && put_pos[next_target[target_row[a]]] != pair(-1,-1) ){
                    auto [x,y] = put_pos[next_target[target_row[a]]];
                    state[x][y] = -1;
                    tasks.push_back({next_target[target_row[a]],x,y,target_row[a],n-1});
                    next_target[target_row[a]]++;
                }

            } else {
                vector<int> cand_pos;
                if (target_row[a] <= 1){
                    cand_pos.push_back(0);
                    cand_pos.push_back(2);
                    cand_pos.push_back(4);
                }
                else if (target_row[a] == 2){
                    cand_pos.push_back(2);
                    if (row <= 2){
                        cand_pos.push_back(0);
                        cand_pos.push_back(4);
                    } else{
                        cand_pos.push_back(4);
                        cand_pos.push_back(0);
                    }
                } else {
                    cand_pos.push_back(4);
                    cand_pos.push_back(2);
                    cand_pos.push_back(0);
                }
                bool ok = false;
                for (auto cpos : cand_pos){
                    if (ok) break;
                    for (int i = 3; i >= 2; i--){
                        if (state[cpos][i] == -1){
                            ok = true;
                            tasks.push_back({a,row,0,cpos,i});
                            put_pos[a] = {cpos,i};
                            state[cpos][i] = a;
                            break;
                        }
                    }
                }

                for (auto cpos : {1,3}){
                    if (ok) break;
                    for (int i = 3; i >= 3; i--){
                        if (state[cpos][i] == -1){
                            ok = true;
                            tasks.push_back({a,row,0,cpos,i});
                            put_pos[a] = {cpos,i};
                            state[cpos][i] = a;
                            break;
                        }
                    }
                }
                if (!ok){
                    cerr << "need clane 0" << endl;
                }
                for (auto cpos : cand_pos){
                    if (ok) break;
                    if (cpos == 2) continue;
                    for (int i = 1; i >= 1; i--){
                        if (state[cpos][i] == -1){
                            ok = true;
                            tasks.push_back({a,row,0,cpos,i});
                            put_pos[a] = {cpos,i};
                            state[cpos][i] = a;
                            break;
                        }
                    }
                }
                

                if (!ok){
                    cerr << "need clane 0" << endl;
                }
                for (int i = 3; i >= 1; i--){
                    if (ok) break;
                    for (int j = 0; j < n; j++){
                        if (state[j][i] == -1){
                            ok = true;
                            tasks.push_back({a,row,0,j,i});
                            put_pos[a] = {j,i};
                            state[j][i] = a;
                            break;
                        }
                    }
                }

            }

            use_A[row]++;
            if (use_A[row] < n){
                state[row][0] = A[row][use_A[row]];
            }
        }

        for (auto x: next_target){
            cerr << x << " ";
        }
        cerr << endl;

        for (auto [a,x,y,nx,ny] : tasks){
            cerr << a << " " << x << " " << y << " " << nx << " " << ny << endl;
        }
        cerr << tasks.size() << endl;

        return tasks;

    }


    update_info update_return_clane(int turn, int target_clane,int gx , int gy,
                    vector<int> &last_use_clane, 
                    vector<int> &finish_A_turn,
                    vector<int> &last_return_clane,
                    vector<int> &plan_return_clane,
                    vector<vector<vector<int>>> &board_history,  
                    vector<vector<vector<int>>> &clane_history, 
                    vector<vector<array<int,3>>> &clane_pos,
                    vector<vector<char>> &ans,
                    vector<int> &plan_last_clane_use, 
                    bool force = false){

        
        vector<pair<int,int>> history3;
        vector<char> move_ans3;

        
        if (force == false && target_clane == last_return_clane[plan_return_clane[target_clane]]){
            return update_info(2,0,0,0,0,0,history3,move_ans3);
        }

        // cerr << " update clane = " << target_clane << endl;
        // cerr << " start at " << turn << " " << gx << " " << gy << endl;
        // cerr << "last return clane ";
        // for (int i = 0; i < n; i++){
        //     cerr << last_return_clane[i] << " ";
        // }
        // cerr << endl;
        // cerr << "plan_return_clane ";
        // for (int i = 0; i < n; i++){
        //     cerr << plan_return_clane[i] << " ";
        // }
        // cerr << endl;

        // cerr << "clear from clane = " << target_clane << " from " << turn+1 << " to " << plan_last_clane_use[target_clane]+50 << endl;
        

        vis_count++;

        bfs_dist[turn][gx][gy] = {0,0};
        bfs_vis[turn][gx][gy] = vis_count;
        
        queue<array<int,3>> q;
        pair<int,int> min_dist = {1000,1000};
        array<int,3> target = {-1,-1,-1};
        q.push({turn,gx,gy});

        for (int t = turn; t < turn+20; t++){
            queue<array<int,3>> nq;
            while (!q.empty()){
               
                auto [t,x,y] = q.front(); q.pop();
                //  if (target_clane == 1){
                //     cerr << "t = " << t << " x = " << x << " y = " << y << " " << clane_history[t][x][y] << " " << clane_history[turn+1][x][y] << endl;
                // }
                auto [d_base,d_use] = bfs_dist[t][x][y];

                // goal かつ 前の荷物も 搬出ずみ
                if (y == 0 && last_return_clane[x] == -1){
                    bool ok = true;

                    for (int nt = t+1; nt <= t+10; nt++){
                        if (clane_history[nt][x][y] >= 0 && (last_use_clane[clane_history[nt][x][y]] >= nt)) ok = false;
                    }


                    if (ok && min_dist > bfs_dist[t][x][y]){
                        min_dist = bfs_dist[t][x][y];
                        target = {t,x,y};
                    }
                }

                for (int i = 0; i < 5; i++){
                    auto [dx,dy] = DIJ[i];
                    int nx = x+dx;
                    int ny = y+dy;
                    if (t+1 >= board_history.size()) continue;
                    if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                    // if (target_clane == 0){
                    //     cerr << "t = " << t << " x = " << x << " y = " << y << " nx = " << nx << " ny = " << ny << " " << clane_history[t+1][x][y]  << " " << clane_history[t][nx][ny] <<  endl;
                    // }
                    // cerr << "t = " << t << " x = " << x << " y = " << y << " nx = " << nx << " ny = " << ny << endl;
                    // 既にその場所が 他の clane に使われてる
                    if (clane_history[t+1][nx][ny] >= 0 && clane_history[t+1][nx][ny] != target_clane) continue;

                    // 既に決まっている clane と 位置の swap が起こる
                    if (clane_history[t+1][x][y] >= 0 && clane_history[t][nx][ny] == clane_history[t+1][x][y]  && clane_history[t+1][x][y] != target_clane) continue;

                    pair<int,int> nd = {d_base+1,d_use - (board_history[t+1][nx][ny] >= 0) + (ny == n-1)};
                    if (bfs_vis[t+1][nx][ny] != vis_count || bfs_dist[t+1][nx][ny] > nd){
                        bfs_dist[t+1][nx][ny] = nd;
                        bfs_par[t+1][nx][ny] = {x,y,i};
                        bfs_vis[t+1][nx][ny] = vis_count;

                        nq.push({t+1,nx,ny});
                    }
                }
            }
            if (min_dist.first != 1000) break;
            swap(q,nq);
        }

        // cerr << min_dist.first << " " << min_dist.second << " " << target[0] <<endl;
        // cerr << target[0] << " " << target[1] << " " << target[2] << endl;
        if (min_dist.first == 1000){
            // swap(last_return_clane,last_return_clane_save);
            return update_info(0,0,0,0,0,0,history3,move_ans3);
        }

        

        pair<int,int> pos = {target[1],target[2]};

        for (int t = target[0]; t > turn; t--){
            history3.push_back(pos);
            auto [nx,ny,id] = bfs_par[t][pos.first][pos.second];
            pos = {nx,ny};
            move_ans3.push_back(DIR[id]);
        };

        reverse(history3.begin(),history3.end());
        reverse(move_ans3.begin(),move_ans3.end());
 
        return update_info(1,target_clane,turn,turn+history3.size(),target[1],target[2],history3,move_ans3);

    }

    void apply_update_info(update_info &up_info, 
                            vector<int> &last_return_clane,
                            vector<int> &plan_return_clane,
                            vector<vector<vector<int>>> &board_history,  
                            vector<vector<vector<int>>> &clane_history, 
                            vector<vector<array<int,3>>> &clane_pos,
                            vector<vector<char>> &ans,
                            vector<int> &plan_last_clane_use){
        
        if (up_info.success != 1) return;

        // cerr << "apply start " << endl;
        int turn = up_info.turn;
        int target_clane = up_info.clane_id;
        // cerr << " turn = " << turn << " target = " << target_clane << "last plan = " << plan_last_clane_use[target_clane] <<endl;
        int t = turn+1;

        while (t < clane_history.size()){
            auto [bx,by,_] = clane_pos[target_clane][t];
            if (bx >= 0){
                // cerr << "clear t = " << t << " bx = " << bx << " by = " << by << endl;
                if (clane_history[t][bx][by] == target_clane){
                    clane_history[t][bx][by] = -1;
                }
                clane_pos[target_clane][t] = no_record;
                ans[target_clane][t-1] = '#';
            } 
            t++;
        }

        // cerr << "new target = " << up_info.target_x << " " << up_info.target_y << endl;
        for (int i = 0; i < up_info.history.size(); i++){
            auto [x,y] = up_info.history[i];
            int t = turn + i;
            // cerr << "move adjust  = " << t << " " << x << " " << y << " " << up_info.move_ans[i] << endl;

            clane_history[t+1][x][y] = target_clane;
            clane_pos[target_clane][t+1] = {x,y,-1};
            ans[target_clane][t] = up_info.move_ans[i];
            // ans の更新
        }

        plan_return_clane[target_clane] = up_info.target_x;
        last_return_clane[up_info.target_x] = target_clane;
        plan_last_clane_use[target_clane] = up_info.end_turn;
        for (int t = plan_last_clane_use[target_clane]; t <= plan_last_clane_use[target_clane]+20; t++){
            if (t >= clane_history.size()) continue;
            clane_history[t][up_info.target_x][up_info.target_y] = target_clane;
            clane_pos[target_clane][t] = {up_info.target_x,up_info.target_y,-1};
        }

        int x = target_clane;
        int y = 0;

        // cerr << "move history clane = " << target_clane << "end at x = " << up_info.target_x << " y = " << up_info.target_y << endl;
        // for (int t = 0; t <= up_info.end_turn+5; t++){

        //     cerr <<"turn = " << t << " " <<  ans[target_clane][t] << "[" << clane_pos[target_clane][t][0] << " " << clane_pos[target_clane][t][1] << "]" << " [" << x << " " << y << "]" << endl;
        //      if (ans[target_clane][t] == 'U'){
        //             x--;
        //         }
        //         if (ans[target_clane][t] == 'D'){
        //             x++;
        //         }
        //         if (ans[target_clane][t] == 'L'){
        //             y--;
        //         }
        //         if (ans[target_clane][t] == 'R'){
        //             y++;
        //         }
        // }
        

    
    }

    bool apply_task(int turn, 
                    int task_id,
                    vector<int> &last_use_clane, 
                    vector<int> &last_return_clane,
                    vector<int> &plan_return_clane,
                    vector<int> &finish_A_turn,
                    array<int,5> &task ,
                    vector<vector<vector<int>>> &board_history,  
                    vector<vector<vector<int>>> &clane_history, 
                    vector<vector<array<int,3>>> &clane_pos,
                    vector<vector<char>> &ans,
                    vector<int> &plan_last_clane_use,
                    vector<vector<int>> &task_by_A,
                    vector<int> &tasks_by_A_count,
                    vector<vector<vector<int>>> &board_history2
                    ){
                
                
        auto [a,sx,sy,gx,gy] = task;

        // cerr << "start " << a << " " << sx << " " << sy << " " << gx << " " << gy << " " << turn << endl;
        
        // cerr << " update return from start" << endl;
        // cerr << "last return clane ";
        // for (int i = 0; i < n; i++){
        //     cerr << last_return_clane[i] << " ";
        // }
        // cerr << endl;
        // cerr << "plan_return_clane ";
        // for (int i = 0; i < n; i++){
        //     cerr << plan_return_clane[i] << " ";
        // }
        // cerr << endl;

        // cerr << "last_use_clane ";
        // for (int i = 0; i < n; i++){
        //     cerr << last_use_clane[i] << " ";
        // }
        // cerr << endl;
        // cerr << "plan_last_clane_use ";
        // for (int i = 0; i < n; i++){
        //     cerr << plan_last_clane_use[i] << " ";
        // }
        // cerr << endl;
        // 過去に戻って荷物を迎える clane を決める
        int min_turn = 1000;
        for (int i = 0; i < n; i++){
            min_turn = min(min_turn,last_use_clane[i]);
        }
        if (min_turn >= turn) return false;

        if (clane_history[turn-1][sx][sy] >= 0 && last_use_clane[clane_history[turn-1][sx][sy]] >= turn-1) return false;
        if (clane_history[turn][sx][sy] >= 0 && last_use_clane[clane_history[turn][sx][sy]] >= turn) return false;


        // 過去に戻りながら clane を探す
        vis_count++;

        // turn sx,sy に P を行う
        bfs_dist[turn-1][sx][sy] = {0,0};
        bfs_vis[turn-1][sx][sy] = vis_count;
        queue<array<int,3>> q;
        q.push({turn-1,sx,sy});

        pair<int,int> min_dist = {1000,1000};
        array<int,3> target = {-1,-1,-1};
        int target_clane = -1;
        for (int t = turn-1; t >= min_turn; t--){
            queue<array<int,3>> nq;
            while (!q.empty()){
                auto [t,x,y] = q.front(); q.pop();
                auto [d_base,d_use] = bfs_dist[t][x][y];
                
                // if (a == 7){
                //     cerr << "t = " << t << " x = " << x << " y = " << y << " " << clane_history[t][x][y] <<  endl;
                // }
                if (clane_history[t][x][y] >= 0  && last_use_clane[clane_history[t][x][y]] < t){
                    bool ok = true;
                    if (t == turn && clane_history[t-1][x][y] != clane_history[t][x][y]) ok = false;
                    if (ok && min_dist > bfs_dist[t][x][y]){
                        min_dist = bfs_dist[t][x][y];
                        target = {t,x,y};
                        target_clane = clane_history[t][x][y];
                        
                    }
                }

                for (int i = 0; i < 5; i++){
                    auto [dx,dy] = DIJ[i];
                    // turnで荷物を掴みたいので turn-1 についている必要がある = turn → turn -1 は [dx,dy] = [0,0]
                    // if (t == turn && (dx != 0 || dy != 0)) continue;
                    int nx = x+dx;
                    int ny = y+dy;
                    if (t <= 0) continue;
                    if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                    // 既にその場所が 他の clane に使われてる

                    // cerr << "t = " << t << " x = " << x << " y = " << y << " nx = " << nx << " ny =  " << ny << " history = " << clane_history[t-1][nx][ny] << endl;
                    if (clane_history[t-1][nx][ny] >= 0 && last_use_clane[clane_history[t-1][nx][ny]] >= t-1) continue;

                    // 既に決まっている clane と 位置の swap が起こる
                    if (i<4 && clane_history[t-1][x][y] >= 0 && clane_history[t][nx][ny] == clane_history[t-1][x][y])continue;// && last_use_clane[clane_history[t-1][x][y]] >= t-1) continue;

                    pair<int,int> nd = {d_base+1,d_use - (board_history[t-1][nx][ny] >= 0)};
                    if (bfs_vis[t-1][nx][ny] != vis_count || bfs_dist[t-1][nx][ny] > nd){
                        bfs_dist[t-1][nx][ny] = nd;
                        bfs_par[t-1][nx][ny] = {x,y,i};
                        bfs_vis[t-1][nx][ny] = vis_count;
                        nq.push({t-1,nx,ny});
                    }
                }
            }
            if (min_dist.first != 1000) break;
            swap(q,nq);
        }

        if (min_dist.first == 1000) return false;


        if (clane_history[turn][sx][sy] >= 0 && clane_history[turn][sx][sy] != target_clane) return false;
        vector<pair<int,int>> history;
        vector<char> move_ans;

        pair<int,int> pos = {target[1],target[2]};
        int t = target[0];
        while (t < turn-1){
            auto [nx,ny,id] = bfs_par[t][pos.first][pos.second];
            move_ans.push_back(REVDIR[id]);
            pos = {nx,ny};
            history.push_back(pos);
            t++;
        };
        history.push_back({sx,sy});
        move_ans.push_back('P');


        // 未来に進みながら 搬送経路を決める

        bool success = true;

        for (int loop = 0; loop < 2; loop++){
            vis_count++;

            bfs_dist[turn][sx][sy] = {0,0};
            bfs_vis[turn][sx][sy] = vis_count;
            while (!q.empty())
            {
                q.pop();
            }
            
            q.push({turn,sx,sy});

            // cerr << "start from " << turn  << " " << sx << " " << sy << " finish_turn = " << finish_A_turn[gx] << endl;

            min_dist = {1000,1000};
            vector<int> changed(n);

            for (int t = turn; t < board_history.size(); t++){
                if (q.empty()) break;
                // cerr << "turn = " <<t << " start " << q.size() << endl;
                
                queue<array<int,3>> nq;
                while (!q.empty()){
                    auto [t,x,y] = q.front(); q.pop();
                    auto [d_base,d_use] = bfs_dist[t][x][y];
                    // if (a == 1){
                    //     cerr << t << " " << x << " " << y << " " << loop << " " << clane_history[t][x][y] << endl;
                    // }
                    // goal かつ 前の荷物も 搬出ずみ
                    if (x == gx && y == gy && (gy != n-1 || t > finish_A_turn[gx])){
                        // 着いた次のターンに荷物を置けるのでそれも確認が必要
                        bool ok = true;
                        
                        if ((board_history[t+1][x][y] >= 0 && board_history[t+1][x][y] < task_id )|| board_history[turn][x][y] > task_id) ok = false;
                        if (clane_history[t+1][x][y] >= 0 && (loop || last_use_clane[clane_history[t+1][x][y]] >= t+1)) ok = false;
                        

                        if (gy != n-1){
                            for (int nt = t+1; nt <= t+10; nt++){
                                if (clane_history[nt][x][y] >= 0 && (loop || last_use_clane[clane_history[nt][x][y]] >= nt)) ok = false;
                            }
                        }

                        if (ok && min_dist > bfs_dist[t][x][y]){
                            min_dist = bfs_dist[t][x][y];
                            target = {t,x,y};
                        }
                    }

                    for (int i = 0; i < 5; i++){
                        auto [dx,dy] = DIJ[i];
                        int nx = x+dx;
                        int ny = y+dy;
                        if (t+1 >= board_history.size()) continue;
                        if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;

                        if (i < 4 && ny == 0) continue;

                        // cerr << t+1 << " " << nx << " " << ny << " " << loop << " " << clane_history[t+1][nx][ny] << endl;

                        // 既にその場所に 荷物がある or turn時点で荷物があり その taskが未処理
                        if (target_clane && (board_history[t+1][nx][ny] >= 0 && board_history[t+1][nx][ny] < task_id ) || board_history2[t+1][nx][ny] > task_id) continue;

                        // 既にその場所が 他の clane に使われてる
                        if (clane_history[t+1][nx][ny] >= 0 && (loop || last_use_clane[clane_history[t+1][nx][ny]] >= t+1)) continue;

                        // 既に決まっている clane と 位置の swap が起こる
                        if (clane_history[t+1][x][y] >= 0 && clane_history[t][nx][ny] == clane_history[t+1][x][y] && (loop || last_use_clane[clane_history[t][nx][ny]] >= t)) continue;

                        pair<int,int> nd = {d_base+1,d_use + (ny == n-1) + (ny == 0 && i != 4)};
                        if (bfs_vis[t+1][nx][ny] != vis_count || bfs_dist[t+1][nx][ny] > nd){
                            bfs_dist[t+1][nx][ny] = nd;
                            bfs_par[t+1][nx][ny] = {x,y,i};
                            bfs_vis[t+1][nx][ny] = vis_count;

                            nq.push({t+1,nx,ny});
                        }
                    }
                }
                if (min_dist.first != 1000) break;
                swap(q,nq);
            }

            // cerr << "end here" << endl;
            if (min_dist.first == 1000) continue;

            // cerr << "start here " << target_clane << endl;
            vector<pair<int,int>> history2;
            vector<char> move_ans2;
            move_ans2.push_back('Q');
            history2.push_back({gx,gy});

            pos = {target[1],target[2]};
            for (int t = target[0]; t > turn; t--){
                history2.push_back(pos);
                if (clane_history[t][pos.first][pos.second] >= 0) changed[clane_history[t][pos.first][pos.second]] = 1;
                auto [nx,ny,id] = bfs_par[t][pos.first][pos.second];
                // if (clane_history[t][nx][ny] >= 0) changed[clane_history[t][nx][ny]] = 1;
                if (clane_history[t][nx][ny] >= 0 && clane_history[t][nx][ny] == clane_history[t-1][pos.first][pos.second]) changed[clane_history[t][nx][ny]] = 1;
                pos = {nx,ny};
                // cerr << "nx = " << nx << " ny = " << ny << endl;
                move_ans2.push_back(DIR[id]);
            };
            if (clane_history[target[0]+1][gx][gy] >= 0) changed[clane_history[target[0]+1][gx][gy]] = 1;
            // cerr << "changed ids = ";
            // for (int i = 0; i < n; i++){
            //     if (changed[i]) cerr << i << " ";
            // }
            // cerr << endl;
            // cerr << "A" << endl;

            reverse(history2.begin(),history2.end());
            reverse(move_ans2.begin(),move_ans2.end());

            int base_plan = plan_return_clane[target_clane];
            vector<int> last_return_clane_save = last_return_clane;
            last_return_clane[base_plan] = -1;
            if (sy == 0){
                last_return_clane[sx] = -1;
            }

            auto clane_history_save = clane_history;
            auto board_history_save = board_history;
            auto last_use_clane_save = last_use_clane;
            vector<int> changed_ind;
            changed[target_clane] = 1;

            for (int i = 0; i < n; i++){
                if (changed[i] == 0) continue;
                changed_ind.push_back(i);
                int base_plan = plan_return_clane[i];
                last_return_clane[base_plan] = -1;

                int t = turn + history2.size();
                if (i != target_clane){
                    t = last_use_clane[i];
                }
                t++;

                while (t < clane_history.size()){

                    auto [bx,by,_] = clane_pos[i][t];
                    if (bx >= 0){
                        if (clane_history[t][bx][by] == i){
                            clane_history[t][bx][by] = -1;
                        }

                    } 
                    t++;
                }

            }
            bool update_ok = true;
            vector<update_info> update_infos;

            for (int i = 0; i < history.size(); i++){
                auto [x,y] = history[i];
                int t = turn - history.size() + i;
                clane_history[t+1][x][y] = target_clane;
                // ans の更新
            }
            for (int i = 0; i < history2.size(); i++){
                auto [x,y] = history2[i];
                int t = turn + i;

                board_history[t+1][x][y] = task_id;                
                clane_history[t+1][x][y] = target_clane;
                // ans の更新
            }

            update_info up_info = update_return_clane(turn + history2.size(),target_clane,gx,gy,
                                last_use_clane, 
                                finish_A_turn,
                                last_return_clane,
                                plan_return_clane,
                                board_history,  
                                clane_history, 
                                clane_pos,
                                ans, plan_last_clane_use,true);

            if (up_info.success == 0){
                update_ok = false;
            }
            update_infos.push_back(up_info);

            for (int j = 0; j < up_info.history.size(); j++){
                auto [x,y] = up_info.history[j];
                int t = turn + history2.size() + j;
                // cerr << "move adjust  = " << t + 1 << " " << x << " " << y << " " << up_info.move_ans[j] << endl;
                clane_history[t+1][x][y] = target_clane;
            }

            last_return_clane[up_info.target_x] = target_clane;
            // cerr << "clane = " << i << " end pos = [" << up_info.target_x << " " << up_info.target_y << "] until " << up_info.end_turn+20 << endl;
            for (int t = up_info.end_turn; t <= up_info.end_turn+20; t++){
                if (t >= clane_history.size()) continue;
                clane_history[t][up_info.target_x][up_info.target_y] = target_clane;
            }
            last_use_clane[target_clane] = turn + history2.size();
           

            for (auto i: changed_ind){
                int end_turn = turn + history2.size();
                int nx = gx, ny = gy;

                if (i == target_clane){
                    continue;
                }
                end_turn = last_use_clane[i];
                nx = clane_pos[i][last_use_clane[i]][0];
                ny = clane_pos[i][last_use_clane[i]][1];
                

                update_info up_info = update_return_clane(end_turn,i,nx,ny,
                                last_use_clane, 
                                finish_A_turn,
                                last_return_clane,
                                plan_return_clane,
                                board_history,  
                                clane_history, 
                                clane_pos,
                                ans, plan_last_clane_use,true);

                if (up_info.success == 0){
                    update_ok = false;
                    break;
                }
                update_infos.push_back(up_info);

                for (int j = 0; j < up_info.history.size(); j++){
                    auto [x,y] = up_info.history[j];
                    int t = end_turn + j;
                    // cerr << "move adjust  = " << t + 1 << " " << x << " " << y << " " << up_info.move_ans[j] << endl;
                    clane_history[t+1][x][y] = i;
                }

                last_return_clane[up_info.target_x] = i;
                // cerr << "clane = " << i << " end pos = [" << up_info.target_x << " " << up_info.target_y << "] until " << up_info.end_turn+20 << endl;
                for (int t = up_info.end_turn; t <= up_info.end_turn+20; t++){
                    if (t >= clane_history.size()) continue;
                    clane_history[t][up_info.target_x][up_info.target_y] = i;
                }
            }
            if (!update_ok){
                // cerr << "update failed" << endl;
                swap(clane_history_save,clane_history);
                swap(last_return_clane_save,last_return_clane);
                swap(board_history_save,board_history);
                swap(last_use_clane_save,last_use_clane);
                continue;
            }
            // cerr << "update success" << endl;

            for (int i = 0; i < 30; i++){
                int t = turn - history.size() + i;
                if (t >= board_history2.size()) break;
                auto [bx,by,_] = clane_pos[target_clane][t+1];
                if (bx >= 0 && clane_history[t+1][bx][by] == target_clane){
                    clane_history[t+1][bx][by] = -1;
                }
            }

            for (int i = 0; i < history.size(); i++){
                auto [x,y] = history[i];
                int t = turn - history.size() + i;
                // cerr << "move1 = " << t << " " << x << " " << y << " " << move_ans[i] << " write = [t = " << t+1 << " x = " << x << " y = " << y << "]" << endl;
                clane_history[t+1][x][y] = target_clane;
                if (t == turn){
                    clane_pos[target_clane][t+1] = {x,y,a};
                } else {
                    clane_pos[target_clane][t+1] = {x,y,-1};
                }
                ans[target_clane][t] = move_ans[i];
                // ans の更新
            }

            for (int i = 0; i < history2.size(); i++){
                auto [x,y] = history2[i];
                int t = turn + i;
                // cerr << "move2 = " << t << " " << x << " " << y << " " << move_ans2[i] << " write = [t = " << t+1 << " x = " << x << " y = " << y << "]" << endl;

                board_history[t+1][x][y] = task_id;
                
                clane_history[t+1][x][y] = target_clane;
                if (i == history2.size()-1){
                    clane_pos[target_clane][t+1] = {x,y,-1};
                    if (y != n-1){
                        board_history[t+1][x][y] = task_by_A[a][tasks_by_A_count[a]];
                    }

                } else {
                    clane_pos[target_clane][t+1] = {x,y,a};
                }
                ans[target_clane][t] = move_ans2[i];
                // ans の更新
            }

            last_use_clane[target_clane] = turn + history2.size();
            
            if (gy != n-1){
                int le = board_history2.size();
                // cerr << "a = " << a << " gx = " << gx << " gy = " << gy << " board history2 from t = " << t << " " << task_by_A[a][tasks_by_A_count[a]] << endl;
                for (int t = last_use_clane[target_clane]; t < le; t++){
                    board_history2[t][gx][gy] = task_by_A[a][tasks_by_A_count[a]];
                }
            }
            
            for (auto up_info : update_infos){
                apply_update_info(up_info,last_return_clane,plan_return_clane,board_history,clane_history,clane_pos,ans,plan_last_clane_use);
            }
           
            if (gy == n-1){
                finish_A_turn[gx] = last_use_clane[target_clane];
            }
            return true;
        }
        

        return false;

        

    }
    void assert_check(vector<vector<char>> &ans,vector<vector<array<int,3>>> &clane_pos,vector<vector<vector<int>>> &clane_history){
        cerr << "assert check insert" << endl;
        for (int t = 0; t < 100; t++){
            vector<int> used(n);
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    if (clane_history[t][i][j] >= 0){
                        used[clane_history[t][i][j]]++;
                        if (used[clane_history[t][i][j]] == 2){
                            cerr << "assert fail at turn = " << t << endl;
                            for (int x = 0; x < n; x++){
                                for (int y = 0; y < n; y++){
                                    cerr << clane_history[t][x][y] << " ";
                                }
                                cerr << endl;
                            }
                        }
                        assert (used[clane_history[t][i][j]] < 2);
                    }
                }
            }
        }
        for (int i = 0; i < n; i++){
            int x = i;
            int y = 0;

            for (int t =0; t < 100; t++){
                if (clane_pos[i][t][0] < 0) continue;
                if (x != clane_pos[i][t][0] || y != clane_pos[i][t][1]){
                    cerr << "ind = " << i << " turn = " << t << " x = " << x << " y = " << y << " nx = " << clane_pos[i][t][0] << " ny = " << clane_pos[i][t][1] << endl;
                 }
                assert ( x == clane_pos[i][t][0] && y == clane_pos[i][t][1]);
                if (ans[i][t] == 'U'){
                    x--;
                }
                if (ans[i][t] == 'D'){
                    x++;
                }
                if (ans[i][t] == 'L'){
                    y--;
                }
                if (ans[i][t] == 'R'){
                    y++;
                }
            }
        }
    }

    void decide_moves(vector<array<int,5>> &tasks){
        long long max_turn = min(best_score+1,(long long)150);
        
        vector<vector<char>> ans(n,vector<char>(max_turn+1,'#'));
        vector<int> last_return_clane(n,-1);
        vector<int> plan_return_clane(n,-1);
        vector<int> plan_last_clane_use(n,0);

        vector<vector<array<int,3>>> clane_pos(n,vector<array<int,3>>(max_turn+1,{-1,-1,-1}));
        vector<vector<vector<int>>> board_history(max_turn+1,vector<vector<int>>(n,vector<int>(n,-1)));
        vector<vector<vector<int>>> board_history2(max_turn+1,vector<vector<int>>(n,vector<int>(n,-1)));

        vector<vector<vector<int>>> clane_history(max_turn+1,vector<vector<int>>(n,vector<int>(n,-1)));

        vector<vector<int>> task_by_A(n*n);
        for (int i = 0; i < tasks.size(); i++){
            task_by_A[tasks[i][0]].push_back(i);
        }
        vector<int> tasks_by_A_count(n*n);
        vector<int> use_A(n);
        vector<int> finish_A_turn(n,-1);
        vector<int> last_use_clane(n,-1);

        // 初期位置の設定
        for (int i = 0; i < n; i++){
            clane_pos[i][0] = {i,0,-1};
            clane_pos[i][1] = {i,0,-1};

            clane_history[0][i][0] = i;
            clane_history[1][i][0] = i;
            last_return_clane[i] = i;
            plan_return_clane[i] = i;

        }

        int finish_task = 0;

        for (int turn = 1; turn < max_turn; turn++){

            for (int i = 0; i < n; i++){
                if (use_A[i] >= n || board_history[turn][i][0] != -1) continue;
                int a = A[i][use_A[i]];
                board_history[turn][i][0] = task_by_A[a][tasks_by_A_count[a]];
                tasks_by_A_count[a]++;
                use_A[i]++;
            }
            // if (turn == 20) break;
            // cerr << "turn = " << turn << " finish task = " << finish_task << endl;
            // for (int i = 0; i < n; i++){
            //     cerr << last_use_clane[i] << " ";
            // }
            // cerr << endl;
            // for (int i = 0; i < n; i++){
            //     for (int j = 0; j < n; j++){
            //         cerr << board_history[turn][i][j] << " ";
            //     }
            //     cerr << endl;
            // }
            // cerr << endl;

            // for (int i = 0; i < n; i++){
            //     for (int j = 0; j < n; j++){
            //         cerr << clane_history[turn][i][j] << " ";
            //     }
            //     cerr << endl;
            // }
            // cerr << endl;
            

            while (finish_task < tasks.size())
            {
                auto [a,x,y,nx,ny] = tasks[finish_task];

                // まだ boardにいないなら turnを進む
                if (board_history[turn][x][y] != finish_task) break;

                // taskを割り当てられたら 次のtaskへ
                if (apply_task(turn, 
                    finish_task,
                    last_use_clane, 
                    last_return_clane,
                    plan_return_clane,
                    finish_A_turn,
                    tasks[finish_task],
                    board_history,  
                    clane_history, 
                    clane_pos,
                    ans, plan_last_clane_use,
                    task_by_A,tasks_by_A_count,board_history2)){
                    assert_check(ans,clane_pos,clane_history);

                    finish_task++;
                } else{
                    break;
                }

            }
            if (finish_task == tasks.size()) break;


            // claneの状態を更新
            for (int i = 0; i < n; i++){
                // 戻る位置の更新
                if (last_use_clane[i] >= 0){
                    // cerr << "update end turn " << endl;
                    update_info up_info = update_return_clane(last_use_clane[i],i,clane_pos[i][last_use_clane[i]][0],clane_pos[i][last_use_clane[i]][1],
                            last_use_clane, 
                            finish_A_turn,
                            last_return_clane,
                            plan_return_clane,
                            board_history,  
                            clane_history, 
                            clane_pos,
                            ans,plan_last_clane_use);
                    assert (up_info.success != 0);
                    apply_update_info(up_info,last_return_clane,plan_return_clane,board_history,clane_history,clane_pos,ans,plan_last_clane_use);

                }
                
                // # なら何もしていないので今の状態を反映

                // for (int t = 0; t <= turn; t++){
                //     cerr << "[ " << ans[i][t] << " " << clane_pos[i][t][0] << " " << clane_pos[i][t][1] << "] " << " ";
                // }
                // cerr << endl;

                
                if (clane_pos[i][turn+1] == no_record){
                    clane_pos[i][turn+1] = clane_pos[i][turn];
                    auto [x,y,p] = clane_pos[i][turn];
                    // cerr << "i = " << i << " " << x << " " << y << " " << p << endl;
                    clane_history[turn+1][x][y] = i;

                } else{
                    // 違うなら clane の状態は反映されている
                }
            }
            // cerr << "clane ok" << endl;

            // boardの状態を更新
            // finish_task より小さい分の動きは history に反映ずみ
            // finish_task 以上の場合はまだ決まってないので今の位置に残っているとする
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    if (board_history[turn][i][j] >= 0 && board_history[turn][i][j] >= finish_task){
                        board_history[turn+1][i][j] = board_history[turn][i][j];
                    }
                }
            }
            // cout << "turn = " << turn << endl;
            // for (int i = 0; i < n; i++){
            //     for (int j = 0; j <= 20; j++){
            //         if (ans[i][j] == '#'){
            //             cout << '.';
            //         } else{
            //             cout << ans[i][j];
            //         }
            //     }
            //     cout << endl;
            // }

            assert_check(ans,clane_pos,clane_history);
        }
        if (finish_task != tasks.size()) return;

        int length = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < ans[i].size(); j++){
                if (ans[i][j] == 'Q'){
                    length = max(length,j);
                }
            }
        }

        for (int i = 0; i < n; i++){
            for (int j = 0; j <= length; j++){
                if (ans[i][j] == '#'){
                    ans[i][j] = '.';
                }    
                // cout << ans[i][j];
                
            }
            // cout << endl;
        }
       

        cerr << ans[0].size() << " " << length << endl;
        State state(n,A);
        for (int t = 0; t <= length; t++){
            vector<char> moves(n);
            for (int i = 0; i < n; i++){
                moves[i] = ans[i][t];
                // cerr << moves[i];
            }
            // cerr << endl;
            auto check = state.apply(moves);
            // assert (check);
            if (!check){
                for (int i = 0; i < n; i++){
                    if (state.pos[i][2] == -1){
                        ans[i][t] = '.';
                        moves[i] = ans[i][t];
                    }
                }
                state.apply(moves);
            }
            // assert (check);

        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j <= length; j++){
                if (ans[i][j] == '#'){
                    ans[i][j] = '.';
                }    
                cout << ans[i][j];
                
            }
            cout << endl;
        }
        
        cerr << "apply end" << endl;


        long long score =length;

        if (best_score > score){
            best_score = score;
        }
        cerr << "score = " << best_score << endl;

    }
    void solve(){
        // solve_greedy_single();

        vector<int> order = get_order_dp();
        vector<array<int,5>> tasks = get_tasks(order);
        decide_moves(tasks);

        
        // out_ans();

    }

    void out_ans(){
        for (auto a: best_ans){
            for (auto c: a){
                cout << c;
            }
            cout << endl;
        }
        cerr << "score = " << best_score << endl;
        exit(0);
    }
};
int main() {
    Input();
    Solver solver = Solver();
    solver.solve();

    
    return 0;
}