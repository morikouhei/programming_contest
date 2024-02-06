
#include <bits/stdc++.h>
using namespace std;
#include <atcoder/fenwicktree>
using namespace atcoder;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> A(n), B(n);
    vector<vector<int>> AB;
    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        if (a < b)
        {
            swap(a, b);
        }
        A[i] = a;
        B[i] = b;
        AB.push_back({b, 1, i});
        AB.push_back({a, -1, i});
    }

    sort(AB.begin(), AB.end());

    fenwick_tree<int> ft(2 * n);

    for (int i = 0; i < 2 * n; i++)
    {
        int pos = AB[i][0];
        int f = AB[i][1];
        int ind = AB[i][2];
        if (f == 1)
        {
            ft.add(pos, 1);
        }
        else
        {
            int l = B[ind];
            if (ft.sum(l + 1, pos))
            {
                cout << "Yes" << endl;
                return 0;
            }
            ft.add(l, -1);
        }
    }

    cout << "No" << endl;
    return 0;
}
