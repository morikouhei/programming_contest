#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> X(m);
    for (int i = 0; i < m; i++)
    {
        cin >> X[i];
        X[i]--;
    }

    vector<long long> imos(n + 1);

    long long ans = 0;
    for (int i = 0; i < m - 1; i++)
    {

        auto [l, r] = minmax(X[i], X[i + 1]);

        int d1 = r - l;
        int d2 = n + l - r;
        ans += min(d1, d2);

        if (d1 == d2)
        {
            continue;
        }

        if (d1 < d2)
        {
            int dif = d2 - d1;

            imos[l] += dif;
            imos[r] -= dif;
        }
        else
        {
            int dif = d1 - d2;

            imos[r] += dif;
            imos[0] += dif;
            imos[l] -= dif;
        }
    }
    long long mi = 1e18;

    for (int i = 0; i < n; i++)
    {
        mi = min(mi, imos[i]);
        imos[i + 1] += imos[i];
    }

    cout << ans + mi << endl;

    return 0;
}
