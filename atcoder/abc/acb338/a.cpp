#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int ok = 1;

    for (int i = 0; i < s.size(); i++)
    {
        char c = s[i];
        if (i == 0)
        {
            if (islower(c))
                ok = 0;
        }
        else
        {
            if (isupper(c))
                ok = 0;
        }
    }
    cout << (ok ? "Yes" : "No") << endl;

    return 0;
}
