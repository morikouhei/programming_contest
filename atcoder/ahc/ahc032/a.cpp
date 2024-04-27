#include <bits/stdc++.h>
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

class P {
public:
    double x, y;

    // コンストラクタ
    P(double x = 0.0, double y = 0.0) : x(x), y(y) {}

    // 加算演算子のオーバーロード
    P operator+(const P& a) const {
        return P(x + a.x, y + a.y);
    }

    // 減算演算子のオーバーロード
    P operator-(const P& a) const {
        return P(x - a.x, y - a.y);
    }

    // スカラー乗算演算子のオーバーロード
    P operator*(double a) const {
        return P(x * a, y * a);
    }

    // デバッグ用の出力演算子オーバーロード
    friend std::ostream& operator<<(std::ostream& os, const P& p) {
        return os << "(" << p.x << ", " << p.y << ")";
    }
};

int n,m;
double eps,sigma;
const int MAX_T = 5000;
vector<P> ps;
P pos;
vector<pair<P,P>> walls;
void Input() {
    cin >> n >> m >> eps >> sigma;
    double x,y;
    cin >> x >> y;
    pos = P(x,y);
    ps.resize(n);
    for (int i = 0; i < n; i++){
        double x,y;
        cin >> x >> y;
        ps[i] = P(x,y);
        
    }
    walls.resize(m);
    for (int i = 0; i < m; i++){
        double x1,y1,x2,y2;
        cin >> x1 >> y1 >> x2 >> y2;

        walls[i] = {P(x1,y1),P(x2,y2)};
    }
    cout << pos << endl;

    
};


struct Solver{

    void solve(){
        P v = {0.0,0.0};

        

        // vector<vector<long long>> sA(n,vector<long long>(n,0));
        // for (int i = 0; i < n; i++){
        //     for (int j = 0; j < n; j++){
        //         sA[i][j] = A[i][j];
        //     }
        // }

        // vector<vector<int>> ans;

        // for (int i = 0; i < n-2;i++){
        //     for (int j = 0; j < n-2; j++){
        //         int x,y;
        //         if (i == n-3){
        //             if (j == n-3){
        //                 auto cand = get_best(sA,i,j,3,3,3);
        //                 x = cand.first;
        //                 y = cand.second;
                        
        //             }
        //             else{
        //                 auto cand = get_best(sA,i,j,3,1,3);
        //                 x = cand.first;
        //                 y = cand.second;
                        
        //             }
        //         }
        //         else if( j == n-3){
        //             auto cand = get_best(sA,i,j,1,3,3);
        //             x = cand.first;
        //             y = cand.second;
                    

        //         } else{
        //             auto cand = get_best(sA,i,j,1,1,1);
        //             x = cand.first;
        //             y = cand.second;

        //         }

        //         for (auto id: ord[x][y]){
        //             ans.push_back({id,i,j});
        //         }

        //         if (x){
        //             stamp s = stamps[x][y];
        //             for (int x = 0; x < 3; x++){
        //                 for (int y = 0; y < 3; y++){
        //                     sA[i+x][j+y] = (sA[i+x][j+y]+s.matrix[x][y])%mod;
        //                 }
        //             }
        //         }
                
                

        //     }
        // }
        // cout << ans.size() << endl;

        // for (int i = 0; i < ans.size(); i++){
        //     cout << ans[i][0] << " " << ans[i][1] << " " << ans[i][2] << endl;
        // }


    }
};
int main() {
    Input();
    Solver solver = Solver();
    solver.solve();

    
    return 0;
}