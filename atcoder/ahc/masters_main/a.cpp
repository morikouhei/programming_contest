#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>
using namespace std;

const double INF = 1e18;
int n,m;
double eps,delta;
const int MAX_T = 5000;
const double M = 100000.0;
const int PARTICLE_SIZE = 3000;
const double POINT_BUFFER = 2000.0;


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

class P {
public:
    double x, y;

    // コンストラクタ
    P(double x = 0, double y = 0) : x(x), y(y) {}

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

    // 等価演算子
    bool operator==(const P& other) const {
        return (x == other.x) && (y == other.y);
    }

    // 不等価演算子
    bool operator!=(const P& other) const {
        return !(*this == other);
    }
    double dot(const P& a) const {
        return x * a.x + y * a.y;
    }

    double det(const P& a) const {
        return x * a.y - y * a.x;
    }

    double abs2() const {
        return dot(*this);
    }

    double abs() const {
        return sqrt(abs2());
    }

    static P gets(P cand, double lim){
        double now = cand.abs();
        P ret = cand * (lim / now);
        return ret;
    }

    // デバッグ用の出力演算子オーバーロード
    friend ostream& operator<<(ostream& os, const P& p) {
        return os << " " << p.x << " " << p.y << " ";
    }

    static double dist2_sp(const P& p1, const P& p2, const P& q) {
        if ((p2 - p1).dot(q - p1) <= 0.0) {
            return (q - p1).abs2();
        } else if ((p1 - p2).dot(q - p2) <= 0.0) {
            return (q - p2).abs2();
        } else {
            return dist2_lp(p1, p2, q);
        }
    }

    static double dist2_lp(const P& p1, const P& p2, const P& q) {
        double det = (p2 - p1).det(q - p1);
        return (det * det) / (p2 - p1).abs2();
    }

    static bool crs_sp(const P& p1, const P& p2, const P& q) {
        return (q - p1).dot(q - p2) <= 0.0;
    }

    static bool crs_lp(const P& p1, const P& p2, const P& q) {
        return (p2 - p1).det(q - p1) == 0.0;
    }

    static bool crs_ss(const P& p1, const P& p2, const P& q1, const P& q2) {
        auto sort = [](double a, double b) {
            return minmax(a, b);
        };

        auto [lp0, up0] = minmax(p1.x, p2.x);
        auto [lq0, uq0] = minmax(q1.x, q2.x);
        auto [lp1, up1] = minmax(p1.y, p2.y);
        auto [lq1, uq1] = minmax(q1.y, q2.y);

        if (up0 < lq0 || uq0 < lp0 || up1 < lq1 || uq1 < lp1) {
            return false;
        }
        return sig((p2 - p1).det(q1 - p1)) * sig((p2 - p1).det(q2 - p1)) <= 0
            && sig((q2 - q1).det(p1 - q1)) * sig((q2 - q1).det(p2 - q1)) <= 0;
    }

    static P proj(const P& p1, const P& p2, const P& q) {
        double d = (p2 - p1).abs2();
        if (d == 0.0) return p1;
        P r = p1 * d + (p2-p1) * (p2-p1).dot(q-p1);
        return P(r.x / d, r.y /d);
    }

    static P get_nearest(const P& p1, const P& p2, const P& q){
        if ((p2 - p1).dot(q - p1) <= 0.0) {
            return p1;
        } else if ((p1 - p2).dot(q - p2) <= 0.0) {
            return p2;
        } else {
            return P::proj(p1,p2,q);
        }

    }

    static P pi_ll(const P& p1, const P& p2, const P& q1, const P& q2) {
        double d = (q2 - q1).det(p2 - p1);
        if (d == 0.0) {
            return P(INF,INF);
        }
        P r = p1 * d + (p2 - p1) * (q2 - q1).det(q1 - p1);
        return P(r.x / d, r.y / d);
    }

    static int sig(double x) {
        if (x > 0) return 1;
        if (x < 0) return -1;
        return 0;
    }
};


double clamp(double x, double minV = -M+1, double maxV = M-1){
    if (x <= minV){
        return minV;
    }
    if (x >= maxV){
        return maxV;
    }
    return x;
}

