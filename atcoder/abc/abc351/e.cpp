#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<vector<vector<long long>>> posX(2,vector<vector<long long>>(2,vector<long long>()));
    vector<vector<vector<long long>>> posY(2,vector<vector<long long>>(2,vector<long long>()));

    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        long long a,b;
        cin >> a >> b;
        long long x = a+b;
        long long y = a-b;
        int ni = (x%2+2)%2;
        int nj = (y%2+2)%2;
        posX[ni][nj].push_back(x);
        posY[ni][nj].push_back(y);

    }

    long long ans = 0;

    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 2; j++){
            {
                sort(posX[i][j].begin(),posX[i][j].end());
                long long sum = 0;
                for (auto x: posX[i][j]) sum += x;
                long long size = posX[i][j].size();

                for (int pos = 0; pos < posX[i][j].size(); pos++){
                    sum -= posX[i][j][pos];
                    ans += sum - posX[i][j][pos] * (size-pos-1);
                }
            }
            {
                sort(posY[i][j].begin(),posY[i][j].end());
                long long sum = 0;
                for (auto x: posY[i][j]) sum += x;
                long long size = posY[i][j].size();

                for (int pos = 0; pos < posY[i][j].size(); pos++){
                    sum -= posY[i][j][pos];
                    ans += sum - posY[i][j][pos] * (size-pos-1);
                }
            }

        }
    }
    cout << ans/2 << endl;

    return 0;
}
