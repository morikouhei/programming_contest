#include <bits/stdc++.h>
using namespace std;

constexpr int TIME_LIM = 3;
const long long mod = 998244353;
const long long INF = 1e18;
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
            elapsed_time_ = chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time_).count();
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

int n,m,k;
vector<vector<long long>> A;
vector<vector<vector<long long >>> S;
struct stamp{
    vector<vector<long long >> matrix;

    stamp() : matrix(3, vector<long long>(3, 0ll)) {}
    stamp(vector<vector<long long>> ns):matrix(ns){}
};

vector<vector<vector<int>>> ord(4);
vector<vector<stamp>> stamps(4);
void Input() {
    cin >> n >> m >> k;
    A.resize(n);
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            long long a;
            cin >> a;
            A[i].push_back(a);
        }
    }
    S.resize(m);
    for (int i = 0; i < m; i++){
        S[i].resize(3);
        for (int x = 0; x < 3; x++){
            for (int y = 0; y < 3; y++){
                long long s;
                cin >> s;
                S[i][x].push_back(s);
            }
        }
    }
    ord[0].push_back({});
    for (int i = 0; i < m; i++){
        ord[1].push_back({i});
        stamps[1].push_back((stamp)S[i]);

        for (int j = 0; j < m; j++){

            ord[2].push_back({i,j});
            stamp base;

            for (int x = 0; x < 3; x++){
                for (int y = 0; y < 3; y++){
                    base.matrix[x][y] = (S[i][x][y]+S[j][x][y])%mod;
                }
            }
            stamps[2].push_back(base);

            for (int l = 0; l < m; l++){
                ord[3].push_back({i,j,l});
                stamp base;

                for (int x = 0; x < 3; x++){
                    for (int y = 0; y < 3; y++){
                        base.matrix[x][y] = (S[i][x][y]+S[j][x][y]+S[l][x][y])%mod;
                    }
                }
                stamps[3].push_back(base);

            }
        }
    }

};

pair<int,int> get_best(vector<vector<long long>>& sA, int x, int y, int wx, int wy, int ma){
    pair<int,int> ans; 
    long long best = 0;

    for (int xi = 0; xi < wx; xi++){
        for (int yi = 0; yi < wy; yi++){
            best += sA[x+xi][y+yi];
        }
    }
    ans = {0,0};

    for (int i = 1; i <= ma; i++){

        for (int j = 0; j < stamps[i].size(); j++){
            long long score = 0;
            for (int xi = 0; xi < wx; xi++){
                for (int yi = 0; yi < wy; yi++){
                    score += (sA[x+xi][y+yi]+stamps[i][j].matrix[xi][yi])%mod;
                }
            }
            if (score > best){
                best = score;
                ans = {i,j};
            }
        }
    }
    return ans;
}
struct Solver{

    void solve(){

        vector<vector<long long>> sA(n,vector<long long>(n,0));
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                sA[i][j] = A[i][j];
            }
        }

        vector<vector<int>> ans;

        for (int i = 0; i < n-2;i++){
            for (int j = 0; j < n-2; j++){
                int x,y;
                if (i == n-3){
                    if (j == n-3){
                        auto cand = get_best(sA,i,j,3,3,3);
                        x = cand.first;
                        y = cand.second;
                        
                    }
                    else{
                        auto cand = get_best(sA,i,j,3,1,3);
                        x = cand.first;
                        y = cand.second;
                        
                    }
                }
                else if( j == n-3){
                    auto cand = get_best(sA,i,j,1,3,3);
                    x = cand.first;
                    y = cand.second;
                    

                } else{
                    auto cand = get_best(sA,i,j,1,1,1);
                    x = cand.first;
                    y = cand.second;

                }

                for (auto id: ord[x][y]){
                    ans.push_back({id,i,j});
                }

                if (x){
                    stamp s = stamps[x][y];
                    for (int x = 0; x < 3; x++){
                        for (int y = 0; y < 3; y++){
                            sA[i+x][j+y] = (sA[i+x][j+y]+s.matrix[x][y])%mod;
                        }
                    }
                }
                
                

            }
        }
        cout << ans.size() << endl;

        for (int i = 0; i < ans.size(); i++){
            cout << ans[i][0] << " " << ans[i][1] << " " << ans[i][2] << endl;
        }


    }
};
int main() {
    Input();
    Solver solver = Solver();
    solver.solve();

    
    return 0;
}