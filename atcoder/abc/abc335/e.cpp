
#include <bits/stdc++.h>
using namespace std;
int main()

{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> A(n);
    for (int i = 0; i < n; i++)
        cin >> A[i];

    vector<vector<int>> e(n);

    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        if (A[u] >= A[v])
        {
            e[v].push_back(u);
        }
        if (A[v] >= A[u])
        {
            e[u].push_back(v);
        }
    }

    vector<vector<int>> sA(2e5 + 5);
    for (int i = 0; i < n; i++)
    {
        sA[A[i]].push_back(i);
    }

    vector<int> dp(n);
    dp[0] = 1;

    for (int i = 0; i <= 2e5; i++)
    {

        priority_queue<pair<int, int>> h;

        for (int now : sA[i])
        {
            if (dp[now] == 0)
                continue;
            h.push(make_pair(dp[now], now));
        }

        while (!h.empty())
        {
            auto [d, pos] = h.top();
            h.pop();
            if (dp[pos] != d)
                continue;

            for (int nex : e[pos])
            {
                if (A[pos] == A[nex])
                {
                    if (dp[nex] < dp[pos])
                    {
                        dp[nex] = dp[pos];
                        h.push(make_pair(dp[nex], nex));
                    }
                }
                else
                {
                    dp[nex] = max(dp[nex], dp[pos] + 1);
                }
            }
        }
    }

    int ans = dp[n - 1];
    cout << ans << endl;

    return 0;
}
