#include <bits/stdc++.h>
using namespace std;

constexpr int TIME_LIM = 3;
constexpr int pena = 100;

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
double time_limit = 2.9;
double time_early_lim = 3.2;

int w,d,n;
vector<vector<int>> A;
int max_a = 0;
void Input() {
    cin >> w >> d >> n;

    A.resize(d);
    for (int i = 0; i < d; i++){
        for (int j = 0; j < n; j++){
            int a;
            cin >> a;
            A[i].push_back(a);
            max_a = max(max_a,a);
        }
    }


};

struct Rectangle{
    int lx,ly,rx,ry;
    int area,wx,wy;

    Rectangle(int x1,int y1, int x2, int y2): lx(x1),ly(y1),rx(x2),ry(y2){
        wx = rx-lx;
        wy = ry-ly;
        area = wx * wy;
    };
    Rectangle(): lx(0),ly(0),rx(0),ry(0){};

};

struct Solver{

    vector<vector<Rectangle>> best_ans,ans,complete_ans;
    vector<Rectangle> temp_rect;
    vector<Rectangle> sA_rect,reserve_rect;
    Rectangle adjust_rect;
    long long best_score = INF;
    bool is_valid_area = false;
    vector<vector<vector<int>>> rectangle_ids,grid_use_X,grid_use_Y, grid_checked_Y;
    
    vector<vector<int>> rectangle_sets, used_a;
    vector<int> dif_rect;
    int last_time = 0;

    Solver(int d, int w, int n) : 

        best_ans(d,vector<Rectangle>(n)),
        ans(d,vector<Rectangle>(n)),
        complete_ans(d,vector<Rectangle>(n)),
        sA_rect(n),
        reserve_rect(n),
        adjust_rect(),
        rectangle_sets(d),
        used_a(d,vector<int>(n,0)),
        rectangle_ids(d, vector<vector<int>>(w+1, vector<int>(w+1, -1))),
        grid_use_X(d, vector<vector<int>>(w+1, vector<int>(w+1, 0))),
        grid_use_Y(d, vector<vector<int>>(w+1, vector<int>(w+1, 0))),
        grid_checked_Y(d, vector<vector<int>>(w+1, vector<int>(w+1, 0))),
        dif_rect(n,0)
    {};

