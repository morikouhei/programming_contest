#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<int>> P(n,vector<int>(n,0));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> P[i][j];
        }
    }

    vector<vector<int>> R(n,vector<int>(n,0));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n-1; j++){
            cin >> R[i][j];
        }
    }
    vector<vector<int>> D(n,vector<int>(n,0));
    for (int i = 0; i < n-1; i++){
        for (int j = 0; j < n; j++){
            cin >> D[i][j];
        }
    }

    const int INF = 1e9+1;
    P[n-1][n-1] = INF;
    const long long INF2 = 1e20;

    pair<ll,ll> INF3 = {INF2,0};

    vector<vector<pair<ll,ll>>> dp(n,vector<pair<ll,ll>>(n,INF3));
    dp[0][0] = {0,0};

    auto upd = [&](int x, int y, pair<ll,ll> nex){
        if (dp[x][y].first > nex.first){
            dp[x][y] = nex;
        }else if (dp[x][y].first == nex.first){
            if (dp[x][y].second < nex.second){
                dp[x][y] = nex;

            }
        }
    };
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (dp[i][j] == INF3) continue;
            int p = P[i][j];
            vector<vector<ll>> mpath(n-i,vector<ll>(n-j,INF2));
            mpath[0][0] = 0;
            for (int ni = 0; ni < n-i; ni++){
                for (int nj = 0; nj < n-j; nj++){
                    if (mpath[ni][nj] == INF2) continue;
                    if (P[i+ni][j+nj] > p){
                        long long turn = max(0ll,(mpath[ni][nj]-dp[i][j].second+P[i][j]-1)/P[i][j]);
                        pair<ll,ll> nex = {dp[i][j].first+turn+ni+nj,dp[i][j].second+turn*P[i][j]-mpath[ni][nj]};
                        upd(i+ni,j+nj,nex);
                    }

                    if (ni < n-i-1){
                        mpath[ni+1][nj] = min(mpath[ni+1][nj],mpath[ni][nj]+D[i+ni][j+nj]);
                    }
                    if (nj < n-j-1){
                        mpath[ni][nj+1] = min(mpath[ni][nj+1],mpath[ni][nj]+R[i+ni][j+nj]);
                    }
                }
            }

        }
    }
    cout << dp[n-1][n-1].first << endl;

    return 0;

}
