#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    cin >> S;

    vector<vector<int>> pos(26);

    for (int i = 0; i < S.length(); i++){
        int x = S[i] - 'a';
        pos[x].push_back(i+1);
    }

    for (int i = 0; i < 26; i++){
        if (pos[i].size() != 1) continue;
        cout << pos[i][0] << endl;
    }
    return 0;
}