double normal(double x, double mean, double stdDev) {
    double v = (x - mean) / stdDev;
    return exp(-0.5 * v * v);
}


Xorshift rng(998244353);
Timer timer;
double time_limit = 1.97;
mt19937 engine(998244353);




// PID制御器を表す構造体
struct PID {
    double kp, ki, kd;
    P integral, prev_error;
    int last_turn;

    PID(double kp, double ki, double kd, int last_turn) : kp(kp), ki(ki), kd(kd), integral(), prev_error(),last_turn(last_turn) {}

    static PID new_with_default(int last_turn=-1) {
        return PID(0.2, 5.8174518156417054e-05, 1.6,last_turn);
    }

    P update(const P& pos, const P& target, int turn) {
        P error = target - pos;
        integral = integral + error;
        P derivative = (error - prev_error) * 0.6 ;//(1.0/(turn -last_turn));
        prev_error = error;
        last_turn = turn;

        return error * kp + integral * ki + derivative * kd;
    }
};


vector<P> ps;
vector<bool> finished(10);

P position;
P velocity;
vector<pair<P,P>> walls;

void Input() {
    cin >> n >> m >> eps >> delta;
    double x,y;
    cin >> x >> y;
    position = P(x,y);
    velocity = P(0,0);
    ps.resize(n);
    for (int i = 0; i < n; i++){
        double x,y;
        cin >> x >> y;
        ps[i] = P(x,y);
        
    }
    walls.resize(m+4);
    for (int i = 0; i < m; i++){
        double x1,y1,x2,y2;
        cin >> x1 >> y1 >> x2 >> y2;

        walls[i] = {P(x1,y1),P(x2,y2)};
    }
    walls[m] = {P(-M,-M),P{M,-M}};
    walls[m+1] = {P(M,-M),P{M,M}};
    walls[m+2] = {P(M,M),P{-M,M}};
    walls[m+3] = {P(-M,M),P{-M,-M}};

    m += 4;

};

// 座標などの情報を管理
// 接触判定や tsp によるパスなども求める
struct Graph {
    vector<vector<double>> points_dists;
    vector<vector<vector<int>>> points_roots;
    vector<P> path_points;
    vector<pair<P,P>> walls;
    int path_points_num;
    double wall_buffer;

    bool need_update_path = true;
    vector<int> target_path_roots;
    int target_path_ind = 0;
    P target;

    Graph() : target_path_ind(0) {}
    Graph(vector<P> ps, vector<pair<P,P>> walls, double wall_buffer) : walls(walls), path_points(ps),wall_buffer(wall_buffer){
        build();
    }

