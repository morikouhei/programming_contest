#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
//#include <atcoder/all>

using namespace std;
//using namespace atcoder;

#define ll long long

#ifdef ONLINE_JUDGE
#define NDEBUG
#endif

struct Timer {
    chrono::system_clock::time_point start;
    double elapsed;
 
    void begin() {
        start = chrono::system_clock::now();
    }
 
    double stopwatch() {
        chrono::system_clock::time_point end = chrono::system_clock::now();
        elapsed = chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
        elapsed *= 1e-9; // nanoseconds -> seconds
        return elapsed;
    }
};

inline int randrange(mt19937& engine, int l, int r) {
    assert(l < r);
    return l + engine() % (r - l);
}

uniform_real_distribution<> uniform(0.0, 1.0);

inline bool annealing_scheduler(mt19937& engine, double progress, double delta, double t0, double t1) {
    assert(0.0 <= t1 && t1 <= t0);
    if (0.0 <= delta) {
        return true;
    } else {
        double t = pow(t0, 1.0 - progress) * pow(t1, progress);
        return uniform(engine) < pow(2.0, delta/t);
    }
}

constexpr double time_limit = 1.95;
constexpr int n = 100;
constexpr int max_power = 5000 * 5000;

inline int square_euclid_distance(int x1, int y1, int x2, int y2) {
    return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
}

struct Input {
    int m, k;
    vector<pair<int,int>> xy;
    vector<tuple<int,int,ll>> uvw;
    vector<pair<int,int>> ab;

    vector<vector<tuple<int,int,ll>>> edges; // edges[u] = {{i, v, w} | uvw[i] = {u, v, w}}
    vector<vector<pair<int,int>>> citizens; // citizens[v] is sorted residents less than or equal to max_power(=5000) distance from v

    void input() {
        int _n;
        cin >> _n >> m >> k;

        xy.resize(n);
        for (int i = 0; i < n; ++i) {
            cin >> xy[i].first >> xy[i].second;
        }
        uvw.resize(m);
        for (int i = 0; i < m; ++i) {
            int u, v;
            ll w;
            cin >> u >> v >> w;
            uvw[i] = {--u, --v, w};
        }
        ab.resize(k);
        for (int i = 0; i < k; ++i) {
            cin >> ab[i].first >> ab[i].second;
        }
        init();
    }

    void input(const string& filename) {
        ifstream in(filename);
 
        int _n;
        in >> _n >> m >> k;

        xy.resize(n);
        for (int i = 0; i < n; ++i) {
            in >> xy[i].first >> xy[i].second;
        }
        uvw.resize(m);
        for (int i = 0; i < m; ++i) {
            int u, v;
            ll w;
            in >> u >> v >> w;
            uvw[i] = {--u, --v, w};
        }
        ab.resize(k);
        for (int i = 0; i < k; ++i) {
            in >> ab[i].first >> ab[i].second;
        }
        in.close();

        init();
    }

    void init() {
        // initialize edges
        edges.resize(n);
        for (int i = 0; i < m; ++i) {
            auto [u, v, w] = uvw[i];
            edges[u].push_back({i, v, w});
            edges[v].push_back({i, u, w});
        }
        // initialize citizens
        citizens.resize(n);
        for (int v = 0; v < n; ++v) {
            auto [x, y] = xy[v];
            citizens[v].push_back({0, k});
            for (int i = 0; i < k; ++i) {
                auto [a, b] = ab[i];
                if (square_euclid_distance(x, y, a, b) <= max_power) {
                    citizens[v].push_back({square_euclid_distance(x, y, a, b), i});
                }
            }
            sort(citizens[v].begin(), citizens[v].end());
        }
    }
};

constexpr int expand_nodes = 3;
constexpr double t0 = 5e4;
constexpr double t1 = 1e4;
constexpr int initial_states = 16;
constexpr double patience_time = 0.5;

struct State {
    vector<bool> b;
    vector<bool> b_copy;
    ll p_cost, w_cost;
    ll w_cost_copy;
    vector<int> covering;
    vector<int> covered;
    vector<int> permutation;
    vector<int> expand_history;
    vector<int> shrink_history;
    mt19937 engine;
    double time_stamp;

    State() {}

    State(const Input& input, int seed) {
        b = vector<bool>(input.m, false);
        p_cost = 0;
        w_cost = 0;
        covering = vector<int>(n, 1);
        covered = vector<int>(input.k + 1, 0);
        covered[input.k] = n;
        permutation = vector<int>(n);
        iota(permutation.begin(), permutation.end(), 0);
        expand_history.reserve(input.k);
        shrink_history.reserve(input.k);
        engine = mt19937(seed);
        time_stamp = 0.0;

        for (int v = 0; v < n; ++v) {
            while (covering[v] < (int)input.citizens[v].size()) {
                expand(v, input, false);
            }
        }
        shuffle_permutation();
        greedy_shrink(input);
        steiner_prim(input);
    }

    void greedy_shrink(const Input& input) {
        for (int v : permutation) {
            while (covering[v] > 1 && covered[input.citizens[v][covering[v] - 1].second] > 1) {
                shrink(v, input, true);
            }
        }
    }

    void expand(int v, const Input& input, bool push_history) {
        assert(covering[v] < (int)input.citizens[v].size());
        p_cost += input.citizens[v][covering[v]].first - input.citizens[v][covering[v] - 1].first;
        ++covered[input.citizens[v][covering[v]++].second];
        if (push_history) {
            expand_history.push_back(v);
        }
    }

