#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> A(n);
    for (auto &a: A) cin >> a;

    vector<long long> lis;

    for (auto a : A){

        while (!lis.empty() && lis.back() == a){
            lis.pop_back();
            a++;
        }
        lis.push_back(a);
    }

    cout << lis.size() << endl;

    return 0;
}