    void build(){

        // for (int i = 0; i < n; i++){
        //     for (int j = 0; j < m-4; j++){
        //         auto [p1,p2] = walls[j];

        //         auto q = P::get_nearest(p1,p2,path_points[i]);
        //         P dif = path_points[i] - q;
        //         P buf = P::gets(dif,1.0);

        //         cout << "# p = " << path_points[i] << " wall = " << j << " q = " << q << endl;
        //         if (!hit_wall(path_points[i]-buf,q+buf)){
        //             cout << "# succeed p = " << path_points[i] << " wall = " << j << " q = " << q << endl;

        //             path_points.push_back((path_points[i]+q) * 0.5);
        //         }
        //     }
        // }

        // for (int i = 0; i < m-4; i++){
        //     auto [p1,p2] = walls[i];

        //     for (int j = 0; j < m-4; j++){
        //         if (i == j) continue;
        //         auto [np1,np2] = walls[j];

        //         if (np1 != p1 && np2 != p1){
        //             auto q = P::get_nearest(np1,np2,p1);
        //             P dif = p1 - q;
        //             P buf = P::gets(dif,1.0);
        //             if (!hit_wall(p1-buf,q+buf)){
        //                 path_points.push_back((p1+q) * 0.5);
        //             }
        //         }
                
        //         if (np1 != p2 && np2 != p2){
        //             auto q = P::get_nearest(np1,np2,p2);
        //             P dif = p2 - q;
        //             P buf = P::gets(dif,1.0);
        //             if (!hit_wall(p2-buf,q+buf)){
        //                 path_points.push_back((p2+q) * 0.5);
        //             }
        //         }
        //     }
        // }
        // 壁から線分方向に buffer だけ離した場所に頂点を作る
        for (int i = 0; i < m-4; i++){
            auto [p1,p2] = walls[i];
            
            P dif = p2 - p1;
            P buf = P::gets(dif,wall_buffer);
            path_points.push_back(p2 + buf);
            path_points.push_back(p1 - buf);
        }

        path_points_num = path_points.size();

        points_dists.resize(path_points_num);
        points_roots.resize(path_points_num);
        for (int i = 0; i < path_points_num; i++){
            points_dists[i].resize(path_points_num,INF);
            points_roots[i].resize(path_points_num);
        }

        // 壁に当たらない頂点間を辺で結ぶ
        for (int i = 0 ; i < path_points_num; i++){
            for (int j = 0; j < i; j++){
                if (hit_wall(path_points[i],path_points[j])) continue;

                // double d = (path_points[i]-path_points[j]).abs();
                double d = calc_edge_weight(path_points[i],path_points[j]);
                points_dists[i][j] = d;
                points_roots[i][j].push_back(j);
                points_dists[j][i] = d;
                points_roots[j][i].push_back(i);
            }
        }

        // ワーシャルフロイドで頂点間の最短距離とその時に通過する頂点集合を求めておく
        for (int k = 0; k < path_points_num; k++){
            for (int i = 0; i < path_points_num; i++){
                for (int j = 0; j < path_points_num; j++){
                    if (points_dists[i][k] == INF || points_dists[k][j] == INF) continue;
                    if (points_dists[i][j] <= points_dists[i][k] + points_dists[k][j]) continue;

                    points_dists[i][j] = points_dists[i][k] + points_dists[k][j];
                    points_roots[i][j].clear();
                    for (auto pos : points_roots[i][k]){
                        points_roots[i][j].push_back(pos);
                    }
                    for (auto pos : points_roots[k][j]){
                        points_roots[i][j].push_back(pos);
                    }
                }
            }
        }
        for (int i = 0; i < path_points_num; i++){
        cout << "# dist from = " << i << endl;
        cout << "# ";
        for (int j = 0; j < path_points_num; j++){
            cout << points_dists[i][j] << " ";
        }
        cout << endl;
    }

    }

    // 線分が壁にぶつかるかの判定 当たるなら true
    bool hit_wall(P p1, P p2){
        bool ok = false;
        for (int i = 0; i < m; i++){
            if (P::crs_ss(p1,p2,walls[i].first,walls[i].second)) ok = true;
        }
        return ok;
    }

    // p1 から p2 の線分で ポイントを通過するか 通過するなら true
    bool hit(P p1, P p2, int i, double d = 1e6){
        return P::dist2_sp(p1,p2,path_points[i]) <= d;
    }

    double calc_wall_distance(P p1, P p2){
        double dist = INF;
        for (int i = 0; i < m; i++){
            dist = min(dist,P::dist2_sp(walls[i].first,walls[i].second,p1));
            dist = min(dist,P::dist2_sp(walls[i].first,walls[i].second,p2));
            dist = min(dist,P::dist2_sp(p1,p2,walls[i].first));
            dist = min(dist,P::dist2_sp(p1,p2,walls[i].second));
        }
        return dist;
    }
    double calc_edge_weight(P p1, P p2){
        double dist = (p1 - p2).abs();
        double wall_dist = calc_wall_distance(p1,p2);
        if (wall_dist < POINT_BUFFER){
            dist *= 1.0 + 5e-4 * eps * log2((POINT_BUFFER / max(wall_dist,1.0)));
        }
        return dist;

    }

    // p1 から dir 方向で最も近い壁との距離 必ず見つかる
    double nearest_wall(P p1, P dir){
        double dist = INF;
        P p2 = p1 + dir;
        for (int i = 0; i < m; i++){
            P cand = P::pi_ll(p1,p2,walls[i].first,walls[i].second);
            if (abs(cand.x - INF) < 1e-8) continue;;
            if ( P::sig(dir.det(walls[i].first-p1)) * P::sig(dir.det(walls[i].second-p1)) <= 0 && (cand-p1).dot(dir) >= 0){
                double dcand = (cand-p1).abs();
                if (dist > dcand){
                    dist = dcand;
                }
            } 
        }
        return dist;
    }

