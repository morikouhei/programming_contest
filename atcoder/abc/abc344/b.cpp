#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> A;
    while (true){
        int a;
        cin >> a;
        A.push_back(a);
        if (a == 0){
            break;
        }
    }

    reverse(A.begin(),A.end());

    for (auto a: A){
        cout << a << endl;
    }
    return 0;
}