    void solve(){
        int line_num = -1;

        vector<array<int,3>> sA;
        vector<int> sums(d);
        for (int day = 0; day < d; day++){
            for (int i = 0; i < n; i++){
                sums[day] += A[day][i];
                sA.push_back({A[day][i],i,day});
            }
        }
        sort(sA.rbegin(),sA.rend());

        vector<vector<int>> use_a_list(d);
        vector<int> mas;
        int comp_num = 0;
        int afford = 50000;
        int lost_sum = 0;
        int width_cand = 0;
        while (true){
            comp_num++;
            int min_dif = w * w;
            vector<array<int,3>> use_list;
            vector<int> pos_ind(d,n-1);

            for (auto [a,i,day]: sA){
                if (used_a[day][i]) continue;

                int ma = a;
                vector<array<int,3>> use_cand;
                int min_cand = w * w;
                for (int di = 0; di < d; di++){
                    for (int x = pos_ind[di]; x >= 0; x--){
                        if (used_a[di][x] || A[di][x] > ma){
                            pos_ind[di]--;
                            continue;
                        }
                        use_cand.push_back({A[di][x],x,di});
                        min_cand = min(min_cand,A[di][x]);
                        break;
                    }
                }
                if (use_cand.size() != d) break;

                if (ma - min_cand < min_dif){
                    min_dif = ma - min_cand;
                    use_list = use_cand;
                }
            }
            if (min_dif == w * w) break;

            for (auto [a,i,day]: use_list){
                sums[day] -= a;
                used_a[day][i] = 1;
                use_a_list[day].push_back(a);
            }

            mas.resize(comp_num);
            for (int i = 0; i < comp_num; i++){
                mas[i] = 0;
            }

            for (int day = 0; day < d; day++){
                sort(use_a_list[day].begin(),use_a_list[day].end());
                for (int i = 0; i < comp_num; i++){
                    mas[i] = max(mas[i],use_a_list[day][i]);
                }
            }
            int lost = 0;
            for (auto m: mas){
                lost += m;
            }

            int ok = 1;
            for (int day = 0; day < d; day++){
                if (sums[day] > w * w - lost - afford) ok = 0;
            }

            if (ok == 0){
                comp_num--;
                for (auto [a,i,day]: use_list){
                    used_a[day][i] = 0;
                }
                break;
            }
            lost_sum = lost;

        }

        cerr << comp_num << " " << lost_sum << " " << (double)lost_sum/w/w << endl;
        

        if (comp_num){
            width_cand = w+1;
            int lost_min = w * w;

            
            for (int i = lost_sum/w; i < lost_sum/w+3; i++){
                if (i*w < lost_sum) continue;

                int lost_now = 0;
                int pos = 0;
                for (int j = comp_num-1; j >= 0; j--){
                    int m = mas[j];
                    lost_now += m%i;
                    pos += (m+i-1)/i;
                }
                if (pos > w) continue;

                lost_now += (w-pos) * i;

                if (lost_min > lost_now){
                    lost_min = lost_now;
                    width_cand = i;
                } 
            }

            
            

            if (width_cand == w+1){
                width_cand = 0;
                comp_num = 0;
                cerr << "width cand = " << width_cand << endl;
                cerr << "lost min = " << 0 << endl;
                for (int day = 0; day < d; day++){
                    for (int i = 0; i < n; i++){
                        used_a[day][i] = 0;
                    }
                }
                temp_rect.push_back({0,0,0,0});
            } else{
                cerr << "width cand = " << width_cand << endl;
                cerr << "lost min = " << lost_min << endl;

                vector<Rectangle> use_last;
                int pos = 0;
                for (int j = 0; j < comp_num; j++){
                    int m = mas[j];
                    int npos = (m+width_cand-1)/width_cand;
                    use_last.push_back({0,pos,width_cand,pos+npos});
                    pos += npos;
                }
                temp_rect.push_back({0,pos,width_cand,w});

                for (int day = 0; day < d; day++){
                    int count = 0;
                    for (int i = 0; i < n; i++){
                        if (used_a[day][i]){ 
                            complete_ans[day][i] = use_last[count];
                            count++;
                        }
                    }
                }
            }

        }

        for (int rep = 0; rep < 2; rep++){
            for (int i = 1; i < min((n-comp_num)/2+1,10)+1; i++){
                bool ok = true;
                vector<Rectangle> bases;
                for (Rectangle tem: temp_rect){
                    bases.push_back(tem);
                }

                int width = (w-width_cand)/i;

                for (int j = 0; j < i; j++){
                    if (j < i-1){
                        bases.push_back({width_cand + width*j,0,width_cand + width*j+width,w});
                    } else{
                        bases.push_back({width_cand + width*j,0,w,w});

                    }
                }
                int day = 0;
                int nday = 0;
                while (day < d){
                    vector<int> sA(n-comp_num);
                    int count = 0;
                    for (int x = 0; x < n; x++){
                        if (used_a[day][x]) continue;
                        sA[count] = A[day][x];
                        count++;
                    }
                    nday = day+1;
                    while (nday < d){
                        int count = 0;
                        int cum_area = 0;
                        for (int x = 0; x < n; x++){
                            if (used_a[nday][x]) continue;
                            sA[count] = max(sA[count],A[nday][x]);
                            cum_area += sA[count];
                            count++;
                            
                        }
                        if (cum_area <= w * w && check_split_greedy(sA,bases)){
                            swap(reserve_rect,sA_rect);
                            nday++;
                        } else{
                            break;
                        }
                    }
                    if (nday == day+1){
                        ok &= split_greedy(day,bases);
                        day++;
                    }else{
                        for (int x = day; x < nday; x++){
                            int last = -1;
                            int count = 0;
                            for (int ni = 0; ni < n; ni++){
                                if (used_a[x][ni]){
                                    ans[x][ni] = complete_ans[x][ni];
                                    last = ni;
                                } else{
                                    ans[x][ni] = reserve_rect[count];
                                    count++;
                                }
                            }
                            if (adjust_rect.area > 0 && last != -1){
                                ans[x][last] = {min(ans[x][last].lx,adjust_rect.lx),min(ans[x][last].ly,adjust_rect.ly),max(ans[x][last].rx,adjust_rect.rx),max(ans[x][last].ry,adjust_rect.ry)};


                            }
                        }
                        day = nday;
                    }
                    if (!ok) break;
                }
                if (ok) {
                    if (update_best(ans)){
                        line_num = i;
                    }
                }

            }

            for (int i = 1; i < min((n-comp_num)/2+1,10)+1; i++){

                int width = (w-width_cand)/i;
                if (width*w >= max_a) continue;

                bool ok = true;
                vector<Rectangle> bases;
                for (Rectangle tem: temp_rect){
                    bases.push_back(tem);
                }

                int need = (max_a+w-1)/w;
                bases.push_back({width_cand + 0,0,width_cand + need,w});
                width = (w-need-width_cand)/(i-1);

                int le = need + width_cand;
                for (int j = 0; j < i-1; j++){
                    if (j < i-2){
                        bases.push_back({le+width*j,0,le+width*j+j,w});
                    } else{
                        bases.push_back({le+width*j,0,w,w});
                    }
                }

                int day = 0;
                int nday = 0;
                while (day < d){
                    vector<int> sA(n-comp_num);
                    int count = 0;
                    for (int x = 0; x < n; x++){
                        if (used_a[day][x]) continue;
                        sA[count] = A[day][x];
                        count++;
                    }
                    nday = day+1;
                    while (nday < d){
                        int count = 0;
                        int cum_area = 0;
                        for (int x = 0; x < n; x++){
                            if (used_a[nday][x]) continue;
                            sA[count] = max(sA[count],A[nday][x]);
                            cum_area += sA[count];
                            count++;
                            
                        }
                        if (cum_area <= w * w && check_split_greedy(sA,bases)){
                            swap(reserve_rect,sA_rect);
                            nday++;
                        } else{
                            break;
                        }
                    }
                    if (nday == day+1){
                        ok &= split_greedy(day,bases);
                        day++;
                    }else{
                        for (int x = day; x < nday; x++){
                            int last = -1;
                            int count = 0;
                            for (int ni = 0; ni < n; ni++){
                                if (used_a[x][ni]){
                                    ans[x][ni] = complete_ans[x][ni];
                                    last = ni;
                                } else{
                                    ans[x][ni] = reserve_rect[count];
                                    count++;
                                }
                            }
                            if (adjust_rect.area > 0 && last != -1){
                                ans[x][last] = {min(ans[x][last].lx,adjust_rect.lx),min(ans[x][last].ly,adjust_rect.ly),max(ans[x][last].rx,adjust_rect.rx),max(ans[x][last].ry,adjust_rect.ry)};


                            }
                        }
                        day = nday;
                    }
                    if (!ok) break;
                }
                if (ok) {
                    if (update_best(ans)){
                        line_num = i;
                    }
                }

            }
            cerr << "line num = " << line_num << endl;

            if (!is_valid_area && width_cand){
                for (int day = 0; day < d; day++){
                    for (int i = 0; i < n; i++){
                        used_a[day][i] = 0;
                    }
                }
                temp_rect.clear();
                width_cand = 0;
                temp_rect.push_back({0,0,0,0});
                comp_num = 0;
            } else{
                annealing();
                break;
            }
           
        }
    

    }

