#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> A(n);
    for (auto &a: A) cin >> a;
    vector<int> pos(n);
    vector<pair<int,int>> ans;
    for (int i = 0; i < n; i++){
        A[i]--;
        pos[A[i]] = i;
    }

    for (int i = 0; i < n-1; i++){
        if (pos[i] == i) continue;
        int j = pos[i];
        ans.push_back({min(i,j)+1,max(i,j)+1});
        swap(pos[A[i]],pos[A[j]]);
        swap(A[i],A[j]);
    }

    for (int i = 0; i < n; i++){
        assert (A[i] == i);
    }

    cout << ans.size() << endl;
    for (auto [i,j] : ans){
        cout << i << " " << j << endl;
    }

    return 0;
}
