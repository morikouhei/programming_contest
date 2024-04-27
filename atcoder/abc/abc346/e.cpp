#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long h,w;
    int m;
    cin >> h >> w >> m;
    long long area = h * w;
    vector<long long> T(m),A(m),X(m);

    for (int i = 0; i < m; i++){
        cin >> T[i] >> A[i] >> X[i];
    }

    vector<long long> ans(200005);
    vector<int> cols(h),rows(w);

    for (int i = m-1; i >= 0; i--){
        long long t = T[i];
        long long a = --A[i];
        long long x = X[i];

        if (t == 1){
            if (cols[a] == 1) continue;
            cols[a] = 1;
            ans[x] += w;
            h--;
        }
        if (t == 2){
            if (rows[a] == 1) continue;
            rows[a] = 1;
            ans[x] += h;
            w--;
        }
    }
    ans[0] += h * w;

    int size = 0;
    int ma = 2e5;
    for (int i = 0; i <= ma; i++){
        
        if (ans[i] > 0){
            size++;
        }
    }
    cout << size << endl;
    for (int i = 0; i <= ma; i++){
        if (ans[i] > 0){
            cout << i << " " << ans[i] << "\n";
        }
    }
    return 0;
}
