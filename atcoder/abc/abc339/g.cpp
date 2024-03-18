#include <bits/stdc++.h>
using namespace std;

struct MergeSortTree
{
    int n;
    vector<vector<int>> A;
    vector<vector<long long>> sums;

    MergeSortTree(int mx)
    {
        n = 1;
        while (n < mx)
        {
            n <<= 1;
        }
        A.resize(n * 2);
        sums.resize(n * 2, vector<long long>(1));
    }

    void set(int i, int a)
    {
        A[n + i] = {a};
        sums[n + i].push_back(a);
    }

    void init()
    {
        for (int i = n - 1; i >= 1; i--)
        {

            int l = i << 1, r = l | 1;

            for (auto a : A[l])
            {
                A[i].push_back(a);
            }
            for (auto a : A[r])
            {
                A[i].push_back(a);
            }

            sort(A[i].begin(), A[i].end());

            for (auto a : A[i])
            {
                sums[i].push_back(sums[i].back() + a);
            }
        }
    }

    long long get(int i, int x)
    {
        int r = upper_bound(A[i].begin(), A[i].end(), x) - A[i].begin();
        return sums[i][r];
    }

    long long query(int l, int r, int x)
    {
        l += n, r += n;
        long long ans = 0;
        while (l < r)
        {
            if (l & 1)
            {
                ans += get(l, x);
                l++;
            }
            if (r & 1)
            {
                r--;
                ans += get(r, x);
            }
            l >>= 1, r >>= 1;
        }

        return ans;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    MergeSortTree mstree(n);

    for (int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        mstree.set(i, a);
    }
    mstree.init();

    long long ans = 0;

    int q;
    cin >> q;

    for (int i = 0; i < q; i++)
    {
        long long l, r, x;
        cin >> l >> r >> x;
        l ^= ans;
        r ^= ans;
        x ^= ans;
        l--;
        ans = mstree.query(l, r, x);
        cout << ans << "\n";
    }

    return 0;
}
