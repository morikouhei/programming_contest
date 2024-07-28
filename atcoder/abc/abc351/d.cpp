#include <bits/stdc++.h>
using namespace std;

int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h,w;
    cin >> h >> w;
    vector<string> S(h);
    for (auto &s: S) cin >> s;

    int ans = 0;
    int time = 0;
    vector<vector<int>> used(h,vector<int>(w));
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            if (used[i][j]) continue;
            if (S[i][j] == '#') continue;
            time++;
            int count = 0;
            used[i][j] = time;
            vector<pair<int,int>> q;
            q.push_back({i,j});

            while (!q.empty()){
                auto [x,y] = q.back(); q.pop_back();
                count++;
                int num = 0;
                for (int dir = 0; dir < 4; dir++){
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    if (0 <= nx && nx < h && 0 <= ny && ny < w && S[nx][ny] == '#'){
                        num++;
                    }
                }
                if (num) continue;

                for (int dir = 0; dir < 4; dir++){
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    if (0 <= nx && nx < h && 0 <= ny && ny < w && S[nx][ny] == '.' && used[nx][ny] != time){
                        used[nx][ny] = time;
                        q.push_back({nx,ny});
                    }
                }
            }

            ans = max(ans,count);
        }
    }

    cout << ans << endl;

    return 0;
}
