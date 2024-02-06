#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int n;
    cin >> n;
    // n++;
    int m = 0;

    while (1<<m < n) m++;

    cout << m << endl;

    vector<vector<int>> drink(n+1,vector<int>(m,0));

    for (int i = 1; i < n; i++){
        for (int j = 0; j < m; j++){
            if (i >> j & 1) drink[i][j] = 1;
        }
    }

    for (int i = 0;i < m; i++){
        vector<int> K;
        for (int j = 1; j < n; j++){
            if (drink[j][i]){
                K.push_back(j);
            }
        }
        assert (K.size() < n);
        cout << K.size() << " ";
        for (auto a: K) cout << a << " ";
        cout << endl;
    }

    string S;
    cin >> S;

    int ans = 0;
    for (int i = 0; i < m; i++){
        if (S[i] == '1') ans += 1<<i;
    }
    if (ans == 0) ans = n;

    cout << ans << endl;
    return 0;

}
