#include <bits/stdc++.h>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>

using namespace std;
using namespace chrono;
using ll = long long;
uint64_t rand_seed = 123456789;
uint64_t xorshift64() {
	rand_seed ^= rand_seed << 13;
	rand_seed ^= rand_seed >> 7;
	rand_seed ^= rand_seed << 17;
	return rand_seed;
}
int rand_int(int l, int r) {
	return l + int(xorshift64() % (r - l));
}

float TIME_LIM = 6;
const int center=1000,SPLIT=10,inf=1e9;
int n,m,d,k;
const int MAX = 3005;
int U[MAX],V[MAX], W[MAX],X[MAX],Y[MAX];

struct edge {
  int to, id;
  ll cost;
  edge() {}
  edge(int to, ll cost,int id): to(to), cost(cost),id(id) {}
};

vector<vector<edge> > G(MAX);
ll dist_sum(vector<int> used,vector<int> dist_point,int n)
{
    ll dist_count = 0;
    for (int i=0;i<2;i++){
        vector<ll> dist(n,inf);
        int s = dist_point[i];
        queue<int> que;
        que.push(s);  // sから探索する
        dist[s] = 0;
        while (que.size() != 0) {     // 幅優先探索
            int state = que.front(); que.pop();
            for (auto next : G[state]) {
                if (used[next.id]) continue;
                ll nd = dist[state] + next.cost;
                if (nd < dist[next.to]) {  // 未探索の時のみ行う
                    dist[next.to] = nd;
                    que.push(next.to);  //次の状態をqueueへ格納
                }
            }
        }
        for (int j = 0;j<n;j++){
            dist_count += dist[j];
        }

        
    }
    return dist_count;
}

