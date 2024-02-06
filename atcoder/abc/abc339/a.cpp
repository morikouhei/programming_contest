#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int last = -1;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '.')
            last = i;
    }

    string ans = s.substr(last + 1, s.length() - last);

    cout << ans << endl;
}
