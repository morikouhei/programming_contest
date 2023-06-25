#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

class Unionfind {
private:
    vector<int> uf;

public:
    Unionfind(int n) : uf(n, -1) {}

    int find(int x) {
        if (uf[x] < 0)
            return x;
        else {
            uf[x] = find(uf[x]);
            return uf[x];
        }
    }

    bool same(int x, int y) {
        return find(x) == find(y);
    }

    bool unionSet(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y)
            return false;
        if (uf[x] > uf[y])
            swap(x, y);
        uf[x] += uf[y];
        uf[y] = x;
        return true;
    }

    int size(int x) {
        x = find(x);
        return -uf[x];
    }
};

int isqrt(int n) {
    int root = 0;
    int rmdr = 0;
    for (int s = 31; s >= 0; s -= 2) {
        int bits = (n >> s) & 3;
        rmdr = (rmdr << 2) | bits;
        int cand = (root << 2) | 1;
        int bit_next = (rmdr >= cand) ? 1 : 0;
        root = (root << 1) | bit_next;
        rmdr -= cand * bit_next;
    }
    return root;
}

struct Edge {
    int u, v, w;

    Edge(int u, int v, int w) : u(u), v(v), w(w) {}
};

struct House {
    int x, y;

    House(int x, int y) : x(x), y(y) {}
};

struct Power {
    int p, id;

    Power(int p, int id) : p(p), id(id) {}
};

vector<int> P;
vector<int> B;
vector<int> used_house;
vector<int> used_power;
vector<int> power_pos;
vector<vector<int>> all_dist;
vector<vector<pair<int, int>>> all_par;
vector<vector<Power>> power_to_house_dist;

int getDistance(int x1, int y1, int x2, int y2) {
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}

int getPInt(int pSquare) {
    return 1 + isqrt(pSquare - 1);
}

pair<vector<int>, vector<pair<int, int>>> bfs(int s, vector<vector<pair<int, int>>>& e) {
    int n = e.size();
    vector<int> dist(n, 1e9);
    vector<pair<int, int>> par(n, make_pair(-1, -1));
    dist[s] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, s));

    while (!pq.empty()) {
        auto [d, now] = pq.top();
        pq.pop();

        if (dist[now] != d)
            continue;

        for (auto [nex, nd, id] : e[now]) {
            if (dist[nex] > d + nd) {
                dist[nex] = d + nd;
                par[nex] = make_pair(now, id);
                pq.push(make_pair(d + nd, nex));
            }
        }
    }

    return make_pair(dist, par);
}

int bsearchLeftPowerToHouse(int id, int power) {
    int l = 0;
    int r = power_to_house_dist[id].size() + 1;
    while (r > l + 1) {
        int m = (r + l) / 2;
        if (power_to_house_dist[id][m].p <= power)
            l = m;
        else
            r = m;
    }
    return l;
}

