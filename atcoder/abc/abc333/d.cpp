#include <bits/stdc++.h>

using namespace std;
const int INF = 100100100;
int N;
int dfs(const vector<vector<int>> &e, int v, int p=-1){

    int ma = 0;
    int count = 1;
    for (int nex : e[v]){
        if (nex == p) continue;
        int num = dfs(e,nex,v);
        count += num;
        ma = max(ma,num+1);
    }

    if (v != 0) return count;

    cout << N - ma + 1<< endl;

    return count;
}
int main() {

    cin >> N;

    vector<vector<int>> e(N);
    for (int i=0;i<N-1;i++){
        int u,v;
        cin >> u >> v;
        u--;v--;
        e[u].push_back(v);
        e[v].push_back(u);


    }

    dfs(e,0);

    return 0;
}