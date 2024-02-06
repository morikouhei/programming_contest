#include<bits/stdc++.h>
#include<atcoder/modint>
using namespace std;
using mint=atcoder::modint998244353;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N;
	cin>>N;

    vector<mint> dp(1,1);

    mint inv2 = mint(2).inv();

    vector<mint> pinv2(N+1,1);
    for (int i = 0;i<N;i++){
        pinv2[i+1] = pinv2[i] * inv2;

    }

    for (int k = 2;k<=N;k++){

        vector<mint> ndp(k);

        mint base = (mint(2)-pinv2[k-1]).inv();

        for (int i = 0;i<k-1;i++){
            ndp[0] += dp[i]*pinv2[k-1-i];
        }
        for (int i = 1;i<k;i++){
            mint count = ndp[i-1];
            count -= pinv2[k-1]*dp[i-1];
            count *= inv2;
            count += dp[i-1];
            ndp[i] = count;
        }

        for (int i = 0;i<k;i++){
            ndp[i] *= base;
        }

        swap(dp,ndp);
    }

    for (int i = 0;i<N;i++){
        cout << dp[i].val() << " ";

    }
    cout << endl;

    return 0;
}
