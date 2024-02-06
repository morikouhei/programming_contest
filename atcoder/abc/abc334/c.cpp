#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int n,k;
    cin >> n >> k;
    vector<int> A(k);
    for (int i = 0;i<k;i++) cin >> A[i];
    const int INF = 100100100;
    vector<vector<int>> dp(2,vector<int>(2,INF));
    dp[0][0] = 0;
    // i skipしたか j 次が0 or 1 番目
    for (auto a: A){
        vector<vector<int>> ndp(2,vector<int>(2,INF));

        for (int i = 0;i < 2;i++){
            for (int j = 0;j < 2;j++){
                if (i == 0){
                    ndp[i+1][j] = min(ndp[i+1][j],dp[i][j]);
                }

                if (j == 0){
                    ndp[i][j+1] = min(ndp[i][j+1],dp[i][j]-a);
                }
                else{
                    ndp[i][j-1] = min(ndp[i][j-1],dp[i][j]+a);
                }
            }
        }
        swap(dp,ndp);
    }

    cout << dp[k%2][0] << endl;
}