void climbUpdate(int s, int pNex, long long& baseScore) {
    int pTarget = bsearchLeftPowerToHouse(s, pNex);
    pNex = power_to_house_dist[s][pTarget].p;
    if (pNex <= P[s])
        return;

    vector<pair<int, int>> upds;
    set<int> calDelSet;

    for (auto [d, id] : power_to_house_dist[s]) {
        if (d <= pNex)
            calDelSet.insert(id);
        else
            break;
    }

    for (int i = 0; i < P.size(); i++) {
        if (i == s)
            continue;

        int nowPos = power_pos[i];
        while (nowPos >= 0) {
            auto [d, id] = power_to_house_dist[i][nowPos];
            if (calDelSet.count(id))
                nowPos--;
            else
                break;
        }

        if (power_pos[i] > nowPos) {
            if (nowPos == -1)
                upds.push_back(make_pair(i, 0));
            else
                upds.push_back(make_pair(i, power_to_house_dist[i][nowPos].p));
        }
    }

    long long dx = 0;
    for (auto [id, pNex] : upds) {
        dx += (long long)pNex * pNex - (long long)P[id] * P[id];
    }

    if (dx <= 0) {
        for (auto [id, pNex] : upds) {
            P[id] = pNex;
            power_pos[id] = bsearchLeftPowerToHouse(id, pNex);
        }
        baseScore += dx;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m, k;
    cin >> n >> m >> k;

    vector<House> XY(n);
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        XY[i] = House(x, y);
    }

    vector<Edge> UVW(m);
    vector<vector<pair<int, int>>> e(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        UVW[i] = Edge(u, v, w);
        e[u].push_back(make_pair(v, w));
        e[v].push_back(make_pair(u, w));
    }

    vector<vector<int>> AB(k, vector<int>(2));
    for (int i = 0; i < k; i++) {
        cin >> AB[i][0] >> AB[i][1];
    }

    P.resize(n, 0);
    B.resize(m, 0);
    used_house.resize(k, 0);
    used_power.resize(n, 0);
    used_power[0] = 1;
    power_pos.resize(n, -1);

    vector<vector<int>> all_dist(n, vector<int>(n, 1e9));
    vector<vector<pair<int, int>>> all_par(n, vector<pair<int, int>>(n));
    for (int i = 0; i < n; i++) {
        auto [dist, par] = bfs(i, e);
        all_dist[i] = dist;
        all_par[i] = par;
    }

    vector<vector<pair<int, int>>> power_to_house_dist;
    for (auto [x, y] : XY) {
        vector<pair<int, int>> power_to_house;
        for (int i = 0; i < k; i++) {
            int d = getDistance(AB[i][0], AB[i][1], x, y);
            d = getPInt(d);
            power_to_house.push_back(make_pair(d, i));
        }
        sort(power_to_house.begin(), power_to_house.end());
        power_to_house_dist.push_back(power_to_house);
    }

    vector<pair<long long, pair<int, int>>> dist_list;
    for (int i = 0; i < k; i++) {
        long long dis = 1e9;
        int id = -1;
        for (int j = 0; j < n; j++) {
            int d = getDistance(AB[i][0], AB[i][1], XY[j].x, XY[j].y);
            if (dis > d) {
                dis = d;
                id = j;
            }
        }
        dist_list.push_back(make_pair(-getPInt(dis), make_pair(i, id)));
    }

    sort(dist_list.begin(), dist_list.end());

    for (auto [d, housePower] : dist_list) {
        auto [houseId, powerId] = housePower;
        if (used_house[houseId])
            continue;
        d *= -1;
        P[powerId] = d;
        used_power[powerId] = 1;

        for (auto [nd, houseId] : power_to_house_dist[powerId]) {
            if (nd <= d)
                used_house[houseId] = 1;
            else
                break;
        }
    }

    vector<pair<int, pair<int, int>>> edges;
    for (int i = 0; i < n; i++) {
        if (used_power[i] == 0)
            continue;
        for (int j = 0; j < i; j++) {
            if (used_power[j] == 0)
                continue;
            edges.push_back(make_pair(all_dist[i][j], make_pair(i, j)));
        }
    }

    sort(edges.begin(), edges.end());

    Unionfind uf(n);
    for (auto [_, edge] : edges) {
        auto [u, v] = edge;
        if (uf.same(u, v))
            continue;
        uf.unionSet(u, v);
        int t = v;
        while (t != u) {
            auto [p, id] = all_par[u][t];
            B[id] = 1;
            t = p;
        }
    }

    long long baseScore = 0;
    for (int i = 0; i < m; i++) {
        if (B[i])
            baseScore += UVW[i].w;
    }

    for (int i = 0; i < n; i++) {
        baseScore += (long long)P[i] * P[i];
    }

    for (int i = 0; i < n; i++) {
        int p = P[i];
        int pLeft = bsearchLeftPowerToHouse(i, p);
        int pLeftMin = (pLeft == -1 ? 0 : power_to_house_dist[i][pLeft].p);
        int pLeftMax = (pLeft + 1 >= power_to_house_dist[i].size() ? 1e9 : power_to_house_dist[i][pLeft + 1].p);
        int pRight = pLeft + 1;
        int pRightMin = (pRight == power_to_house_dist[i].size() ? 1e9 : power_to_house_dist[i][pRight].p);
        int pRightMax = (pRight + 1 >= power_to_house_dist[i].size() ? 1e9 : power_to_house_dist[i][pRight + 1].p);
        int baseP = P[i];
        climbUpdate(i, baseP, baseScore);
        climbUpdate(i, pLeftMin, baseScore);
        climbUpdate(i, pLeftMax, baseScore);
        climbUpdate(i, pRightMin, baseScore);
        climbUpdate(i, pRightMax, baseScore);
    }

    cout << baseScore << endl;
    for (int i = 0; i < n; i++) {
        cout << P[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < m; i++) {
        cout << B[i] << " ";
    }
    cout << endl;

    return 0;
}
