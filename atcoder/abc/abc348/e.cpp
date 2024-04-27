#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<int>> e(n);
    for (int i = 0; i < n-1; i++){
        int a,b;
        cin >> a >> b;
        a--;
        b--;
        e[a].push_back(b);
        e[b].push_back(a);
    }
    vector<long long> C(n);
    for (auto &c: C) cin >> c;


    const long long INF = 4e18;

    vector<long long> num(n,0);
    vector<int> par(n,-1);
    vector<long long> Csum(n,0);

    auto dfs = [&](auto dfs, int now) -> long long {
        long long count = 0;
        Csum[now] += C[now];
        for (auto nex: e[now]){
            if (nex == par[now]) continue;
            par[nex] = now;
            count += dfs(dfs,nex);
            Csum[now] += Csum[nex];
        }
        num[now] = count + Csum[now] - C[now];
        return num[now];
    };

    dfs(dfs,0);

    long long ans = INF;

    auto dfs2 = [&](auto dfs2, int now, long long pnum, long long cs) -> void {
        ans = min(ans,num[now] + pnum + cs);

        for (auto nex: e[now]){
            if (nex == par[now]) continue;
            dfs2(dfs2,nex,pnum + cs + num[now] - num[nex] - Csum[nex], cs + Csum[now] - Csum[nex]);
        }
    };

    dfs2(dfs2,0,0,0);

    cout << ans << endl;

    return 0;
}
