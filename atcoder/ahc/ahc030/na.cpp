
#include <bits/stdc++.h>
using namespace std;

mt19937 gen(998244353);
constexpr int TIME_LIM = 3;
constexpr double INF = 1e9;

class Xorshift {
    public:
        Xorshift(uint32_t seed): x_(seed) {
            assert(seed);
        }

        uint32_t randrange(uint32_t stop) {
            // [0, stop)
            assert(stop > 0);
            next();
            return x_ % stop;
        }

        uint32_t randrange(uint32_t start, uint32_t stop) {
            // [start, stop)
            assert(start < stop);
            next();
            return start + x_ % (stop - start);
        }

        uint32_t randint(uint32_t a, uint32_t b) {
            // [a, b]
            assert(a <= b);
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
double time_limit = 2.95;
double time_early_lim = 100;

vector<int> DX = {1, 0, -1, 0,1,1,-1,-1,0};
vector<int> DY = {0, 1, 0, -1,1,-1,1,-1,0};
double memo[200][200][200];

struct Block {
    int block_size;
    int max_x;
    int max_y;
    vector<array<int, 2>> block_list;

    Block(const vector<int>& l) {
        block_size = l[0];
        max_x = 0;
        max_y = 0;

        for (size_t i = 0; i < block_size; ++i) {
            int x = l[2 * i + 1];
            int y = l[2 * i + 2];
            block_list.push_back({x, y});
            max_x = max(x, max_x);
            max_y = max(y, max_y);
        }
    }
};

int atcoder = 0;

int n, m;
double eps;
vector<Block> Blocks;
int Block_sum = 0;
int n2;

void Input() {
    cin >> n >> m >> eps;
    n2 = n * n;

    if (m > 3){
        exit(0);
    }

    if (getenv("ATCODER")) {
        atcoder = 1;
        time_early_lim = 2.85;
    }

    for (int i = 0; i < m; ++i) {
        vector<int> l;
        int le;
        cin >> le;
        l.push_back(le);
        for (int i = 0; i < 2*le; i++){
            int x;
            cin >> x;
            l.push_back(x);
        }
        Block_sum += le;
        Blocks.push_back(l);
    }
}

// 正規分布における確率の取得
double normal_cdf(double x, double mean, double variance) {
    double z = (x - mean) / sqrt(variance);
    return (1 + erf(z / sqrt(2))) / 2;
}

double probability_in_interval(double start, double end, double mean, double variance) {
    return normal_cdf(end, mean, variance) - normal_cdf(start, mean, variance);
}

double get_normal_dist_interval(int now_num, int now_res, int k) {
    if (memo[now_num][now_res][k] != INF){
        return memo[now_num][now_res][k];
    }

    double mu = (k - now_num) * eps + now_num * (1.0 - eps);
    double sigma = k * eps * (1.0 - eps);
    double prob;
    if (now_res == 0) {
        prob = normal_cdf(0.5, mu, sigma);
    } else {
        prob = probability_in_interval(now_res - 0.5, now_res + 0.5, mu, sigma);
    }
    if (prob) {
        prob = log(prob);
    } else {
        prob = -100;
    }
    memo[now_num][now_res][k] = prob;

    // cout << "#c prob " << now_num << " " << now_res << " " << prob << " " << k << endl;
    return prob;
}
//

struct Environment {
    int query_time;
    int oil_num;
    double cost;

    vector<array<int, 2>> Block_pos_list;
    vector<vector<int>> V;
    vector<double> errors;

    

    Environment() : query_time(0), oil_num(0), cost(0) {
    }

    void build() {
        if (atcoder) {
            return;
        }

        for (int i = 0; i < m; ++i) {
            int x, y;
            cin >> x >> y;
            Block_pos_list.push_back({x, y});
        }

        V.resize(n, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> V[i][j];
                if (V[i][j] != 0) {
                    oil_num++;
                }
            }
        }

        errors.resize(2 * n2);
        for (int i = 0; i < 2 * n2; ++i) {
            cin >> errors[i];
        }
    }

    int ask_query(const vector<array<int, 2>>& ask_list) {
        query_time++;

        assert(query_time <= 2 * n2);

        int k = ask_list.size();
        if (k == 1) {
            cost += 1;
        } else {
            cost += 1 / sqrt(k);
        }

        cout << "q " << k;
        for (auto [x, y] : ask_list) {
            cout << " " << x << " " << y;
            assert(0 <= x && x < n && 0 <= y && y < n);
        }
        cout << endl;
        int res;
        if (atcoder) {
            cin >> res;
        } else {
            if (k == 1) {
                int x = ask_list[0][0];
                int y = ask_list[0][1];
                res = V[x][y];
            } else {
                int count = 0;
                for (auto [x, y] : ask_list) {
                    count += V[x][y];
                }
                double mu = (k - count) * eps + count * (1.0 - eps);
                double sigma = sqrt(k * eps * (1.0 - eps));
                res = max(static_cast<int>(round(mu + errors[query_time - 1] * sigma)), 0);
            }
        }
        return res;
    }

    int answer_query(const vector<array<int, 2>>& ans_list) {
        query_time++;

        assert(query_time <= 2 * n2);

        int k = ans_list.size();

        cout << "a " << k;
        for (auto [x, y] : ans_list) {
            cout << " " << x << " " << y;
            assert(0 <= x && x < n && 0 <= y && y < n);
        }
        cout << endl;

        int res;

        if (atcoder) {
            cin >> res;
        } else {
            if (k != oil_num) {
                res = 0;
            } else {
                res = 1;
                for (auto [x, y] : ans_list) {
                    if (V[x][y] == 0) {
                        res = 0;
                        break;
                    }
                }
            }
        }

        if (res) {
            out_score();
            exit(0);
        } else {
            cost += 1;
            return res;
        }
        
    }

    void comment(const string& comment) {
        // comment = "#c " + comment
        cout << "#c " << comment << endl;
    }

    void out_score() {
        int cost_int = round(1e6 * max(1.0 / n, cost));
        comment(to_string(timer.get_time()));
        comment("cost = " + to_string(cost_int));
    }
};

Environment environment;


struct BlockChange {
    int bind;
    array<int, 2> pos;
};

struct QueryChange {
    int qind;
    int nweight;
    double nprob;
};

struct StateChange {
    int px;
    int py;
    int nstate;
    int npena;
};

struct UpdateChange {
    vector<BlockChange> blockchange;
    vector<QueryChange> querychange;
    vector<StateChange> statechange;
};

// Define Environment struct
struct State {
    int query_time = 0;
    double query_cost = 0;
    int query_size = 4;
    int score_last_update = 0;

