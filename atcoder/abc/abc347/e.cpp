#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,q;
    cin >> n >> q;

    vector<int> X(q);
    for (auto &x: X) cin >> x;

    vector<long long> ans(n);
    vector<int> contain(n);
    vector<int> last(n);
    vector<long long> accum = {0};

    long long size = 0;
    for (int i = 0; i < q; i++){
        int x = X[i];
        x--;
        if (contain[x]){
            size -= 1;
            ans[x] += accum.back() - accum[last[x]-1];
        } else{
            size += 1;
        }
        contain[x] ^= 1;
        long long num = accum.back() + size;
        accum.push_back(num);
        last[x] = i+1;
    }

    for (int i = 0; i < n; i++){
        if (contain[i]){
            ans[i] += accum.back() - accum[last[i]-1];
        }
    }

    for (auto a: ans) cout << a << " ";
    cout << endl;





    return 0;
}
