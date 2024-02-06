#include <bits/stdc++.h>
using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<string> S(n);
    for (int i = 0; i < n; i++)
    {
        cin >> S[i];
    }
    const int INF = 1e9;

    vector<vector<int>> dist(n * n, vector<int>(n * n, INF));

    queue<pair<int, int>> que;
    vector<int> P;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (S[i][j] == 'P')
            {
                P.push_back(i * n + j);
            }
        }
    }
    que.push(pair(P[0], P[1]));
    dist[P[0]][P[1]] = 0;

    auto move_id = [&](int x, int y, int dir)
    {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if (nx < 0 || nx >= n || ny < 0 || ny >= n || S[nx][ny] == '#')
        {
            nx = x;
            ny = y;
        }
        return nx * n + ny;
    };

    int ans = INF;

    while (!que.empty())
    {

        auto [id1, id2] = que.front();
        que.pop();

        if (id1 == id2)
        {
            ans = min(ans, dist[id1][id2]);
        }
        int x1 = id1 / n, y1 = id1 % n;
        int x2 = id2 / n, y2 = id2 % n;

        for (int dir = 0; dir < 4; dir++)
        {
            int nid1 = move_id(x1, y1, dir);
            int nid2 = move_id(x2, y2, dir);

            if (dist[nid1][nid2] > dist[id1][id2] + 1)
            {
                dist[nid1][nid2] = dist[id1][id2] + 1;
                que.push(pair(nid1, nid2));
            }
        }
    }
    if (ans == INF)
    {
        ans = -1;
    }

    cout << ans << endl;

    return 0;
}