    // 粒子の候補に対して dir 方向の計測を行った時に期待される 距離の分散/距離の平均, 大きいほど嬉しい 
    double get_direction_var(vector<pair<P,P>> &particle_candidate, P dir){

        vector<double> ds;
        long double ds_sum = 0;
        for (auto &c: particle_candidate){
            double d = nearest_wall(c.first,dir);

            if (abs(d - INF) < 1e-8){
                assert (false);
            }
            ds.push_back(d);
            ds_sum += d;
            
        }
        long double avg = ds_sum / ds.size();
        long double var = 0;
        for (auto d: ds){
            var += (d-avg) * (d-avg);
        }
        var /= ds.size();

        return sqrt(var)/avg;
    }

    // 現在位置から次の目標までに壁がある場合、 ポイントを通過した場合は tsp で 次の目標を決める
    void update_target_root(P position){

        if (need_update_path == false){
            if (hit_wall(position,target)){
                need_update_path = true;
            }
        }

        if (need_update_path == false) return ;
        need_update_path = false;
        target_path_roots.clear();
        target_path_ind = 0;

        // pid = PID::new_with_default(turn-1);

        vector<double> dists(path_points_num,INF);
        vector<vector<int>> paths(path_points_num);
        priority_queue<pair<double,int>> h;
        for (int i = 0; i < path_points_num; i++){
            if (hit_wall(position,path_points[i])) continue;
            dists[i] = (position-path_points[i]).abs();
            h.push({-dists[i],i});
            paths[i].push_back(i);
        }

        while (!h.empty()){
            auto [d,now] = h.top();
            h.pop();
            for (int nex = 0; nex < path_points_num; nex++){
                double nd = -d + points_dists[now][nex];
                if (nd < dists[nex]){
                    dists[nex] = nd;
                    h.push({-nd,nex});
                    paths[nex].clear();

                    for (auto pos : paths[now]){
                        paths[nex].push_back(pos);
                    }
                    for (auto pos : points_roots[now][nex]){
                        paths[nex].push_back(pos);
                    }
                }
            }
        }
        int is_end = 0;
        int n2 = 1<<n;
        for (int i = 0; i < n; i++){
            if (finished[i]) is_end |= 1<<i;
        }

        pair<int,int> empty = {-1,-1};
        vector<vector<double>> dp(n,vector<double>(n2,INF));
        vector<vector<pair<int,int>>> par(n,vector<pair<int,int>>(n2,empty));

        for (int i = 0; i < n; i++){
            if (finished[i]) continue;
            dp[i][is_end|1<<i] = dists[i];
        }
        for (int bi = 0; bi < n2; bi++){
            for (int i = 0; i < n; i++){
                if (dp[i][bi] == INF) continue;
                for (int ni = 0; ni < n; ni++){
                    if (bi >> ni & 1) continue;
                    if (points_dists[i][ni] == INF) continue;
                    int nbi = bi | 1 << ni;
                    int ndist = dp[i][bi] + points_dists[i][ni];
                    if (ndist < dp[ni][nbi]){
                        par[ni][nbi] = {i,bi};
                        dp[ni][nbi] = ndist;
                    }
                }
            }
        }
        double mi = INF;
        pair<int,int> last;
        for (int i = 0; i < n; i++){
            if (dp[i][n2-1] == INF) continue;

            if (mi > dp[i][n2-1]){
                mi = dp[i][n2-1];
                last = {i,n2-1};
            }
        }

        while (true){
            auto p = par[last.first][last.second];
            if (p != empty){
                last = p;
                continue;
            }
            target_path_roots = paths[last.first];
            target = path_points[target_path_roots[0]];
            break;
        }
    
        cout << "# new targets path" << endl;
        cout << "# ";
        for (auto ind : target_path_roots){
            cout << ind << " ";
        }
        cout << endl;
    }