    long long get_dif_area_single(int day){
        vector<int> ids(n);

        for (int i = 0; i < n; i++){
            ids[i] = i;
        }
        
        long long score = 0;

        sort(ids.begin(), ids.end(),
              [&](int i1, int i2) {
                  return rectangle_sets[day][i1] < rectangle_sets[day][i2];
              });
        

        for (int i = 0; i < n; i++){
            if (A[day][i] > rectangle_sets[day][ids[i]]){
                score += pena*(A[day][i] - rectangle_sets[day][ids[i]]);
            }
        }
        return score;

    }

    long long get_dif_area(vector<int>& dif_rect, int day){
        
        vector<int> ids(n);
        
        for (int i = 0; i < n; i++){
            ids[i] = i;
        }

        long long score = 0;

        sort(ids.begin(), ids.end(),
              [&](int i1, int i2) {
                  return rectangle_sets[day][i1] < rectangle_sets[day][i2];
              });

        for (int i = 0; i < n; i++){
            if (A[day][i] > rectangle_sets[day][ids[i]]){
                score += pena*(A[day][i] - rectangle_sets[day][ids[i]]);
            }
        }

        sort(ids.begin(), ids.end(),
              [&](int i1, int i2) {
                  return dif_rect[i1] < dif_rect[i2];
              });
        
        for (int i = 0; i < n; i++){

            if (A[day][i] > dif_rect[ids[i]]){
                score -= pena*(A[day][i] - dif_rect[ids[i]]);
            }
        }

        return score;

    }