    vector<vector<vector<int>>> query_info_list;
    vector<vector<int>> V_fixed;

    vector<vector<int>> state;
    vector<vector<int>> state_changes;
    vector<vector<int>> state_pena;
    vector<vector<double>> state_query_weight;

    vector<int> query_weight;
    vector<int> query_ans;
    vector<int> query_length;

    vector<vector<array<int, 2>>> query_list;
    vector<int> query_changes;
    vector<array<int,2>> block_pos_list;
    vector<double> query_score;

    double score = 0.0;

    // Constructor
    explicit State(int n) : state(n, vector<int>(n, 0)),state_query_weight(n, vector<double>(n, 1.0)),state_changes(n, vector<int>(n, 0)), state_pena(n, vector<int>(n, 0)),V_fixed(n, vector<int>(n, -1)),query_info_list(n, vector<vector<int>>(n)) {
        _build();
    }

    int can_put_block(int ind, int x, int y) {
        Block block = Blocks[ind];
        if (block.max_x+x >= n || block.max_y+y >= n || x < 0 || y < 0){
            return 0;
        }
        return 1;
    }

    int get_state_pena(int state, int x, int y) {

        int v = V_fixed[x][y];

        if (v == -1 || v == state){
            return 0;
        }
        if (v == 0){
            return -state * 1000;
        }
        return -abs(v-state)*100;
    }

    int query(const vector<array<int,2>>& q) {

        int k = q.size();

        if (k == 1){
            query_cost += 1.0;
        } else{
            query_cost += 1 / sqrt(k);
        }

        int res = environment.ask_query(q);

        if (k == 1) {
            return res;
        }

        query_ans.push_back(res);
        query_weight.push_back(0);
        query_list.push_back(q);
        query_changes.push_back(0);
        query_length.push_back(q.size());
        
        double res_weight = (double)res / k;
        for (auto& [x,y] : q){
            query_info_list[x][y].push_back(this->query_time);
            state_query_weight[x][y] += res_weight;
        }

        this->query_time++;
        return res;

    }

