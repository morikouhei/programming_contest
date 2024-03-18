#include <bits/stdc++.h>
using namespace std;
using ll = long long;

map<ll, ll> memo;

ll dfs(ll x)
{
    if (x <= 1)
    {
        return 0;
    }
    if (memo.count(x))
    {
        return memo[x];
    }

    ll count = x + dfs(x / 2) + dfs((x + 1) / 2);
    memo[x] = count;
    return count;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n;
    cin >> n;
    cout << dfs(n) << endl;
    return 0;
}
