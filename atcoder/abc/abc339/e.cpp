
#include <bits/stdc++.h>
using namespace std;
#include <atcoder/segtree>
using namespace atcoder;

int op(int a, int b) { return max(a, b); }

int e() { return 0; }

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d;
    cin >> n >> d;
    vector<int> A(n);
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }

    int M = 5e5 + 5;

    segtree<int, op, e> seg(M);

    for (auto a : A)
    {

        int ma = seg.prod(max(0, a - d), min(M, a + d + 1));
        seg.set(a, ma + 1);
    }

    cout << seg.all_prod() << endl;

    return 0;
}
