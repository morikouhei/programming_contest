#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<string> A(n),B(n);
    for (auto &a: A) cin >> a;
    for (auto &b: B) cin >> b;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (A[i][j] != B[i][j]){
                cout << i+1 << " " << j+1 << endl;
            }
        }
    } 

    return 0;
}
