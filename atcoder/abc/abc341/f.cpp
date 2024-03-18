#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m;
    cin >> n >> m;
    vector<vector<int>> e(n);
    for (int i = 0; i < m; i++){
        int u,v;
        cin >> u >> v;
        u--;v--;
        e[u].push_back(v);
        e[v].push_back(u);
    }

    vector<int> W(n),A(n);
    for (auto &w : W) cin >> w;
    for (auto &a : A) cin >> a;
    vector<int> Ord(n);
    for (int i = 0 ; i < n; i++){
        Ord[i] = i;
    }

    sort(Ord.begin(),Ord.end(),[&](int a, int b){
        return W[a] < W[b];
    });

    vector<long long> ans(n,0);

    for (int i = 0; i < n; i++){

        int w = W[Ord[i]];
        vector<long long> dp(w,0);

        dp[0] = 1;

        for (auto ni : e[Ord[i]]){
            int nw = W[ni];
            if (w <= nw) continue;

            for (int j = w-1; j >= 0; j--){
                if (j + nw < w){
                    dp[j+nw] = max(dp[j+nw],dp[j] + ans[ni]);
                }
            }
        }
        ans[Ord[i]] = *max_element(dp.begin(),dp.end());

    }

    long long num = 0;
    for (int i = 0; i < n; i++){
        num += A[i] * ans[i];
    }

    cout << num << endl;
    return 0;
}
