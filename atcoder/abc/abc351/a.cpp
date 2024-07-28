#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> A(9),B(8);
    for (auto &a: A) cin >> a;
    for (auto &b: B) cin >> b;
    int num = 0;
    for (auto a : A) num -= a;
    for (auto b: B) num += b;
    cout << max(-num+1,0) << endl;

    return 0;
}