    long long neighbor1(long long base_score, double temp){

        int day = rng.randint(0,d-1);
        int rect_id = rng.randint(0,n-1);
        int corner = rng.randint(0,3);
        int xy = rng.randint(0,1);

        Rectangle rect = ans[day][rect_id];
        int x = rect.lx;
        int x2 = x;
        int y = rect.ly;
        int y2 = y;
        
        if (corner == 1 || corner == 3){
            x = rect.rx-1;
            x2 = rect.rx;
        }

        if (corner == 2 || corner == 3){
            y = rect.ry-1;
            y2 = rect.ry;
        }
        

        if (xy == 0){ // x方向に伸ばす
            int nx = x-1;
            int nx2 = x2-1;

            if (corner == 1 || corner == 3){
                nx = x+1;
                nx2 = x2+1;
            }

            if (nx < 0 || nx >= w){
                return base_score;
            }
            set<int> add_point;
            set<int> rem_point;

            int ly = -1,ry = -1;
            for (int ny = y; ny >= 0; ny--){
                int id1 = rectangle_ids[day][x][ny];
                int id2 = rectangle_ids[day][nx][ny];

                if (ans[day][id2].wx == 1){
                    return base_score;
                }
                add_point.insert(ans[day][id1].ly);
                rem_point.insert(ans[day][id2].ly);
                if (ans[day][id1].ly == ans[day][id2].ly){
                    ly = ans[day][id1].ly;
                    break;
                }
            }
            for (int ny = y; ny < w; ny++){
                int id1 = rectangle_ids[day][x][ny];
                int id2 = rectangle_ids[day][nx][ny];

                if (ans[day][id2].wx == 1){
                    return base_score;
                }
                add_point.insert(ans[day][id1].ry);
                rem_point.insert(ans[day][id2].ry);
                if (ans[day][id1].ry == ans[day][id2].ry){
                    ry = ans[day][id1].ry;
                    break;
                }
            }

            long long dif_score = 0; // 現在のコスト - 変化後のコスト
            
            for (int i = 0; i < n; i++){
                dif_rect[i] = rectangle_sets[day][i];

            }
            // パーティションのコスト
            for (int ny = ly; ny < ry; ny++){
                dif_rect[rectangle_ids[day][x][ny]]++;
                dif_rect[rectangle_ids[day][nx][ny]]--;

                if (day > 0){
                    dif_score += (grid_use_Y[day-1][x2][ny] == 1 ? -1: 1);
                    dif_score += (grid_use_Y[day-1][nx2][ny] == 0 ? -1: 1);
                }

                if (day < d-1){
                    dif_score += (grid_use_Y[day+1][x2][ny] == 1 ? -1: 1);
                    dif_score += (grid_use_Y[day+1][nx2][ny] == 0 ? -1: 1);
                    
                }
            }
            for (auto ny: add_point){

                if (day > 0){
                    dif_score += (grid_use_X[day-1][nx][ny] == 0 ? -1: 1);
                }
                if (day < d-1){
                    dif_score += (grid_use_X[day+1][nx][ny] == 0 ? -1: 1);
                }
            }
            for (auto ny: rem_point){

                if (day > 0){
                    dif_score += (grid_use_X[day-1][nx][ny] == 1 ? -1: 1);
                }
                if (day < d-1){
                    dif_score += (grid_use_X[day+1][nx][ny] == 1 ? -1: 1);
                }
            }

            dif_score += get_dif_area(dif_rect,day);

            // 変更を採択
            if (dif_score >= 0 || exp(dif_score / temp)>= rng.random()){
                base_score -= dif_score;
                // 面積の情報を更新

                for (int i = 0; i < n; i++){
                    if (rectangle_sets[day][i] == dif_rect[i]) continue;
                    if (dif_rect[i] < rectangle_sets[day][i]){
                        if (corner == 0 || corner == 2){
                            ans[day][i].wx--;
                            ans[day][i].area -= ans[day][i].wy;
                            ans[day][i].rx--;
                        } else{
                            ans[day][i].wx--;
                            ans[day][i].area -= ans[day][i].wy;
                            ans[day][i].lx++;
                        }

                    } else{
                        if (corner == 0 || corner == 2){
                            ans[day][i].wx++;
                            ans[day][i].area += ans[day][i].wy;
                            ans[day][i].lx--;
                        } else{
                            ans[day][i].wx++;
                            ans[day][i].area += ans[day][i].wy;
                            ans[day][i].rx++;
                        }
                    }
                    
                }
                swap(rectangle_sets[day],dif_rect);

                // パーティションの情報を更新
                for (int ny = ly; ny < ry; ny++){
                    grid_use_Y[day][x2][ny] = 0;
                    grid_use_Y[day][nx2][ny] = 1;
                    rectangle_ids[day][nx][ny] = rectangle_ids[day][x][ny];
                }
            
                for (auto ny: rem_point){
                    grid_use_X[day][nx][ny] = 0;
                }
                for (auto ny: add_point){
                    grid_use_X[day][nx][ny] = 1;
                }
            }

            return base_score;

        } else{  // y方向に伸ばす
            int ny = y-1;
            int ny2 = y2-1;

            if (corner == 2 || corner == 3){
                ny = y+1;
                ny2 = y2+1;
            }

            if (ny < 0 || ny >= w){
                return base_score;
            }
            set<int> add_point;
            set<int> rem_point;

            int lx = -1,rx = -1;
            for (int nx = x; nx >= 0; nx--){
                int id1 = rectangle_ids[day][nx][y];
                int id2 = rectangle_ids[day][nx][ny];

                if (ans[day][id2].wy == 1){
                    return base_score;
                }
                add_point.insert(ans[day][id1].lx);
                rem_point.insert(ans[day][id2].lx);
                if (ans[day][id1].lx == ans[day][id2].lx){
                    lx = ans[day][id1].lx;
                    break;
                }
            }
            for (int nx = x; nx < w; nx++){
                int id1 = rectangle_ids[day][nx][y];
                int id2 = rectangle_ids[day][nx][ny];

                if (ans[day][id2].wy == 1){
                    return base_score;
                }
                add_point.insert(ans[day][id1].rx);
                rem_point.insert(ans[day][id2].rx);
                if (ans[day][id1].rx == ans[day][id2].rx){
                    rx = ans[day][id1].rx;
                    break;
                }
            }

            long long dif_score = 0; // 現在のコスト - 変化後のコスト
            
            for (int i = 0; i < n; i++){
                dif_rect[i] = rectangle_sets[day][i];
            }
            // パーティションのコスト
            for (int nx = lx; nx < rx; nx++){
                dif_rect[rectangle_ids[day][nx][y]]++;
                dif_rect[rectangle_ids[day][nx][ny]]--;

                if (day > 0){
                    dif_score += (grid_use_X[day-1][nx][y2] == 1 ? -1: 1);
                    dif_score += (grid_use_X[day-1][nx][ny2] == 0 ? -1: 1);
                }

                if (day < d-1){
                    dif_score += (grid_use_X[day+1][nx][y2] == 1 ? -1: 1);
                    dif_score += (grid_use_X[day+1][nx][ny2] == 0 ? -1: 1);
                }
            }
            for (auto nx: add_point){

                if (day > 0){
                    dif_score += (grid_use_Y[day-1][nx][ny] == 0 ? -1: 1);
                }
                if (day < d-1){
                    dif_score += (grid_use_Y[day+1][nx][ny] == 0 ? -1: 1);
                }
            }
            for (auto nx: rem_point){

                if (day > 0){
                    dif_score += (grid_use_Y[day-1][nx][ny] == 1 ? -1: 1);

                }
                if (day < d-1){
                    dif_score += (grid_use_Y[day+1][nx][ny] == 1 ? -1: 1);
                }
            }

            dif_score += get_dif_area(dif_rect,day);

            // 変更を採択
            if (dif_score >= 0 || exp(dif_score / temp)>= rng.random()){

                base_score -= dif_score;
                // 面積の情報を更新

                for (int i = 0; i < n; i++){
                    if (rectangle_sets[day][i] == dif_rect[i]) continue;
                    if (dif_rect[i] < rectangle_sets[day][i]){
                        if (corner == 0 || corner == 1){
                            ans[day][i].wy--;
                            ans[day][i].area -= ans[day][i].wx;
                            ans[day][i].ry--;
                        } else{
                            ans[day][i].wy--;
                            ans[day][i].area -= ans[day][i].wx;
                            ans[day][i].ly++;
                        }
                    } else{
                        if (corner == 0 || corner == 1){
                            ans[day][i].wy++;
                            ans[day][i].area += ans[day][i].wx;
                            ans[day][i].ly--;
                        } else{
                            ans[day][i].wy++;
                            ans[day][i].area += ans[day][i].wx;
                            ans[day][i].ry++;
                        }
                    }
                    
                }
                swap(rectangle_sets[day],dif_rect);

                // パーティションの情報を更新
                for (int nx = lx; nx < rx; nx++){
                    grid_use_X[day][nx][y2] = 0;
                    grid_use_X[day][nx][ny2] = 1;
                    rectangle_ids[day][nx][ny] = rectangle_ids[day][nx][y];
                }
            
                for (auto nx: rem_point){
                    grid_use_Y[day][nx][ny] = 0;
                }
                for (auto nx: add_point){
                    grid_use_Y[day][nx][ny] = 1;
                }
            }
            return base_score;
        }
        
           
    }

