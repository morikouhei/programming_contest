#include <bits/stdc++.h>
using namespace std;
int main()

{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> A;
    int q;
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        int t, x;
        cin >> t >> x;
        if (t == 1)
        {
            A.push_back(x);
        }
        else
        {

            cout << A[A.size() - x] << endl;
        }
    }
    return 0;
}
