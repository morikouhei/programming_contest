#include <bits/stdc++.h>
#include <atcoder/dsu>
#include <atcoder/modint>
using namespace atcoder;
using namespace std;
using mint = atcoder::modint998244353;

vector<int> dx = {1, 0, -1, 0};
vector<int> dy = {0, 1, 0, -1};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    cin >> H >> W;

    dsu uf(H * W);

    vector<string> S(H);
    for (int i = 0; i < H; i++)
    {
        cin >> S[i];
    }

    for (int x = 0; x < H; x++)
    {
        for (int y = 0; y < W; y++)
        {
            if (S[x][y] == '.')
                continue;

            int id = x * W + y;

            for (int i = 0; i < 4; i++)
            {
                int nx, ny;
                nx = x + dx[i];
                ny = y + dy[i];

                if (0 <= nx && nx < H && 0 <= ny && ny < W && S[nx][ny] != '.')
                {
                    uf.merge(id, nx * W + ny);
                }
            }
        }
    }

    int count = 0;
    int num = 0;
    for (int x = 0; x < H; x++)
    {
        for (int y = 0; y < W; y++)
        {

            if (S[x][y] == '.')
            {
                count++;
                continue;
            }
            if (uf.leader(x * W + y) == x * W + y)
                num++;
        }
    }
    mint ans = 0;
    for (int x = 0; x < H; x++)
    {
        for (int y = 0; y < W; y++)
        {
            if (S[x][y] == '#')
                continue;

            set<int> s;

            for (int i = 0; i < 4; i++)
            {
                int nx, ny;
                nx = x + dx[i];
                ny = y + dy[i];

                if (0 <= nx && nx < H && 0 <= ny && ny < W && S[nx][ny] == '#')
                {
                    s.insert(uf.leader(nx * W + ny));
                }
            }
            if (s.size() == 0)
                ans += num + 1;
            else
            {
                ans += num - s.size() + 1;
            }
        }
    }
    ans /= count;
    cout << ans.val() << endl;

    return 0;
}
