#include <bits/stdc++.h>
using namespace std;
using P = pair<long long,int>;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m;
    cin >> n >> m;
    vector<vector<pair<int,int>>> e(n);
    vector<long long> L(m),D(m),K(m),C(m);

    for (int i = 0; i < m; i++){
        cin >> L[i] >> D[i] >> K[i] >> C[i];
        int a,b;
        cin >> a >> b;
        a--;
        b--;
        e[b].push_back({a,i});
    }

    priority_queue<P> h;
    const long long INF = 4e18;

    vector<long long> dist(n,-1);

    auto push = [&](int now, int nex, int ind,long long t){
        long long mt = L[ind]+C[ind];

        if (mt > t) return ;

        long long nt = (t-mt) / D[ind];
        if (nt >= K[ind]) nt = K[ind]-1;

        long long ndist = L[ind] + D[ind] * nt;

        if (ndist > dist[nex]){
            dist[nex] = ndist;
            h.push({ndist,nex});
        }
        
    };

    dist[n-1] = INF;
    h.push({INF,n-1});

    while (!h.empty()){
        auto [d,now] = h.top();h.pop();

        if (dist[now] != d) continue;

        for (auto& [nex,ind] : e[now]){
            push(now,nex,ind,d);
        }
    }

    for (int i = 0; i < n-1; i++){
        long long ans = dist[i];

        if (ans == -1){
            cout << "Unreachable" << "\n";
        } else{
            cout << ans << "\n";
        }
    }

}
