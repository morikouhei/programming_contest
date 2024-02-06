#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    const int INF = 1e9;

    vector<vector<int>> dist(n, vector<int>(n, INF));

    for (int i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        dist[u][v] = w;
    }

    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (dist[i][k] == INF || dist[k][j] == INF)
                {
                    continue;
                }
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    int n2 = 1 << n;
    vector<vector<int>> dp(n, vector<int>(n2, INF));

    for (int i = 0; i < n; i++)
    {
        dp[i][1 << i] = 0;
    }

    for (int bi = 0; bi < n2; bi++)
    {
        for (int i = 0; i < n; i++)
        {
            if (dp[i][bi] == INF)
            {
                continue;
            }

            for (int j = 0; j < n; j++)
            {
                if (bi >> j & 1 || dist[i][j] == INF)
                {
                    continue;
                }
                dp[j][bi | 1 << j] = min(dp[j][bi | 1 << j], dp[i][bi] + dist[i][j]);
            }
        }
    }
    int ans = INF;
    for (int i = 0; i < n; i++)
    {
        if (dp[i][n2 - 1] != INF)
        {
            ans = min(ans, dp[i][n2 - 1]);
        }
    }
    if (ans == INF)
    {
        cout << "No" << endl;
    }
    else
    {
        cout << ans << endl;
    }
    return 0;
}