    // Member functions
    void _build() {

        int grid_len = 1;
        for (int x = 0; x < n; x++){
            if (x*grid_len >= n) break;

            int lx = x*grid_len;
            int rx = lx+grid_len;
            if (rx > n){
                int dif = rx-n;
                lx -= dif;
                rx -= dif;
            }

            vector<array<int,2>> q;
            for (int y = 0; y < n; y++) {
                for (int i = lx; i < rx;i++){
                    q.push_back({i, y});
                }
                
            }
            query(q); 
        }

        for (int y = 0; y < n; y++){
            if (y*grid_len >= n) break;

            int ly = y*grid_len;
            int ry = ly+grid_len;
            if (ry > n){
                int dif = ry-n;
                ly -= dif;
                ry -= dif;
            }
            vector<array<int,2>> q;
            for (int x = 0; x < n; x++) {
                for (int i = ly; i < ry;i++){
                    q.push_back({x, i});
                }
            }
            query(q); 
        
        }


        for (int bdif : {0}) {

            for (int i = 0; i < n; ++i) {

                if (i * query_size + bdif >= n) break;

                for (int j = 0; j < n; ++j) {

                    if (j * query_size + bdif >= n) break;

                    int lx = i * query_size + bdif;
                    int rx = lx + query_size;
                    int ly = j * query_size + bdif;
                    int ry = ly + query_size;

                    if (rx > n){
                        int dif = rx-n;
                        lx -= dif;
                        rx -= dif;
                    }

                    if (ry > n){
                        int dif = ry-n;
                        ly -= dif;
                        ry -= dif;
                    }


                    vector<array<int,2>> q;
                    for (int x = lx; x < rx; ++x) {
                        for (int y = ly; y < ry; ++y) {
                            q.push_back({x, y});
                        }
                    }

                    int same = 0;

                    for (auto& nq: query_list){
                        if (nq == q){
                            same = 1;
                        }
                    }
                    if (same) continue;

                    query(q); // 仮定: queryメソッドが結果をintで返す
                }
            }
        }

        for (int x = 0; x < n ; x++){
            for (int y = 0; y < n; y++){
                assert (query_info_list[x][y].size());

                state_query_weight[x][y] /= query_info_list[x][y].size();
            }
        }

        for (int ind = 0; ind < m; ++ind) {
            int x,y;
            while (true) {
                x = rng.randint(0,n-1);
                y = rng.randint(0,n-1);

                if (can_put_block(ind, x, y)) {
                    block_pos_list.push_back({x, y});
                    break;
                }
            }

            for (auto& [nx, ny] : Blocks[ind].block_list) {
                state[x + nx][y + ny] += 1;
            }
        }

        // クエリリストを使ったスコアの計算
        for (int i = 0; i < query_list.size(); ++i) {
            int count = 0;

            for (auto [x,y]: query_list[i]){
                count += state[x][y];
            }

            query_weight[i] = count;

            double prob = get_normal_dist_interval(count,query_ans[i],query_length[i]);
            query_score.push_back(prob);
            score += prob;
        }
    }

    pair<double, pair<vector<QueryChange>,vector<StateChange>>> get_change_info(const set<int>& query_change, const set<pair<int, int>>& state_change) {
        double score_dif = 0.0;

        vector<QueryChange> query_changes_result;
        vector<StateChange> state_changes_result;

        for (int qind : query_change) {
            if (query_changes[qind] == 0) continue;

            int nweight = query_weight[qind] + query_changes[qind];
            double nprob = get_normal_dist_interval(nweight, query_ans[qind], query_length[qind]);

            score_dif += nprob - query_score[qind];
            query_changes_result.push_back({qind, nweight, nprob});
            query_changes[qind] = 0;
        }


        for (const auto& [px, py] : state_change) {
            if (state_changes[px][py] == 0) continue;

            int nstate = state[px][py] + state_changes[px][py];
            int npena = get_state_pena(nstate, px, py);
            score_dif += npena - state_pena[px][py];
            state_changes_result.push_back({px,py,nstate, npena});

            state_changes[px][py] = 0;
        }

        return {score_dif, {query_changes_result,state_changes_result}}; 
    }

    void apply_query_res(int res, array<int,2> pos){
        auto [x,y] = pos;
        V_fixed[x][y] = res;
        score -= state_pena[x][y];
        state_pena[x][y] = get_state_pena(state[x][y], x, y);
        score += state_pena[x][y];

    }

