#include <bits/stdc++.h>
using namespace std;

struct Edge{
    int to,id;
    Edge(int t=-1, int i=-1): to(t),id(i) {}
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m,k;
    cin >> n >> m >> k;

    vector<vector<Edge>> e(n);
    for (int i = 1; i <= m; i++){
        int u,v;
        cin >> u >> v;
        u--;v--;
        e[u].push_back(Edge(v,i));
        e[v].push_back(Edge(u,i));

    }

    if (k&1){
        cout << "No" << endl;
        return 0;
    }

    vector<Edge> p(n);
    vector<int> used(n,0);
    vector<int> s(n,0);
    vector<int> ans;

    auto dfs = [&](auto dfs, int now) -> void {
        used[now] = 1;
        for (Edge nex: e[now]){
            if (used[nex.to]) continue;
            p[nex.to] = Edge(now,nex.id);
            dfs(dfs,nex.to);
        }

        int par = p[now].to;
        int ei = p[now].id;

        cout << now << " " << par << " " << ei << " " << k << endl;
        for (auto x: s){
            cout << x << " ";
        }
        cout << endl;

        if (k && s[now] == 0 && par != -1){
            ans.push_back(ei);
            k -= 1^s[now];
            k -= (s[par]==0? 1: -1);
            s[now] ^= 1;
            s[par] ^= 1;
        }
    };

    for (int i = 0; i < n; i++){
        if (used[i]) continue;
        dfs(dfs,i);
    }
    if (k != 0){
        cout << "No" << endl;
    } else{
        cout << "Yes" << endl;
        cout << ans.size() << endl;
        for (auto a: ans){
            cout << a << " ";
        }
        cout << endl;
    }
    
    return 0;
}
