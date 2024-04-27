#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    set<string> ans;
    string S;
    cin >> S;

    int n = S.length();

    for (int i = 0; i < n; i++){
        for (int j = 1; i + j <= n; j++){
            ans.insert(S.substr(i,j));
        }
    }

    cout << ans.size() << endl;

    return 0;
}
