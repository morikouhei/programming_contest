#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long a,b;
    cin >> n >> a >> b;
    long long le = a + b;
    vector<long long> cand;
    for (int i = 0; i < n; i++){
        long long d;
        cin >> d;

        cand.push_back(d%le);
        cand.push_back(d%le+le);

    }
    sort(cand.begin(),cand.end());
    cout << endl;
    int r = 0;

    for (int l = 0; l < n; l++){
        while (r < 2 * n && cand[r]-cand[l] < a) r++;
        if (r - l >= n){
            cout << "Yes" << endl;
            exit(0);
        } 
    }

    cout << "No" << endl; 

    return 0;
}
