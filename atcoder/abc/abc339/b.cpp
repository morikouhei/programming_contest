#include <bits/stdc++.h>
using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, n;
    cin >> h >> w >> n;

    vector<string> ans(h, string(w, '.'));

    int dir = 0;
    int x = 0, y = 0;

    for (int i = 0; i < n; i++)
    {
        if (ans[x][y] == '.')
        {
            ans[x][y] = '#';
            dir = (dir + 1) % 4;
        }
        else
        {
            ans[x][y] = '.';
            dir = (dir + 3) % 4;
        }

        x += dx[dir];
        y += dy[dir];

        x = (x + h) % h;
        y = (y + w) % w;
    }

    for (int i = 0; i < h; i++)
    {
        cout << ans[i] << endl;
    }

    return 0;
}
