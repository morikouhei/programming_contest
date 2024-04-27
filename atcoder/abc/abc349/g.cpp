#include <bits/stdc++.h>
using namespace std;

#include <atcoder/all>
using namespace atcoder;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> A(n);
    for (auto &a: A) cin >> a;

    dsu uf(n);


    auto merge = [&](int i, int j){
        uf.union(i,j);
    };
    vector<pair<int,int>> edges;

    auto diff = [&](int i, int j){
        edges.push_back({i,j});
    };

    auto end = [](){
        cout << "No" << endl;
        exit(0);
    };


    int i = 0, j = 0;

    while (i < n){
        while (i - j >= 0 && i + j < n && j < A[i]){
            merge(i-j,i+j);
            j++;
        }
        if (j != A[i]) end();

        diff(i-j,i+j);

        int k = 1;
        while (i - k >= 0 && k + ans[i-k] < j){
            if (A[i-k] != A[i+k]) end();
            k++;
        }

        i += k;
        j -= k;

    }

    vector<vector<int>> e(n);

    for (auto [i,j]: edges){
        i = uf.leader(i);
        j = uf.leader(j);
        if (uf.same(i,j)) end();
        e[i].push_back(j);
        e[j].push_back(i);
    }

    cout << "Yes" << endl;

    vector<int> ans(n,-1);

    for (int i = 0; i < n; i++){
        if (uf.leader(i) != i) continue;

        set<int> s;
        for (int ni : e[i]){
            s.insert(ni);
        }

        ans[i] = 1;
        while (s.count(ans[i]))ans[i]++;
    }

    for (int i = 0; i < n; i++){
        cout << ans[uf.leader(i)] << " ";
    }
    cout << endl;
    return 0;
}