    long long neighbor2(long long base_score, double temp){

        int day = rng.randint(0,d-1);
        int rect_id = rng.randint(0,n-1);
        int corner = rng.randint(0,3);
        int xy = rng.randint(0,1);

        Rectangle rect = ans[day][rect_id];
        int x = rect.lx;
        int x2 = x;
        int y = rect.ly;
        int y2 = y;
        
        if (corner == 1 || corner == 3){
            x = rect.rx-1;
            x2 = rect.rx;
        }

        if (corner == 2 || corner == 3){
            y = rect.ry-1;
            y2 = rect.ry;
        }
        
        if (xy == 0){ // x方向に伸ばす
            int nx = x-1;
            int ny = y;
            int nx2 = x2-1;
            int ny2 = y2-1;
            if (corner == 1 || corner == 3){
                nx = x+1;
            }

            if (corner == 2 || corner == 3){
                y2 = rect.ly;
            } else{
                y2 = rect.ry;
            }


            if (nx < 0 || nx >= w){
                return base_score;
            }
            int id2 = rectangle_ids[day][nx][y];
            Rectangle rect2 = ans[day][id2];

            if (corner == 0 || corner == 1){
                if (rect2.ly != rect.ly || rect2.wy <= rect.wy){
                    return base_score;
                }
            } else{
                if (rect2.ry != rect.ry || rect2.wy <= rect.wy){
                    return base_score;
                }
            }

            long long dif_score = 0; // 現在のコスト - 変化後のコスト
            
            for (int i = 0; i < n; i++){
                dif_rect[i] = rectangle_sets[day][i];

            }
            for (int ny = rect.ly; ny < rect.ry; ny++){
                assert (grid_use_Y[day][x2][ny]);
                if (day > 0){
                    dif_score += (grid_use_Y[day-1][x2][ny] == 1 ? -1: 1);
                }

                if (day < d-1){
                    dif_score += (grid_use_Y[day+1][x2][ny] == 1 ? -1: 1);
                }
            }

            for (int nx = rect2.lx; nx < rect2.rx; nx++){
                assert (grid_use_X[day][nx][y2] == 0);

                if (day > 0){
                    dif_score += (grid_use_X[day-1][nx][y2] == 0 ? -1: 1);
                }

                if (day < d-1){
                    dif_score += (grid_use_X[day+1][nx][y2] == 0 ? -1: 1);
                }
            }

            int dx = rect2.wx;
            int dy = rect.wy;
            int darea = dx * dy;
            dif_rect[rect_id] += darea;
            dif_rect[id2] -= darea;

            dif_score += get_dif_area(dif_rect,day);

            // 変更を採択
            if (dif_score >= 0 || exp(dif_score / temp)>= rng.random()){

                base_score -= dif_score;

                // パーティションの情報を更新
                for (int ny = rect.ly; ny < rect.ry; ny++){
                    grid_use_Y[day][x2][ny] = 0;
                }

                for (int nx = rect2.lx; nx < rect2.rx; nx++){
                    grid_use_X[day][nx][y2] = 1;
                    
                }

                for (int nx = rect2.lx; nx < rect2.rx; nx++){
                    for (int ny = rect.ly; ny < rect.ry; ny++){
                        rectangle_ids[day][nx][ny] = rect_id;
                    }
                }

                // 面積の情報を更新

                ans[day][rect_id].wx += dx;
                ans[day][rect_id].area += darea;
                ans[day][id2].wy -= dy;
                ans[day][id2].area -= darea;
                if (corner == 0 || corner == 2){
                    ans[day][rect_id].lx -= dx;
                } else{
                    ans[day][rect_id].rx += dx;
                }

                if (corner == 0 || corner == 1){
                    ans[day][id2].ly += dy;
                } else{
                    ans[day][id2].ry -= dy;
                }

                swap(rectangle_sets[day],dif_rect);
            }

            return base_score;

        } else{  // y方向に伸ばす

            int nx = x;
            int ny = y-1;
            int nx2 = x2-1;
            int ny2 = y2-1;
            if (corner == 2 || corner == 3){
                ny = y+1;
            }
            if (corner == 0 || corner == 2){
                x2 = rect.rx;
            } else{
                x2 = rect.lx;
            }
           

            if (ny < 0 || ny >= w){
                return base_score;
            }
            int id2 = rectangle_ids[day][x][ny];
            Rectangle rect2 = ans[day][id2];

            if (corner == 0 || corner == 2){
                if (rect2.lx != rect.lx || rect2.wx <= rect.wx){
                    return base_score;
                }
            } else{
                if (rect2.rx != rect.rx || rect2.wx <= rect.wx){
                    return base_score;
                }
            }

            long long dif_score = 0; // 現在のコスト - 変化後のコスト
            
            for (int i = 0; i < n; i++){
                dif_rect[i] = rectangle_sets[day][i];

            }

            for (int nx = rect.lx; nx < rect.rx; nx++){
                assert (grid_use_X[day][nx][y2]);
                if (day > 0){
                    dif_score += (grid_use_X[day-1][nx][y2] == 1 ? -1: 1);
                }

                if (day < d-1){
                    dif_score += (grid_use_X[day+1][nx][y2] == 1 ? -1: 1);
                }
            }

            for (int ny = rect2.ly; ny < rect2.ry; ny++){
                assert (grid_use_Y[day][x2][ny] == 0);

                if (day > 0){
                    dif_score += (grid_use_Y[day-1][x2][ny] == 0 ? -1: 1);
                }

                if (day < d-1){
                    dif_score += (grid_use_Y[day+1][x2][ny] == 0 ? -1: 1);
                }
            }

            int dx = rect.wx;
            int dy = rect2.wy;
            int darea = dx * dy;
            dif_rect[rect_id] += darea;
            dif_rect[id2] -= darea;

            dif_score += get_dif_area(dif_rect,day);

            // 変更を採択
            if (dif_score >= 0 || exp(dif_score / temp)>= rng.random()){

                base_score -= dif_score;

                // パーティションの情報を更新
                for (int nx = rect.lx; nx < rect.rx; nx++){
                    grid_use_X[day][nx][y2] = 0;
                }

                for (int ny = rect2.ly; ny < rect2.ry; ny++){
                    grid_use_Y[day][x2][ny] = 1;
                    
                }

                for (int nx = rect.lx; nx < rect.rx; nx++){
                    for (int ny = rect2.ly; ny < rect2.ry; ny++){
                        rectangle_ids[day][nx][ny] = rect_id;
                    }
                }

                // 面積の情報を更新
        
                ans[day][rect_id].wy += dy;
                ans[day][rect_id].area += darea;
                ans[day][id2].wx -= dx;
                ans[day][id2].area -= darea;

                if (corner == 0 || corner == 1){
                    ans[day][rect_id].ly -= dy;
                } else{
                    ans[day][rect_id].ry += dy;
                }

                if (corner == 0 || corner == 2){
                    ans[day][id2].lx += dx;
                } else{
                    ans[day][id2].rx -= dx;
                }

                swap(rectangle_sets[day],dif_rect);
                
            }

            return base_score;
            
        }
        
           
    }