    void update_state(double score_dif, UpdateChange updateChange){

        score += score_dif;

        for (BlockChange& bc : updateChange.blockchange){
            block_pos_list[bc.bind] = bc.pos;
        }

        for (QueryChange& qc : updateChange.querychange){
            query_weight[qc.qind] = qc.nweight;
            query_score[qc.qind] = qc.nprob;
        }

        for (StateChange& sc : updateChange.statechange){
            state[sc.px][sc.py] = sc.nstate;
            state_pena[sc.px][sc.py] = sc.npena;
        }
        
    }
    // Block 1つをランダムな位置に移動
    pair<double, UpdateChange> neighbor1(){
        int bind = rng.randint(0, m - 1);

        Block block = Blocks[bind];

        auto [x, y] = block_pos_list[bind];

        int nx = rng.randint(0, n - 1);
        int ny = rng.randint(0, n - 1);

        if (x == nx && y == ny){
            UpdateChange up;
            return {INF,up};
        }

        if (!can_put_block(bind, nx, ny) ){
            UpdateChange up;
            return {INF,up};
        }

        set<int> query_change;
        set<pair<int,int>> state_change;

        for (auto& [bx, by] : block.block_list){

            for (auto qind :query_info_list[x + bx][y + by]){
                query_change.insert(qind);
                query_changes[qind] -= 1;
            }
            state_changes[x + bx][y + by] -= 1;
            state_change.insert({x + bx, y + by});

            for (auto qind :query_info_list[nx + bx][ny + by]){
                query_change.insert(qind);
                query_changes[qind] += 1;
            }
            state_changes[nx + bx][ny + by] += 1;
            state_change.insert({nx + bx, ny + by});
        }

        pair<double, pair<vector<QueryChange>,vector<StateChange> >> info = get_change_info(query_change, state_change);

        double score_dif = info.first;
        vector<QueryChange> query_changes = info.second.first;
        vector<StateChange> state_changes = info.second.second;
        vector<BlockChange> block_changes;

        array<int,2> pos = {nx,ny};
        block_changes.push_back({bind,pos});

        UpdateChange up = {block_changes,query_changes,state_changes};
        return {score_dif,up};
    }

    // Block 2つの場所を swap + 周辺で少し動かす
    pair<double, UpdateChange> neighbor2(){
        int bind1 = rng.randint(0, m - 1);
        int bind2 = rng.randint(0, m - 1);

        if (bind1 == bind2){
            UpdateChange up;
            return {INF,up};
        }

        Block block1 = Blocks[bind1];
        Block block2 = Blocks[bind2];


        auto [x, y] = block_pos_list[bind1];
        auto [nx, ny] = block_pos_list[bind2];

        int dir1 = rng.randint(0,8);
        int dir2 = rng.randint(0,8);


        int x2 = x + DX[dir1];
        int y2 = y + DY[dir1];

        int nx2 = nx + DX[dir2];
        int ny2 = ny + DY[dir2];


        if (!can_put_block(bind1, nx2, ny2) || !can_put_block(bind2, x2, y2) ){
            UpdateChange up;
            return {INF,up};
        }


        set<int> query_change;
        set<pair<int,int>> state_change;

        for (auto& [bx, by] : block1.block_list){

            for (auto qind :query_info_list[x + bx][y + by]){
                query_change.insert(qind);
                query_changes[qind] -= 1;
            }
            state_changes[x + bx][y + by] -= 1;
            state_change.insert({x + bx, y + by});

            for (auto qind :query_info_list[nx2 + bx][ny2 + by]){
                query_change.insert(qind);
                query_changes[qind] += 1;
            }
            state_changes[nx2 + bx][ny2 + by] += 1;
            state_change.insert({nx2 + bx, ny2 + by});
        }

        for (auto& [bx, by] : block2.block_list){

            for (auto qind :query_info_list[x2 + bx][y2 + by]){
                query_change.insert(qind);
                query_changes[qind] += 1;
            }
            state_changes[x2 + bx][y2 + by] += 1;
            state_change.insert({x2 + bx, y2 + by});

            for (auto qind :query_info_list[nx + bx][ny + by]){
                query_change.insert(qind);
                query_changes[qind] -= 1;
            }
            state_changes[nx + bx][ny + by] -= 1;
            state_change.insert({nx + bx, ny + by});
        }

        pair<double, pair<vector<QueryChange>,vector<StateChange> >> info = get_change_info(query_change, state_change);

        double score_dif = info.first;
        vector<QueryChange> query_changes = info.second.first;
        vector<StateChange> state_changes = info.second.second;
        vector<BlockChange> block_changes;

        array<int,2> pos1 = {nx2,ny2};
        array<int,2> pos2 = {x2,y2};

        block_changes.push_back({bind1,pos1});
        block_changes.push_back({bind2,pos2});

        UpdateChange up = {block_changes,query_changes,state_changes};

        return {score_dif,up};
    }

