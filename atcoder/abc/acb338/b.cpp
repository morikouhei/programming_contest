#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    vector<int> freaqs(26);

    for (auto c : s)
    {
        int pos = c - 'a';
        freaqs[pos]++;
    }

    int ma = 0;
    for (auto f : freaqs)
        ma = max(ma, f);

    for (int i = 0; i < 26; i++)
    {
        if (freaqs[i] == ma)
        {
            char ans = 'a' + i;
            cout << ans << endl;
            return 0;
        }
    }
    return 0;
}
