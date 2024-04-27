#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    string S;
    cin >> S;
    vector<long long> C(n);
    for (auto &c: C) cin >> c;
    const long long INF = 1e18;
    vector<vector<long long>> dp(2,vector<long long>(2,INF));
    dp[0][0] = (S[0] == '0' ? 0 : C[0]);
    dp[0][1] = (S[0] == '1' ? 0 : C[0]);

    for (int i = 1; i < n; i++){
        vector<vector<long long>> ndp(2,vector<long long>(2,INF));
        for (int j = 0; j < 2; j++){
            for (int k = 0; k < 2; k++){
                if (dp[j][k] == INF) continue;

                for (int nk = 0; nk < 2; nk++){
                    if (j && k == nk) continue;
                    long long c = (S[i] - '0' == nk ? 0 : C[i]);
                    if (k == nk){
                        ndp[j+1][nk] = min(dp[j][k]+c,ndp[j+1][nk]);
                    } else{
                        ndp[j][nk] = min(dp[j][k]+c,ndp[j][nk]);
                    }
                }
            }
        }
        swap(dp,ndp);
    }

    cout << min(dp[1][0],dp[1][1]) << endl;


    return 0;
}
