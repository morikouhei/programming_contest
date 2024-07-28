#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;

using mint = modint998244353;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    cin >> k;
    vector<int> C(26);
    for (int i = 0; i < 26; i++){
        cin >> C[i];
    }

    // nCr を mint で求めるために factorial と inverse factorial を用意
    vector<mint> fact(1005);
    vector<mint> invfact(1005);
    fact[0] = 1;
    for (int i = 1; i < 1005; i++){
        fact[i] = fact[i-1] * i;
    }
    invfact[1004] = fact[1004].inv();
    for (int i = 1004; i > 0; i--){
        invfact[i-1] = invfact[i] * i;
    }

    // nCr を求める関数
    auto nCr = [&](int n, int r){
        return fact[n] * invfact[r] * invfact[n-r];
    };

    // dp[i][j] := i 文字目まで見て、j 個の文字を使っているときの場合の数
    vector<vector<mint>> dp(27, vector<mint>(k+1));
    dp[0][0] = 1;
    for (int i = 0; i < 26; i++){
        for (int j = 0; j <= k; j++){
            for (int l = 0; l <= C[i] && j+l <= k; l++){
                // j 個の文字を使っているときに、l 個の文字を挿入する場合の数 nPr みたいになる
                dp[i+1][j+l] += dp[i][j] * nCr(j+l, l);
            }
        }
    }
    mint ans = 0;
    for (int i = 1; i <= k; i++){
        ans += dp[26][i];
    }
    cout << ans.val() << endl;

    
    
}
