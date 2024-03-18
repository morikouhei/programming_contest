#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,q;
    cin >> n >> q;
    string S;
    cin >> S;

    set<int> s;


    vector<int> status(n-1,0);
    for (int i = 0; i < n-1; i++){
        if (S[i] == S[i+1]){
            s.insert(i);
            status[i] = 1;
        }
    }

    auto push = [&](int ind){
        if (ind < 0 || ind >= n-1) return;
        if (status[ind]){
            s.erase(ind);
        } else{
            s.insert(ind);
        }

        status[ind] ^= 1;
    };


    for (int i = 0; i < q; i++){
        int t,l,r;
        cin >> t >> l >> r;
        l--;
        if (t == 1) {
            push(l-1);
            push(r-1);
        }

        if (t == 2) {
            auto it = s.lower_bound(l);
            if (it == s.end() || *it >= r-1){
                cout << "Yes" << endl;
            } else{
                cout << "No" << endl;
            }
        }

    }

    
    return 0;
}