    void update_targets(P position, P velocity){
        if (need_update_path) return ;
        if (target_path_roots[target_path_ind] >= n || finished[target_path_roots[target_path_ind]]){
            if (hit(position,position+velocity,target_path_roots[target_path_ind])){
                target_path_ind++;
                target = path_points[target_path_roots[target_path_ind]];

            }
        }
    }

};

struct ParticleFilter {
    P position;
    P velocity;
    vector<pair<P,P>> particle_candidate;
    int particle_num;
    double sigma;

    
    ParticleFilter() : particle_num(PARTICLE_SIZE){}
    ParticleFilter(vector<pair<P,P>> particle_candidate, int particle_num) : particle_candidate(particle_candidate),particle_num(particle_num){
        update_current_state();
    }

    void update_current_state(){

        position = P();
        velocity = P();
        sigma = 0;
        for (auto &[np,nv] : particle_candidate){
            np.x = clamp(np.x);
            np.y = clamp(np.y);
            position = position + np;
            velocity = velocity + nv;
        }
        position = position * (1.0 / particle_candidate.size());
        velocity = velocity * (1.0 / particle_candidate.size());

        sigma = 0;
        for (auto &[np,nv]: particle_candidate){
            sigma += (np - position).abs2();
        }
        sigma /= particle_candidate.size();
        sigma = sqrt(sigma);
    }

    // 壁に当たったら速度を 0 にする
    void reset_velocity(){
        for (auto &cand: particle_candidate){
            cand.second = P(0,0);
        }
    }

    // パーティクルに速度分の変化を反映
    void position_update(){
        for (auto &cand: particle_candidate){
            cand.first = cand.first + cand.second;
        }
    }

    // パーティクルの不足分を補充する
    void fill_particle(vector<pair<P,P>> &nparticle_candidate){
        swap(particle_candidate,nparticle_candidate);
        while (particle_candidate.size() < particle_num){
            particle_candidate.push_back(particle_candidate[rng.randrange(particle_candidate.size())]);
        }
    }

    // パーティクルに加速クエリを反映
    void apply_accel(P accel){
        for (auto &c: particle_candidate){
            c.second = c.second + accel;
        }
    }

    // パーティクルに計測クエリを反映
    // 確率による重み付きで更新する
    void apply_measurement(P measure, Graph &graph){

        double res;
        cin >> res;

        cout << "# measurement result = " << res << endl;

        vector<double> probs;
        for (auto &cand: particle_candidate){
            double d = graph.nearest_wall(cand.first,measure);
            double alpha = res / max(1e-9,d);
            probs.push_back(max(normal(alpha,1.0,delta),1e-18));
        }

        discrete_distribution weighted(probs.begin(),probs.end());

        vector<pair<P,P>> nparticle_candidate;

        for (int _ = 0; _ < particle_num; _++){
            nparticle_candidate.push_back(particle_candidate[weighted(engine)]);
        }

        swap(particle_candidate,nparticle_candidate);

    }
    
