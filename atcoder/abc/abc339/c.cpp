#include <bits/stdc++.h>
using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> A(n + 1);

    long long ans = 1e18;
    for (int i = 0; i < n; i++)
    {
        cin >> A[i + 1];
        A[i + 1] += A[i];
        ans = min(ans, A[i + 1]);
    }

    if (ans > 0)
    {
        ans = 0;
    }
    ans = abs(ans) + A[n];
    cout << ans << endl;
    return 0;
}