    // Block 1つを周囲にランダムで動かす
    pair<double, UpdateChange> neighbor3(){
        int bind = rng.randint(0, m - 1);

        Block block = Blocks[bind];

        auto [x, y] = block_pos_list[bind];

        int dir = rng.randint(0,7);
        int nx = x + DX[dir];
        int ny = y + DY[dir];

        if (!can_put_block(bind, nx, ny) ){
            UpdateChange up;
            return {INF,up};
        }

        set<int> query_change;
        set<pair<int,int>> state_change;

        for (auto& [bx, by] : block.block_list){

            for (auto qind :query_info_list[x + bx][y + by]){
                query_change.insert(qind);
                query_changes[qind] -= 1;
            }
            state_changes[x + bx][y + by] -= 1;
            state_change.insert({x + bx, y + by});

            for (auto qind :query_info_list[nx + bx][ny + by]){
                query_change.insert(qind);
                query_changes[qind] += 1;
            }
            state_changes[nx + bx][ny + by] += 1;
            state_change.insert({nx + bx, ny + by});
        }

        pair<double, pair<vector<QueryChange>,vector<StateChange> >> info = get_change_info(query_change, state_change);

        double score_dif = info.first;
        vector<QueryChange> query_changes = info.second.first;
        vector<StateChange> state_changes = info.second.second;
        vector<BlockChange> block_changes;

        array<int,2> pos = {nx,ny};
        block_changes.push_back({bind,pos});

        UpdateChange up = {block_changes,query_changes,state_changes};
        return {score_dif,up};
    }


    int can_put_block_greedy(int ind, int x, int y) {
        Block block = Blocks[ind];
        if (block.max_x+x >= n || block.max_y+y >= n || x < 0 || y < 0){
            return 0;
        }

        for (auto& [nx,ny] : block.block_list){
            if (V_fixed[x+nx][y+ny] == 0){
                return 0;
            }
        }
        return 1;
    }

    vector<vector<double>> apply_block_greedy(int ind, int x, int y, vector<vector<double>>& weight_list){
        Block block = Blocks[ind];

        int size = block.block_size;

        int use_num = 0;

        for (auto& [nx,ny] : block.block_list){
            if (V_fixed[x+nx][y+ny] > 0){
                use_num++;
            }
        }

        if (use_num == size){
            return weight_list;
        }
        double psize = size * (size / (size - use_num));

        for (auto& [nx,ny] : block.block_list){
            if (V_fixed[x+nx][y+ny] == -1){
                weight_list[x + nx][y + ny] += psize;
            }
        }

        return weight_list;
    }

    array<int,2> greedy_choice(){

        vector<vector<double>> weight_list(n, vector<double>(n,0.0));

        for (int bind = 0; bind < m; bind++){
            for (int x = 0; x < n; x++){
                for (int y = 0; y < n; y++){
                    if (!can_put_block_greedy(bind,x,y)){
                        continue;
                    }
                    weight_list = apply_block_greedy(bind,x,y,weight_list);
                }
            }
        }
            

        double weight_max = 0.0;
        array<int,2> pos;

        for (int x = 0; x < n; x++){
            for (int y = 0; y < n; y++){
                double weight = weight_list[x][y] * state_query_weight[x][y];
                if (weight > weight_max){
                    weight_max = weight;
                    pos = {x,y};
                }
            }
        }
        
        assert (weight_max > 0);

        return pos;
    }