    void annealing(){

        // 初期化
        ans = best_ans;
        long long base_score = best_score;
        for (int day = 0; day < d; day++){

            for (int x = 0; x <= w; x++){
                for (int y = 0; y <= w; y++){
                    grid_use_X[day][x][y] = 0;
                    grid_use_Y[day][x][y] = 0;
                    rectangle_ids[day][x][y] = -1;
                }
            }
            for (int i = 0; i < n; i++){
                Rectangle& rect = ans[day][i];

                if (rect.area < A[day][i]){
                    base_score -= pena * (A[day][i] - rect.area);
                }

                rectangle_sets[day].push_back(rect.area);
                for (int x = rect.lx; x < rect.rx; x++){
                    for (int y = rect.ly; y < rect.ry; y++){
                        rectangle_ids[day][x][y] = i;
                    }
                }

                for (int x = rect.lx; x < rect.rx; x++){
                    grid_use_X[day][x][rect.ly] = 1;
                    grid_use_X[day][x][rect.ry] = 1;

                }
                for (int y = rect.ly; y < rect.ry; y++){
                    grid_use_Y[day][rect.lx][y] = 1;
                    grid_use_Y[day][rect.rx][y] = 1;

                }
            }
            base_score += get_dif_area_single(day);
        }

        int chose = -1;

        

        assert (base_score == best_score);
        cerr << "start score = " << base_score << " at " << timer.get_time() <<endl;
        int loop_count = 0;
        const static double START_TEMP = 10; // 開始時の温度
        const static double END_TEMP   = 0.1; // 終了時の温度
        double temp = START_TEMP;
        double progressRatio = 0;
        while (true){
            loop_count++;
            if (loop_count % 100 == 0)
            {
                if (!timer.yet(time_limit)) break;
                progressRatio = timer.get_time() / time_limit;   // 進捗。開始時が0.0、終了時が1.0
                // const double progressRatio = (double)loop_count / loop_time;
                temp = START_TEMP + (END_TEMP - START_TEMP) * progressRatio;
            }

            chose = rng.randint(0,10);

            if (chose < 10){
                base_score = neighbor1(base_score,temp);
            }
            else{
                base_score = neighbor2(base_score,temp);
            }
            if (base_score < best_score){
                best_score = base_score;
                best_ans = ans;
            }
        }

        cerr << "loop count = " << loop_count << endl;
        cerr << "end time = " << timer.get_time() << endl;
        out_ans();

    }

