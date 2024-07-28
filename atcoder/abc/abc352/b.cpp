#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    string T;
    cin >> S >> T;

    int now = 0;
    for (auto s: S){
        while (now < T.length() && s != T[now]){
            now++;
        }
        now++;
        cout << now << " ";
    }
    cout << endl;

    return 0;
}
