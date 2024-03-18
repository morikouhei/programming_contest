
#include <bits/stdc++.h>
using namespace std;
#include <atcoder/lazysegtree>

using namespace std;
using namespace atcoder;

// using long long long long;

long long op(long long l, long long r) { return l + r; }

long long e() { return 0; }

long long mapping(long long l, long long r) { return l + r; }
long long composition(long long l, long long r) { return l + r; }

long long id() { return 0; }

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<long long> A(n);
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    lazy_segtree<long long, op, e, long long, mapping, composition, id> seg(A);
    vector<int> B(m);
    for (int i = 0; i < m; i++)
    {
        cin >> B[i];
    }
    for (int i = 0; i < m; i++)
    {
        int b = B[i];

        long long x = seg.get(b);
        seg.set(b, 0);
        seg.apply(0, n, x / n);

        int left = x % n;

        if (left == 0)
        {
            continue;
        }

        int add = min(n - 1 - b, left);
        seg.apply(b + 1, b + 1 + add, 1);

        if (add < left)
        {
            seg.apply(0, left - add, 1);
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << seg.get(i) << " ";
    }
    cout << endl;
    return 0;
}