    void validate(int day){
        for (int i = 0; i < n; i++){
            assert (ans[day][i].area == rectangle_sets[day][i]);
        }
        vector<vector<int>> temp(w,vector<int>(w,-1));
        vector<vector<int>> temp_grid_X(w+1,vector<int>(w+1,0));
        vector<vector<int>> temp_grid_Y(w+1,vector<int>(w+1,0));
        
        for (int i = 0; i < n; i++){
            Rectangle rect = ans[day][i];

            for (int x = rect.lx; x < rect.rx; x++){
                for (int y = rect.ly; y < rect.ry; y++){
                    assert (temp[x][y] == -1);
                    temp[x][y] = i;
                    
                }
            }

            for (int x = rect.lx; x < rect.rx; x++){
                temp_grid_X[x][rect.ly] = 1;
                temp_grid_X[x][rect.ry] = 1;

            }
            for (int y = rect.ly; y < rect.ry; y++){
                temp_grid_Y[rect.lx][y] = 1;
                temp_grid_Y[rect.rx][y] = 1;

            }

        }
        for (int x = 0; x < w; x++){
            for (int y = 0; y < w; y++){
                if (temp[x][y] != rectangle_ids[day][x][y]){
                    cerr << "Error rectangle_ids at day = " << day << " x = " << x << " y = " << y << " temp[x][y] = " <<  temp[x][y] << " rectangle[x][y] = " << rectangle_ids[day][x][y] << endl;  
                }
                assert (temp[x][y] == rectangle_ids[day][x][y]);
            }
        }

        for (int i = 0; i < w+1; i++){
            for (int j = 0; j < w+1; j++){
                assert (grid_use_X[day][i][j] == temp_grid_X[i][j]);
                assert (grid_use_Y[day][i][j] == temp_grid_Y[i][j]);

            }
        }
    }

    void out_ans(){
        if (best_score == INF) best_score = -1;

        cerr << "score = " << best_score << endl;

        for (int day = 0; day < d; day++){
            sort(best_ans[day].begin(), best_ans[day].end(),
              [&](Rectangle i1, Rectangle i2) {
                  return i1.area < i2.area;
              });

            for (int i = 0; i < n; i++){
                assert (A[day][i] <= best_ans[day][i].area);
                cout << best_ans[day][i].lx << " " << best_ans[day][i].ly << " " << best_ans[day][i].rx << " "  << best_ans[day][i].ry << endl;
            }
        }
    }

    void out_ans(vector<vector<Rectangle>> ans, long long score){

        cout << "score = " << score << endl;
        for (int day = 0; day < d; day++){

            sort(ans[day].begin(), ans[day].end(),
              [&](Rectangle i1, Rectangle i2) {
                  return i1.area < i2.area;
              });
            for (int i = 0; i < n; i++){
                cout << ans[day][i].lx << " " << ans[day][i].ly << " " << ans[day][i].rx << " "  << ans[day][i].ry << endl;
            }
        }
    }

    bool update_best(vector<vector<Rectangle>>& ans){

        last_time++;
        long long area_score = 0;
        long long build_score = 0;

        auto& grid_time_X = grid_use_X;
        auto& grid_time_Y = grid_use_Y;
        auto& grid_checked_X = rectangle_ids;

        bool valid_check = true;
        for (int day = 0; day < d; day++){
            sort(ans[day].begin(), ans[day].end(),
              [&](Rectangle i1, Rectangle i2) {
                  return i1.area < i2.area;
              });
            for (int i = 0; i < n; i++){
                Rectangle& rect = ans[day][i];
                if (rect.rx == rect.lx || rect.ry == rect.ly){
                    return false;
                }

                if (rect.area < A[day][i]){
                    area_score += pena * (A[day][i]- rect.area);
                    valid_check = false;
                }

                for (int x = rect.lx; x < rect.rx; x++){
                    grid_time_X[day][x][rect.ly] = last_time;
                    grid_time_X[day][x][rect.ry] = last_time;

                }
                for (int y = rect.ly; y < rect.ry; y++){
                    grid_time_Y[day][rect.lx][y] = last_time;
                    grid_time_Y[day][rect.rx][y] = last_time;

                }
            }
        }

        for (int day = 0; day < d; day++){

            for (int i = 0; i < n; i++){
                Rectangle& rect = ans[day][i];

                for (int x = rect.lx; x < rect.rx; x++){

                    if (day > 0){
                        if (rect.ly > 0 && grid_checked_X[day-1][x][rect.ly] != last_time && grid_time_X[day-1][x][rect.ly] != grid_time_X[day][x][rect.ly]) {
                            build_score++;
                            grid_checked_X[day-1][x][rect.ly] = last_time;

                        }
                        if (rect.ry < w && grid_checked_X[day-1][x][rect.ry] != last_time && grid_time_X[day-1][x][rect.ry] != grid_time_X[day][x][rect.ry]) {
                            build_score++;
                            grid_checked_X[day-1][x][rect.ry] = last_time;

                        }
                    }

                    if (day < d-1){
                        if (rect.ly > 0 && grid_checked_X[day][x][rect.ly] != last_time && grid_time_X[day+1][x][rect.ly] != grid_time_X[day][x][rect.ly]){
                            build_score++;
                            grid_checked_X[day][x][rect.ly] = last_time;

                        }
                        if (rect.ry < w && grid_checked_X[day][x][rect.ry] != last_time && grid_time_X[day+1][x][rect.ry] != grid_time_X[day][x][rect.ry]) {
                            build_score++;
                            grid_checked_X[day][x][rect.ry] = last_time;

                        }
                    }
                }
                for (int y = rect.ly; y < rect.ry; y++){
                    if (day > 0){
                        if (rect.lx > 0 && grid_checked_Y[day-1][rect.lx][y] != last_time && grid_time_Y[day-1][rect.lx][y] != grid_time_Y[day][rect.lx][y]) {
                            build_score++;
                            grid_checked_Y[day-1][rect.lx][y] = last_time;
                        }
                        if (rect.rx < w && grid_checked_Y[day-1][rect.rx][y] != last_time && grid_time_Y[day-1][rect.rx][y] != grid_time_Y[day][rect.rx][y]) {
                            build_score++;
                            grid_checked_Y[day-1][rect.rx][y] = last_time;

                        }
                    }

                    if (day < d-1){
                        if (rect.lx > 0 && grid_checked_Y[day][rect.lx][y] != last_time && grid_time_Y[day+1][rect.lx][y] != grid_time_Y[day][rect.lx][y]) {
                            build_score++;
                            grid_checked_Y[day][rect.lx][y] = last_time;

                        }
                        if (rect.rx < w && grid_checked_Y[day][rect.rx][y] != last_time && grid_time_Y[day+1][rect.rx][y] != grid_time_Y[day][rect.rx][y]) {
                            build_score++;
                            grid_checked_Y[day][rect.rx][y] = last_time;

                        }
                    }

                }

            }
        }

        long long score = area_score + build_score + 1;
        if (valid_check) is_valid_area = true;
        if (score < best_score){
            best_score = score;
            best_ans = ans;
            return true;
        }
        return false;

    }