    // 行動後の結果による更新
    pair<int,int> update_from_result(Graph &graph){
        
        mt19937 gen(998244353);
        normal_distribution<double> normal_dist(0.0,eps);

        int c,h;
        cin >> c >> h;
        cout << "# c = " << c << " h = " << h << endl;

        vector<bool> new_finished(n);

        if (h){
            for (int i = 0 ; i < h; i++){
                int x;
                cin >> x;
                new_finished[x] = true;
            }
        }

        vector<pair<P,P>> saved = particle_candidate;

        // アクションの結果と一致する候補を風の影響も踏まえて生成する
        int empty = 0;
        for (int _ = 0; _ < 10; _++){
            for (auto &cand : particle_candidate){
                double r1 = normal_dist(engine);
                double r2 = normal_dist(engine);
                cand.second.x += r1;
                cand.second.y += r2;
            }

            // 壁と当たるかの判定が結果と一致するか
            vector<pair<P,P>> nparticle_candidate;
            for (auto &cand: particle_candidate){
                if (graph.hit_wall(cand.first,cand.first+cand.second) == c){
                    nparticle_candidate.push_back(cand);
                }
            }

            if (nparticle_candidate.size()){
                fill_particle(nparticle_candidate);

            } else{
                particle_candidate = saved;
                empty++;
                continue;  
            }

            // 壁に当たったなら速度を 0 にして完了
            if (c == 1){

                reset_velocity();

                for (int i = 0; i < n; i++){
                    if (new_finished[i]) finished[i] = true;
                }

                return {c,h};

            } else{
                // 壁に当たってないなら h の通過判定が一致するかを確認

                position_update();

                bool ok = true;

                for (int i = 0; i < n; i++){
                    if (finished[i]) continue;

                    nparticle_candidate.clear();
                    // 頂点の通過判定が結果と一致するか
                    for (auto &cand: particle_candidate){
                        if (graph.hit(cand.first-cand.second,cand.first,i) == new_finished[i]){
                            nparticle_candidate.push_back(cand);
                        }
                    }

                    if (nparticle_candidate.size()){
                        fill_particle(nparticle_candidate);
                    } else{
                        particle_candidate = saved;
                        ok = false;
                        break;
                    }
                }
                if (!ok){
                    empty++;
                    continue;
                }
                // 通過判定も一致したのでリターン
                for (int i = 0; i < n; i++){
                    if (new_finished[i]) finished[i] = true;
                }
                return {c,h};
            }
        
        }
        // 全滅した
        for (int i = 0; i < n; i++){
            if (new_finished[i]) finished[i] = true;
        }
        // 壁に当たってたら今の候補をランダムでバラす
        if (c == 1){
            for (auto &cand: particle_candidate){
                cand.first.x += 2e4 * rng.uniform(-1.0,1.0);
                cand.first.y += 2e4 * rng.uniform(-1.0,1.0);
                cand.second = P(0,0);
            }
            
        } else{
            // 壁に当たってないなら速度は反映する
            position_update();

            // 通過判定があったらその近くにいたことにする
            for (int i = 0; i < n; i++){
                if (new_finished[i]){
                    for (auto &cand: particle_candidate){
                        cand.first = ps[i] + cand.second;
                    }

                }
            }
        }
        
        
        cout << "# empty = " << empty << endl;

        if (h || particle_num != particle_candidate.size()) return {c,h};

        // 全滅したら一時的に候補を増やす
        for (int i = 0; i < particle_num; i++){
            auto cand = particle_candidate[i];
            cand.first.x += 2e4 * rng.uniform(-1.0,1.0);
            cand.first.y += 2e4 * rng.uniform(-1.0,1.0);
            if (c == 0){
                cand.second.x *= rng.uniform(0.9,1.1);
                cand.second.y += rng.uniform(0.9,1.1);
            }
            particle_candidate.push_back(cand);
        }

        return {c,h};
    }
};


struct Solver{
    ParticleFilter particleFilter;
    Graph graph;
    int turn = 0;
    int hit_count = 0;

    PID pid = PID::new_with_default();

    // 終了判定
    void is_finish(){
        bool ok = true;
        for (int i = 0; i < n; i++){
            if (finished[i] == false) ok = false;
        }
        if (ok){
            exit(0);
        }
    }

    void accel_query(P a){
        a = P((int)a.x,(int)a.y);
        cout << "A " << (int)a.x << " " << (int)a.y << endl;

        particleFilter.apply_accel(a);
    }

    void measurement_query(P a){
        
        a = P((int)a.x,(int)a.y);
        cout << "S " << (int)a.x << " " << (int)a.y << endl;

        particleFilter.apply_measurement(a,graph);
    }

    P decide_next_target(){

        graph.update_target_root(particleFilter.position);
        return graph.target;
    }

    double max_velocity(double distance){
        if (eps == 0.0){
            return sqrt(0.9 * 2.0 * 500.0 * distance);
        } else{
            return sqrt(0.9 * 500 * distance);
        }
    }