    array<int,2> query_choice(){
        vector<vector<array<int,2>>> rand_list(5);

        for (int x = 0; x < n; x++){
            for (int y = 0; y < n; y++){
                if (V_fixed[x][y] != -1){
                    continue;
                }
                if (state[x][y] == 0){
                    continue;
                }
                int zero_num = 0;

                for (int dir = 0; dir < 4; dir++){
                    int nx = x + DX[dir];
                    int ny = y + DY[dir];
                    if (nx >= 0 && ny >= 0 && nx < n && ny < n && state[nx][ny] > 0){
                        continue;
                    }
                    zero_num++;
                }
                rand_list[zero_num].push_back({x,y});
            }
        }

        for (int i = 4;i >= 0; i--){
            int le = rand_list[i].size();

            if (le == 0){
                continue;
            }

            return rand_list[i][rng.randint(0,le-1)];


        }

        return greedy_choice();
    }

    int try_ans(int turn){
        if (turn % n && turn - score_last_update != 3) return 0;

        vector<array<int,2>> ans_list;
        for (int x = 0; x < n; x++){
            for (int y = 0; y < n; y++){
                int v = V_fixed[x][y];
                int s = state[x][y];
                if (v != -1 && v != s){
                    return 0;
                }
                if (s > 0){
                    ans_list.push_back({x,y});
                }
            }
        }

        int res = environment.answer_query(ans_list);

        query_cost += 1;
        query_time += 1;

        return res;
    }

    void state_log(){
        for (int x = 0; x < n; x++){
            for (int y = 0; y < n; y++){
                int v = V_fixed[x][y];
                int s = state[x][y];
                string color;
                if (v == -1){
                    if (s > 0){
                        color = "green";
                    }else{
                        color = "white";
                    }
                }
                else if (v > 0){
                    color = "red";
                } else{
                    color = "blue";
                }
                std::ostringstream oss;
                oss << x << " " << y << " " << color << "";
                string message = oss.str();

                environment.comment(message);

            }
        }

    }

    vector<array<int,2>> make_ans_query(vector<array<int,2>>& pos_list){
        vector<array<int,2>> q;

        for (int i = 0; i < pos_list.size(); i++){
            auto [x,y] = pos_list[i];

            for (auto& [nx,ny] : Blocks[i].block_list){
                    q.push_back({x+nx,y+ny});
                }
        }

        q.erase(unique(q.begin(),q.end()),q.end());

        return q;

    }

    void solve_m2(){

        vector<pair<double,vector< array<int,2> > > > cand;

        for (int i1 = 0; i1 < n2; i1++){
            int x1 = i1/n, y1 = i1%n;
            if (!can_put_block(0,x1,y1)) continue;

            for (int i2 = 0; i2 < n2; i2++){
                int x2 = i2/n, y2 = i2%n;
                if (!can_put_block(1,x2,y2)) continue;

                vector<vector<int>> cand_state(n,vector<int>(n,0));

                for (auto& [nx,ny] : Blocks[0].block_list){
                    cand_state[x1+nx][y1+ny]++;
                }

                for (auto& [nx,ny] : Blocks[1].block_list){
                    cand_state[x2+nx][y2+ny]++;
                }

                double cand_score = 0;

                // クエリリストを使ったスコアの計算
                for (int i = 0; i < query_list.size(); ++i) {
                    int count = 0;

                    for (auto [x,y]: query_list[i]){
                        count += cand_state[x][y];
                    }

                    // query_weight[i] = count;

                    double prob = get_normal_dist_interval(count,query_ans[i],query_length[i]);
                    cand_score += prob;
                }

                cand.push_back({cand_score,{{x1,y1},{x2,y2}}});
            }
        }

        sort(cand.rbegin(),cand.rend());
        int ind = 1;
        for (auto& [s,va] : cand){
            if (va != environment.Block_pos_list){
                cout << "#c find " << ind << endl;
            }

            ind++;
        }
        exit(0);


    }

