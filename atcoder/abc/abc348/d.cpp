#include <bits/stdc++.h>
using namespace std;

struct medicine {
    int r,c,e;
    medicine() {}
    medicine(int r, int c, int e): r(r),c(c),e(e) {}
};

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h,w;
    cin >> h >> w;
    vector<string> A(h);
    for (auto &a: A) cin >> a;
    int si,sj,ti,tj;
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            if (A[i][j] == 'S') si = i, sj = j;
            if (A[i][j] == 'T') ti = i, tj = j;
        }
    }
    int n;
    cin >> n;
    vector<medicine> medicines;

    medicines.push_back({si,sj,0});
    medicines.push_back({ti,tj,0});

    for (int i = 0; i < n; i++){
        int r,c,e;
        cin >> r >> c >> e;
        r--;
        c--;
        medicines.push_back({r,c,e});
    }

    const int INF = 1e9;

    vector<vector<int>> g(n+2);
    for (int id = 0; id < n+2; id++){
        auto [r,c,e] = medicines[id];

        vector<vector<int>> dist(h,vector<int>(w,INF));
        dist[r][c] = 0;
        queue<pair<int,int>> q;
        q.push({r,c});
        while (!q.empty()){
            auto [x,y] = q.front(); q.pop();
            for (int dir = 0; dir < 4; dir++){
                int nx = x + dx[dir];
                int ny = y + dy[dir];
                if (0 > nx || nx >= h || 0 > ny || ny >= w) continue;
                if (A[nx][ny] == '#') continue;
                if (dist[nx][ny] > dist[x][y]+1){
                    dist[nx][ny] = dist[x][y] + 1;
                    q.push({nx,ny});
                }
            }
        }

        for (int i = 0; i < n+2; i++){
            auto [nr,nc,ne] = medicines[i];
            if (dist[nr][nc] <= e){
                g[id].push_back(i);
            }
        }
    }

    vector<int> dist(n+2,INF);
    dist[0] = 0;
    queue<int> q;
    q.push(0);
    while (!q.empty()){
        auto now = q.front(); q.pop();
        for (auto nex: g[now]){
            if (dist[nex] > dist[now]+1){
                q.push(nex);
                dist[nex] = dist[now]+1;
            }
        }
    }

    if (dist[1] != INF){
        cout << "Yes" << endl;
    } else{
        cout << "No" << endl;
    }


    return 0;
}