    P decide_accel(P target){
        P dir = target - particleFilter.position;

        P acc = P::proj(P(),dir,particleFilter.velocity);
        bool approaching = dir.dot(acc) > 0.0;
        P fix = acc - particleFilter.velocity;

        if (fix.abs() > 498.0){
            return P::gets(fix,498.0);
        } else{
            double max_proceed = sqrt((500.0*500.0 - fix.abs2()));
            double proceed = max_velocity(dir.abs());
            if (approaching){
                proceed -= acc.abs();
            } else{
                proceed += acc.abs();
            }

            proceed = clamp(proceed,-max_proceed,max_proceed);

            return fix + P::gets(dir,proceed);
        }
    }

    void next_action(P target, double sigma, int turn){
        
        cout << "# target = " << target << endl;
        P a = decide_accel(target);

        // 条件を満たせば加速
        if (a != P() && (turn%2 == 0 || eps == 0.0 || sigma < 1000.0)){
            accel_query(a);
            return ;
        }

        // 計測の方向を最適化

        vector<P> cand;
        for (int i = 0; i < m; i++){
            if (i < m-4){
                cand.push_back(walls[i].first-particleFilter.position);
                cand.push_back(walls[i].second-particleFilter.position);
            } else{
                cand.push_back(walls[i].first-particleFilter.position);
            }
            cand.push_back(P::proj(walls[i].first,walls[i].second,particleFilter.position) - particleFilter.position);
        }
        vector<P> ncand;
        swap(cand,ncand);

        for (auto v: ncand){
            double d = v.abs();
            if (d > 1e5){
                v = v * (99998.0 / d);
            }
            v = P((int)v.x,(int)v.y);
            if (v.abs2() > 0.0){
                cand.push_back(v);
            }
        }
        vector<P> targets(2);

        if (false){//timer.get_time() >= 1.5){
            vector<double> scores(2,INF);

            for (auto dir: cand){
                double d = graph.nearest_wall(particleFilter.position,dir);
                if (d < scores[1]){
                    scores[1] = d;
                    targets[1] = dir;
                } else{
                    continue;
                }
                if (scores[1] < scores[0]){
                    swap(scores[1],scores[0]);
                    swap(targets[1],targets[0]);
                }
            }
        } else {
            vector<double> scores(2,-1.0);
            for (auto dir : cand){
                double d = graph.get_direction_var(particleFilter.particle_candidate,dir);
                if (d > scores[1]){
                    scores[1] = d;
                    targets[1] = dir;
                } else{
                    continue;
                }
                if (scores[1] > scores[0]){
                    swap(scores[1],scores[0]);
                    swap(targets[1],targets[0]);
                }
            }
        }
        cout << "# measure " << endl;
        if (rng.randrange(0,4) < 4){
            measurement_query(targets[0]);
        } else{
            measurement_query(targets[1]);
        }
    }

    void escape(int turn){
        for (int t = turn ; t < MAX_T; t++){
            cout << "A 0 0" << endl; 
        }
        exit(0);
    }

    void solve(){

        vector<pair<P,P>> candidate(PARTICLE_SIZE,{position,velocity});
        particleFilter = ParticleFilter(candidate,PARTICLE_SIZE);
        graph = Graph(ps,walls,POINT_BUFFER);
        
        for (int t = 0; t < MAX_T; t++){
            cout << "#turn = " << t << " eps = " << eps << " delta = " << delta << endl;
            // cout << "# ";
            // for (auto f : finished){
            //     cout << (int)f << " ";
            // }
            // cout << endl;
            // 全て通過したら終了
            is_finish();

            if (!timer.yet(time_limit)){
                escape(t);
            }

            // 推定情報を更新
            particleFilter.update_current_state();

            cout << "#p_pred = " << particleFilter.position << endl;
            cout << "#v_pred = " << particleFilter.velocity << endl;
            cout << "#sigma = " << particleFilter.sigma << endl;

  
            // 次の目標を決定
            P target = decide_next_target();

            // 行動を決定
            next_action(target,particleFilter.sigma,t);

            // 結果による更新
            auto [c,h] = particleFilter.update_from_result(graph);

            if (h){
                graph.need_update_path = true;
            }

            graph.update_targets(particleFilter.position,particleFilter.velocity);
        }

        cout << "#end at " << timer.get_time() << endl;
        
    }
};
int main() {
    Input();
    Solver solver = Solver();
    solver.solve();

    
    return 0;
}