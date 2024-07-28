#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m;
    cin >> n >> m;

    vector<vector<int>> info(n,vector<int>(n,0));
    for (int i = 0; i < m; i++){
        int a,b,c;
        cin >> a >> b >> c;
        a--;
        b--;
        info[a][b] = c;
        info[b][a] = -c;
    }

    vector<pair<vector<int>,int>> groups;
    vector<bool> used(n);

    for (int i = 0; i < n; i++){
        if (used[i]) continue;
        int gb = 1 << i;
        used[i] = true;
        vector<int> relation(n);
        vector<int> q;
        q.push_back(i);
        while (!q.empty()){
            int now = q.back();
            q.pop_back();

            for (int nex = 0; nex < n; nex++){
                if (info[now][nex] == 0 || (gb >> nex & 1)) continue;
                gb |= 1<<nex;
                relation[nex] = relation[now] + info[now][nex];
                q.push_back(nex);
                used[nex] = true;
            }
        }

        int mi = n+1;
        for (auto r: relation){
            mi = min(mi,r);
        }
        for (auto &r: relation){
            r -= mi;
        }
        int ord = 0;
        vector<int> group;
        for (int j = 0; j < n; j++){
            if (gb >> j & 1){
                ord |= 1<<relation[j];
                group.push_back(j);
            }
        }
        sort(group.begin(),group.end(),[&](int i, int j){
            return relation[i] < relation[j];
        });

        groups.push_back({group,ord});
    }
    

    int ng = groups.size();
    int n2 = 1<<n;
    vector<int> ans(n,-1);

    for (int i = 0; i < ng; i++){
        vector<int> dp(n2);
        dp[0] = 1;
        for (int j = 0; j < ng; j++){
            if (i == j) continue;
            auto [gb,ord] = groups[j];

            for (int b = n2-1; b >= 0; b--){
                if (dp[b] == 0) continue;
                for (int ni = 0; ni < n; ni++){
                    if (b & (ord<<ni)) continue;
                    int nb = b | (ord<<ni);
                    if (nb < n2) dp[nb] = 1;
                }
            }
        }

        auto [gb,ord] = groups[i];
        vector<int> match;
        for (int b = 0; b < n2; b++){
            if (dp[b] == 0) continue;

            for (int ni = 0; ni < n; ni++){
                if (b & (ord<<ni)) continue;
                int nb = b | (ord<<ni);
                if (nb == n2-1) {
                    match.push_back(ord<<ni);
                }
            }
        }
        assert (match.size());

        if (match.size() > 1) continue;
        int pos = 0;

        int ma = match[0];

        for (int j = 0; j < n; j++){
            if (ma >> j & 1){
                ans[gb[pos]] = n-j;
                pos++;
            }
        }
    }

    for (auto a: ans){
        cout << a << " ";
    }
    cout << endl;

    return 0;
}
