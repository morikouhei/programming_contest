#include <bits/stdc++.h>
using namespace std;



int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n,a,x,y;
    cin >> n >> a >> x >> y;

    map<long long, double> dic;

    auto dfs = [&](auto dfs, long long n) -> double {
        if (dic.count(n)){
            return dic[n];
        }
        if (n == 0){
            return 0.0;
        }

        double c1 = x + dfs(dfs,n/a);
        double c2 = y * 6. / 5;
        for (long long i = 2; i <= 6; i++){
            c2 += dfs(dfs,n/i)/5;
        }
        // c2 /= 5;

        dic[n] = min(c1,c2);
        return dic[n];
    };

    double ans = dfs(dfs,n);

    cout << fixed << setprecision(10) << ans << endl;

    

    return 0;
}
