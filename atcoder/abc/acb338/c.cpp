#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> Q(n), A(n), B(n);
    for (int i = 0; i < n; i++)
        cin >> Q[i];
    for (int i = 0; i < n; i++)
        cin >> A[i];
    for (int i = 0; i < n; i++)
        cin >> B[i];

    int ans = 0;

    for (int a = 0; a <= 1e6; a++)
    {
        int ok = 1;
        for (int i = 0; i < n; i++)
        {
            if (A[i] * a > Q[i])
                ok = 0;
        }
        if (ok == 0)
            break;

        long long b = 1e7;
        for (int i = 0; i < n; i++)
        {
            if (B[i] == 0)
            {
                continue;
            }
            long long left = Q[i] - A[i] * a;
            b = min(b, left / B[i]);
        }
        ans = max(ans, a + (int)b);
    }
    cout << ans << endl;
    return 0;
}