    void solve_m3(){

        vector<pair<double,vector< array<int,2> > > > cand;

        for (int i1 = 0; i1 < n2; i1++){
            int x1 = i1/n, y1 = i1%n;
            if (!can_put_block(0,x1,y1)) continue;

            for (int i2 = 0; i2 < n2; i2++){
                int x2 = i2/n, y2 = i2%n;
                if (!can_put_block(1,x2,y2)) continue;

                for (int i3 = 0; i3 < n2; i3++){
                    int x3 = i3/n, y3 = i3%n;
                    if (!can_put_block(2,x3,y3)) continue;

                    vector<vector<int>> cand_state(n,vector<int>(n,0));


                    for (auto& [nx,ny] : Blocks[0].block_list){
                        cand_state[x1+nx][y1+ny]++;
                    }

                    for (auto& [nx,ny] : Blocks[1].block_list){
                        cand_state[x2+nx][y2+ny]++;
                    }

                    for (auto& [nx,ny] : Blocks[2].block_list){
                        cand_state[x3+nx][y3+ny]++;
                    }

                    double cand_score = 0;

                    // クエリリストを使ったスコアの計算
                    for (int i = 0; i < query_list.size(); ++i) {
                        int count = 0;

                        for (auto [x,y]: query_list[i]){
                            count += cand_state[x][y];
                        }

                        // query_weight[i] = count;

                        double prob = get_normal_dist_interval(count,query_ans[i],query_length[i]);
                        cand_score += prob;
                    }

                    cand.push_back({cand_score,{{x1,y1},{x2,y2},{x3,y3}}});
                }
            }
        }

        sort(cand.rbegin(),cand.rend());
        int ind = 1;
        for (auto& [s,va] : cand){
            if (va == environment.Block_pos_list){
                cout << "#c find " << ind << endl;
            }

            ind++;
        }
        exit(0);


    }
};

struct Climbing {
    State state;

    Climbing(int n) : state(n) {
    }

    void solve() {

        if (m == 2){
            state.solve_m2();
        }
        if (m == 3){
            state.solve_m3();
        }
        int find_oil_sum = 0;
        int loop_size = 50000;
        const static double START_TEMP = 300; // 開始時の温度
        const static double END_TEMP   = 100; // 終了時の温度
        double temp = START_TEMP;
        const static double eps = 1e-5;
        vector<array<int,2>> ans_list;

        for (int turn = 0; turn < 2 * n2; ++turn) {
            environment.comment("start");
            
            environment.comment(to_string(state.score));

            double score_start = state.score;
            // if (false){
            if (timer.yet(time_early_lim)){
                for (int i = 0; i < loop_size; ++i) {
                    if (i % 1000 == 0)
                    {
                        // // const double time = timer.get_time();   // 経過時間（秒）
                        // if (!timer.yet(time_limit))
                        // {
                        //     break;
                        // }

                        const double progressRatio = (double)i / loop_size;   // 進捗。開始時が0.0、終了時が1.0
                        temp = START_TEMP + (END_TEMP - START_TEMP) * progressRatio;
                    }
                    int rand = rng.randint(0,99);

                    double score_dif;
                    UpdateChange update_info; // 仮定: UpdateChangeが定義されている
                    if (rand <= 50) {
                        tie(score_dif, update_info) = state.neighbor3();
                    } else if (rand <= 70) {
                        tie(score_dif, update_info) = state.neighbor1();
                    } else {
                        tie(score_dif, update_info) = state.neighbor2();
                    }

                    if (score_dif == INF) continue;
                    
                    const double probability = exp(score_dif *100/ temp); // 焼きなまし法の遷移確率

                    if (probability >= rng.random()) {
                        // cout << "#c " << probability << " " << score_dif << " " << temp << " " << i << " " << rand << endl;
                        state.update_state(score_dif, update_info);
                    }
                }

                state.state_log();

                if (abs(state.score -score_start) > eps){
                    state.score_last_update = turn;
                }
                state.try_ans(turn);

                array<int,2> pos = state.query_choice();
                int res = state.query({pos});

                environment.comment(to_string(state.score));
                find_oil_sum += res;

                if (res) {
                    ans_list.push_back(pos);
                }
                state.apply_query_res(res,pos);

                if (find_oil_sum == Block_sum) {
                    environment.answer_query(ans_list);
                }


            } else {

                array<int,2> pos = state.greedy_choice();
                int res = state.query({pos});

                environment.comment(to_string(state.score));
                find_oil_sum += res;

                if (res) {
                    ans_list.push_back(pos);
                }
                state.apply_query_res(res,pos);

                if (find_oil_sum == Block_sum) {
                    environment.answer_query(ans_list);
                }

            }
            
        }
    }
};

void InitializeMemo() {
    for (int i = 0; i < 200; ++i) {
        for (int j = 0; j < 200; ++j) {
            for (int k = 0; k < 200; ++k){
                memo[i][j][k] = INF;

            }
        }
    }
}

int main() {
    InitializeMemo();
    Input();
    environment.build();
    Climbing solver = Climbing(n);
    solver.solve();
    
    return 0;
}