#include<bits/stdc++.h>
using namespace std;

vector<int> dx = {0,1,0,-1};
vector<int> dy = {1,0,-1,0};

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int n;
    cin >> n;

    vector<vector<int>> ans(n,vector<int>(n,0));

    int x=0,y=0;

    
    int dir = 0;
    for (int i=1;i <= n*n;i++){

        ans[x][y] = i;

        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if (0 <= nx && nx < n && 0 <= ny && ny < n && ans[nx][ny] == 0){
            x = nx;
            y = ny;
            continue;
        }
        dir = (dir+1)%4;

        x = x + dx[dir];
        y = y + dy[dir];
    }

    for (int i = 0;i < n ;i++){
        for (int j = 0;j<n;j++){
            if (ans[i][j] == n*n){
                cout << "T ";
            }else{
                cout << ans[i][j] << " ";
            }
        }
        cout << endl;
    }
    return 0;

}
