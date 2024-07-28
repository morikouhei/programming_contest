#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<mint> A(n);
    queue<vector<mint>> fps;
    mint s = 0;
    for (int i = 0; i < n; i++){
        int a;
        cin >> a;
        s += a;
        fps.push({1,a});
    }

    while (fps.size() > 1){
        auto a = fps.front(); fps.pop();
        auto b = fps.front(); fps.pop();
        fps.push(convolution(a,b));
    }

    vector<mint> dp = fps.front();
    mint ans = 0;
    mint po = 1;
    for (int i = 0; i < n+1; i++){
        ans += dp[i] * po;
        po *= i+1;
        po /= s-i;
    }
    cout << ans.val() << endl;

    return 0;
}