int main() {
    auto startClock = system_clock::now();
    cin >> n >> m >> d >> k;
    for (int i = 0;i < m;i++){
        cin >> U[i] >> V[i] >> W[i];
        U[i]--;
        V[i]--;
    }  
    pair<int,int> xma = make_pair(-inf,-1);
    pair<int,int> xmi = make_pair(inf,-1);
    pair<int,int> yma = make_pair(-inf,-1);
    pair<int,int> ymi = make_pair(inf,-1);

    for (int i = 0;i<n;i++){
        cin >> X[i] >> Y[i];
        if (xma.first < X[i]){
            xma.first = X[i];
            xma.second = i;
        }
        if (xmi.first >X[i]){
            xmi.first = X[i];
            xmi.second = i;
        }

        if (yma.first < Y[i]){
            yma.first = Y[i];
            yma.second = i;
        }
        if (ymi.first >Y[i]){
            ymi.first = Y[i];
            ymi.second = i;
        }
    }

    vector<int> dist_point = {xma.second,xmi.second,yma.second,ymi.second};
    // vector<int> dist_point = {xma.second,xmi.second};

    for (int i = 0; i < m; i++) {
        int u=U[i],v=V[i],w=W[i];
        G[u].emplace_back(v,w,i);
        G[v].emplace_back(u,w,i);

    }

    // vector<int> nX(n),nY(n);
    // for (int i=0;i<n;i++){
    //     nX[i] = X[i]*2-center;
    //     nY[i] = Y[i]*2-center;
    // }
    // vector<vector<int> > radius(SPLIT);
    // vector<int> lim;
    // for (int i=1;i<=SPLIT;i++){
    //     int l = i*100*i*100;
    //     lim.push_back(l);
    // }
    // for (int i = 0;i<m;i++){
    //     int u = U[i],v = V[i];
    //     int x = nX[u],y=nY[u];
    //     int nx=nX[v],ny=nY[v];

    //     int cx = (x+nx)/2;
    //     int cy = (y+ny)/2;

    //     int rxy = cx*cx+cy*cy;
    //     for (int j = 0;j<SPLIT;j++){
    //         if (rxy <= lim[j]){
    //             radius[j].push_back(i);
    //             break;
    //         }
    //     }
    // }
    // vector<int> pos_R(m);

    // int now = 0;
    // for (int i=0;i<SPLIT;i++){
    //     vector rad = radius[i];
    //     random_device seed_gen;
    //     mt19937 engine(seed_gen());
    //     shuffle(rad.begin(), rad.end(), engine);

    //     for (auto x: rad){
    //         pos_R[x] = now+1;
    //         now = (now+1)%d;
    //     }
    // }

    vector<int> pos_R;

    for (int i = 1; i<=d;i++){
        int need = m/d;
        if (m%d >= i) need++;
        for (int j = 0;j<need;j++){
            pos_R.push_back(i);
        }
    }
    random_device seed_gen;
    mt19937 engine(seed_gen());
    shuffle(pos_R.begin(), pos_R.end(), engine);


    vector<vector<int> > DayInfos(d,vector<int>(m,0));
    for (int i=0;i<m;i++){
        int r = pos_R[i];
        DayInfos[r-1][i] = 1;
    }
  
    // for (int i = 0;i<d;i++){
    //     int num = 0;
    //     for (int j = 0;j<m;j++){
    //         num += DayInfos[i][j];
    //     }
    //     cout << "day" << i+1 << " dist = " << dist_sum(DayInfos[i],dist_point,n) << " " << dist_point.size() << " " << num << endl;
    // }
    vector<int> upd_score(d,0);
    vector<ll> score(d,0);
    const static double END_TIME = TIME_LIM - 0.3;
    int n1=0,n2=0;
    while (true)
    {        
        if (n1%100 == 0){
            const double time = duration_cast<microseconds>(system_clock::now() - startClock).count() * 1e-6;   // 経過時間（秒）
            if (time >= END_TIME)
            {
                break;
            }
        }
        int e1 = rand_int(0,m-1), e2 = rand_int(0,m-1);
        int d1 = pos_R[e1]-1, d2 = pos_R[e2]-1;
        n1++;
        if (d1 == d2) continue;
        n2++;
        ll dist1,dist2;
        if (upd_score[d1]){
            dist1 = score[d1];
        } else{
            dist1 = dist_sum(DayInfos[d1],dist_point,n);
        }
        if (upd_score[d2]){
            dist2 = score[d2];
        } else{
            dist2 = dist_sum(DayInfos[d2],dist_point,n);
        }
 
        ll base_score = dist1+dist2;

        DayInfos[d1][e1] = 0,DayInfos[d1][e2] = 1;
        DayInfos[d2][e1] = 1,DayInfos[d2][e2] = 0;

        ll ndist1 = dist_sum(DayInfos[d1],dist_point,n);
        ll ndist2 = dist_sum(DayInfos[d2],dist_point,n);

        if (ndist1+ndist2 > base_score){
            DayInfos[d1][e1] = 1,DayInfos[d1][e2] = 0;
            DayInfos[d2][e1] = 0,DayInfos[d2][e2] = 1;
            upd_score[d1] = 1;
            upd_score[d2] = 1;
            score[d1] = dist1;
            score[d2] = dist2;
        } else{
            upd_score[d1] = 1;
            upd_score[d2] = 1;
            score[d1] = ndist1;
            score[d2] = ndist2;
            pos_R[e1] = d2+1;
            pos_R[e2] = d1+1;

        }
    }
    // cout << n1 << " " << n2 << endl;
    // for (int i = 0;i<d;i++){
    //     int num = 0;
    //     for (int j = 0;j<m;j++){
    //         num += DayInfos[i][j];
    //     }
    //     cout << "day" << i+1 << " dist = " << dist_sum(DayInfos[i],dist_point,n) << " " << dist_point.size() << " " << num << endl;
    // }

    for (int i=0;i<m;i++){
        cout << pos_R[i] << " ";
    }
    cout << endl;

    return 0;
}