#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m;
    cin >> n >> m;
    vector<vector<int>> A(n,vector<int>(m));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> A[i][j];
        }
    }

    vector<vector<bitset<2000>>> bs(m,vector<bitset<2000>>(1000));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            bs[j][A[i][j]].set(i);
        }
    }

    int ans = 0;
    for (int i = 0; i < n; i++){
        bitset<2000> b;

        for (int j = 0; j < m; j++){
            b ^= bs[j][A[i][j]];
        }

        ans += b.count();
    }
    if (m&1) ans -= n;

    cout << ans/2 << endl;


    return 0;
}