    int get_base_rect(vector<Rectangle>& bases){
        int ma_size = -1;
        int ma_ind = -1;
        for (int i = 0; i < bases.size(); i++){
            if (ma_size < bases[i].area){
                ma_size = bases[i].area;
                ma_ind = i;
            }
        }

        return ma_ind;
    };

    bool split_greedy(int day, vector<Rectangle> bases){
        vector<int> last_use(bases.size(),-1);

        for (int i = n-1; i >= 0; i--){
            if (used_a[day][i]){
                ans[day][i] = complete_ans[day][i];
                if (last_use[0] == -1) last_use[0] = i;
                continue;
            }

            int a = A[day][i];

            int ma_ind = get_base_rect(bases);

            Rectangle& base = bases[ma_ind];

            if (base.area <= 0) return false;

            if (base.wx >= base.wy){
                int need = (a+base.wy-1)/base.wy;
                
                if (need > base.wx){
                    need = base.wx;
                }

                ans[day][i] = (Rectangle){base.lx,base.ly,base.lx+need,base.ry};
                base = (Rectangle){base.lx+need,base.ly,base.rx,base.ry};   

            } else{
                int need = (a+base.wx-1)/base.wx;
                if (need > base.wy){
                    need = base.wy;
                }
                
                ans[day][i] = (Rectangle){base.lx,base.ly,base.rx,base.ly+need};
                base = (Rectangle){base.lx,base.ly+need,base.rx,base.ry};    

            }
            last_use[ma_ind] = i;

            
        }
        for (int i = 0; i < bases.size(); i++){
            if (bases[i].area == 0 || last_use[i] == -1) continue;
            int last = last_use[i];

            ans[day][last] = {min(ans[day][last].lx,bases[i].lx),min(ans[day][last].ly,bases[i].ly),max(ans[day][last].rx,bases[i].rx),max(ans[day][last].ry,bases[i].ry)};


        }

        return true;
    }

    bool check_split_greedy(vector<int>& sA, vector<Rectangle> bases){

        vector<int> last_use(bases.size(),-1);        

        for (int i = sA.size()-1; i >= 0; i--){

            int a = sA[i];

            int ma_ind = get_base_rect(bases);

            Rectangle& base = bases[ma_ind];

            if (base.area <= 0) return false;

            if (base.wx >= base.wy){
                int need = (a+base.wy-1)/base.wy;
                
                if (need > base.wx){
                    return false;
                }
                sA_rect[i] = (Rectangle){base.lx,base.ly,base.lx+need,base.ry};
                base = (Rectangle){base.lx+need,base.ly,base.rx,base.ry};   

            } else{
                int need = (a+base.wx-1)/base.wx;
                if (need > base.wy){
                    return false;
                }
                sA_rect[i] = (Rectangle){base.lx,base.ly,base.rx,base.ly+need};
                
                base = (Rectangle){base.lx,base.ly+need,base.rx,base.ry};    

            }

            last_use[ma_ind] = i;

            
        }
        for (int i = 0; i < bases.size(); i++){
            if (i == 0 && bases[i].area && last_use[i] == -1){
                adjust_rect = bases[i];
            }

            if (bases[i].area == 0 || last_use[i] == -1) continue;
            int last = last_use[i];

            sA_rect[last] = {min(sA_rect[last].lx,bases[i].lx),min(sA_rect[last].ly,bases[i].ly),max(sA_rect[last].rx,bases[i].rx),max(sA_rect[last].ry,bases[i].ry)};


        }

        return true;
    }

};

int main() {
    Input();
    Solver solver = Solver(d,w,n);
    solver.solve();

    
    return 0;
}