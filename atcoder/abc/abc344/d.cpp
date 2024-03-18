#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string T;
    cin >> T;
    int ma = T.length() + 1;
    const int INF = 1e9;
    vector<int> dp(ma,INF);
    dp[0] = 0;
    cout << ma << endl;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        int a;
        cin >> a;
        vector<string> S(a);
        for (auto& s: S) cin >> s;

        for (int j = ma-1; j >= 0; j--){
            if (dp[j] == INF) continue;

            for (auto s: S){
                int nj = j + s.length();
                if (nj >= ma) continue;
                int ok = 1;
                for (int p = 0; p < s.length(); p++){
                    if (T[j+p] != s[p]){
                        ok = 0;
                        break;
                    }
                }
                if (ok){
                    dp[nj] = min(dp[nj],dp[j]+1);
                }
            }
        }
    }
    int ans = dp[ma-1];
    if (ans == INF) ans = -1;
    cout << ans << endl;
    return 0;
}
