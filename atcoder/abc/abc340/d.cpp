#include <bits/stdc++.h>
using namespace std;
int main()

{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<pair<int, int>>> g(n);
    for (int i = 0; i < n - 1; i++)
    {
        int a, b, x;
        cin >> a >> b >> x;
        x--;
        g[i].emplace_back(i + 1, a);
        g[i].emplace_back(x, b);
    }

    priority_queue<pair<long long, int>> h;
    h.push(pair(0, 0));

    const long long INF = 1e18;
    vector<long long> dist(n, INF);
    dist[0] = 0;
    while (!h.empty())
    {
        auto [d, now] = h.top();
        d *= -1;
        h.pop();
        if (dist[now] != d)
        {
            continue;
        }

        for (auto [nex, nd] : g[now])
        {
            if (dist[nex] > d + nd)
            {
                dist[nex] = d + nd;
                h.push(pair(-dist[nex], nex));
            }
        }
    }

    cout << dist[n - 1] << endl;

    return 0;
}