    void shrink(int v, const Input& input, bool push_history) {
        assert(covering[v] > 1);
        assert(covered[input.citizens[v][covering[v] - 1].second] > 1);
        --covered[input.citizens[v][--covering[v]].second];
        p_cost -= input.citizens[v][covering[v]].first - input.citizens[v][covering[v] - 1].first;
        if (push_history) {
            shrink_history.push_back(v);
        }
    }

    void shuffle_permutation() {
        shuffle(permutation.begin(), permutation.end(), engine);
    }

    void undo(const Input& input) {
        b = b_copy;
        w_cost = w_cost_copy;
        for (int v : shrink_history) {
            expand(v, input, false);
        }
        for (int v : expand_history) {
            shrink(v, input, false);
        }
    }

    void anneal(const Input& input, double progress, double t0, double t1) {
        expand_history.clear();
        shrink_history.clear();

        ll s = p_cost + w_cost;
        shuffle_permutation();
        for (int i = n - expand_nodes; i < n; ++i) {
            int v = permutation[i];
            if ((int)input.citizens[v].size() == covering[v]) {
                continue;
            }
            int cnt = randrange(engine, 1, (int)input.citizens[v].size() - covering[v] + 1);
            while (cnt--) {
                expand(v, input, true);
            }
        }
        greedy_shrink(input);
        steiner_prim(input);

        long long delta = s - (p_cost + w_cost);
        if (!annealing_scheduler(engine, progress, delta, t0, t1)) {
            undo(input);
        }
    }

    void steiner_prim(const Input& input) {
        b_copy = b;
        fill(b.begin(), b.end(), false);
        w_cost_copy = w_cost;
        w_cost = 0;

        int root = 0;
        vector<ll> costs(n, 1ll << 60);
        costs[root] = 0;
        priority_queue<pair<ll,int>> todo;
        todo.push({0, root});

        while (!todo.empty()) {
            auto [cost, u] = todo.top();
            todo.pop();
            cost = -cost;
            if (costs[u] < cost) {
                continue;
            }
            if (covering[u] > 1 && cost) {
                while (costs[u]) {
                    todo.push({0, u});
                    for (auto [i, v, w] : input.edges[u]) {
                        if (costs[v] + w == costs[u]) {
                            costs[u] = 0;
                            b[i] = true;
                            w_cost += w;
                            u = v;
                            break;
                        }
                    }
                }
            } else {
                for (auto [i, v, w] : input.edges[u]) {
                    if (cost + w < costs[v]) {
                        costs[v] = cost + w;
                        todo.push({-(cost + w), v});
                    }
                }
            }
        }
    }

    void print(const Input& input) {
        for (int v = 0; v < n; ++v) {
            cout << (int)ceil(sqrt(input.citizens[v][covering[v] - 1].first));
            if (v == n - 1) {
                cout << "\n";
            } else {
                cout << " ";
            }
        }
        for (int i = 0; i < input.m; ++i) {
            cout << b[i];
            if (i == input.m - 1) {
                cout << "\n";
            } else {
                cout << " ";
            }
        }
    }

    ll score() {
        return round(1e6 * (1.0 + 1e8 / (p_cost + w_cost + 1e7)));
    }
};

struct Solver {
    Timer timer;
    Input input;
    State best;

    Solver(const Input& _input) {
        timer.begin();
        input = _input;
        best = State(input, 0);
    }

    void solve() {
        vector<State> states;
        for (int i = 0; i < initial_states; ++i) {
            states.emplace_back(State(input, i));
        }
        while (timer.stopwatch() < time_limit) {
            double progress = timer.elapsed / time_limit;
            for (int i = 0; i < (int)states.size(); ++i) {
                states[i].anneal(input, progress, t0, t1);
                if (states[i].p_cost + states[i].w_cost < best.p_cost + best.w_cost) {
                    best = states[i];
                    states[i].time_stamp = timer.elapsed;
                } else if (timer.elapsed - states[i].time_stamp > patience_time && states.size() > 1) {
                    states.erase(states.begin() + i);
                }
            }
        }
    }

    void print() {
        best.print(input);
    }

    ll score() {
        return best.score();
    }
};

void multi_test(int cases) {
    // cerr << "cases: " << cases << endl;
    ll sum_scores = 0;
    for (int seed = 1; seed < cases + 1; ++seed) {
        string filename = "in/";
        filename += '0' + seed / 1000;
        filename += '0' + (seed / 100) % 10;
        filename += '0' + (seed / 10) % 10;
        filename += '0' + seed % 10;
        filename += ".txt";
 
        Timer timer;
        timer.begin();
 
        Input input;
        input.input(filename);
 
        Solver solver(input);
        solver.solve();
 
        double elapsed_time = timer.stopwatch();
 
        // cerr << filename << " " << solver.score() << " " << elapsed_time << " sec" << endl;
 
        sum_scores += solver.score();
        cout << solver.score();
    }
    // cerr << "Average Score: " << sum_scores / cases << endl;
}

int main() {
    Input input;
    input.input();

    Solver solver(input);
    solver.solve();
    solver.print();
    cout << solver.score() << endl;

// #ifndef ONLINE_JUDGE
//     int cases = 1;
//     multi_test(cases);
// #endif
}
