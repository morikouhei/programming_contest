#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;

using mint = modint998244353;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n,m;
    cin >> n >> m;
    mint ans = 0;

    for (long long i = 0; i < 60; i++){
        if (!(m >> i & 1)) continue;
        long long mod2 = 2ll << i;
        long long p = n%mod2;
        ans += (n-p)/2;

        if (p >= (1ll<<i)){
            ans += p-(1ll<<i)+1;
        }
    }

    cout << ans.val() << endl;
    
}
