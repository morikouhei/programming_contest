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
    long long m;
    cin >> n >> m;
    vector<long long> A(n);
    for (auto& a: A) cin >> a;

    if (m == 1){
        int count = 0;
        for (auto a: A){
            if (a == 1) count++;
        }

        cout << mint(2).pow(count).val()-1 << endl;
        return 0;
    }

    vector<pair<long long, int>> factors;
    long long nm = m;

    for (long long i = 2; i*i <= nm; i++){
        if (nm%i) continue;
        int num = 0;
        while (nm%i == 0){
            nm /= i;
            num++;
        }
        factors.push_back({i,num});
    }
    if (nm != 1) factors.push_back({nm,1});
    int le = factors.size();

    vector<int> nums(1<<le);

    for (auto a: A){
        if (m%a) continue;
        int pos = 0;

        for (auto& [fac,num] : factors){
            int count = 0;
            pos <<= 1;
            while (a%fac == 0){
                a /= fac;
                count++;
            }
            if (num == count) pos |= 1;
        }
        nums[pos]++;
    }
    
    vector<vector<mint>> dp((1<<le)+1,vector<mint>(1<<le,mint(0)));
    vector<mint> pow2(n+1);
    for (int i = 0; i <= n; i++){
        pow2[i] = mint(2).pow(i);
    }
    dp[0][0] = 1;

    for (int i = 0; i < 1<<le; i++){
        mint num = pow2[nums[i]]-1;
        for (int j = 0; j < 1<<le; j++){
            dp[i+1][i|j] += dp[i][j]*num;
            dp[i+1][j] += dp[i][j];
        }
    }
    cout << dp[1<<le][(1<<le)-1].val() << endl;
    

    return 0;
}
