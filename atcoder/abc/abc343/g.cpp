#include <iostream>
#include <vector>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<string> S(n);
    for (auto& s: S) cin >> s;

    sort(S.begin(),S.end(),[&](string& a, string& b){
        return a.size() > b.size();
    });

    vector<string> nS;

    for (auto& s: S){

        int ok = 1;

        for (auto& ns: nS){

            string t = s + "#" + ns;
            vector<int> za = z_algorithm(t);

            for (int i = 1; i < za.size(); i++){
                if (za[i] == s.size()) ok = 0;
            }
        }
        if (ok) nS.push_back(s);
    }

    n = nS.size();
    S = nS;

    const int INF = 1e9;
    vector<vector<int>> dist(n,vector<int>(n,INF));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (i == j) continue;

            dist[i][j] = S[j].size();

            string t = S[j] + "#" + S[i];

            vector<int> za = z_algorithm(t);

            for (int pos = 1; pos <= S[j].size(); pos++){
                if (za[t.size()-pos] == pos) dist[i][j] = S[j].size() - pos;
            }
        }
    }

    int n2 = 1<<n;
    vector<vector<int>> dp(n2,vector<int>(n,INF));
    for (int i = 0; i < n; i++){
        dp[1<<i][i] = S[i].size();
    }

    for (int b = 0; b < n2; b++){
        for (int i = 0; i < n; i++){
            if (dp[b][i] == INF) continue;

            for (int j = 0; j < n; j++){
                if (b >> j & 1) continue;
                dp[b|1<<j][j] = min(dp[b|1<<j][j],dp[b][i] + dist[i][j]);
            }
        }
    }

    int ans = INF;
    for (int i = 0; i < n; i++){
        ans = min(ans,dp[n2-1][i]);
    }

    cout << ans << endl;



}
