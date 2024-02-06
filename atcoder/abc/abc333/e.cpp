#include <bits/stdc++.h>

using namespace std;

int main() {

    int N;
    cin >> N;

    vector<vector<int>> potion(N);

    vector<int> ans(N);

    vector<int> T(N),X(N);
    

    for (int i = 0;i < N ; i++){
        cin >> T[i] >> X[i];
        X[i]--;
    }

    int count = 0;
    for (int i = 0; i < N;i++){

        int t = T[i];
        int x = X[i];

        if (t == 1){
            potion[x].push_back(i);
        }
        else {
            if (potion[x].size() == 0){
                cout << -1 << endl;
                return 0;
            } else{
                int p = potion[x][potion[x].size()-1];
                potion[x].pop_back();
                ans[p] = 1;
            }
        }
    }
    int ma = 0;
    for (int i = 0;i < N;i++){
        count += ans[i];
        if (T[i] == 2) count--;
        ma = max(ma,count);
    }

    cout << ma << endl;

    for (int i = 0;i < N;i++){
        if (T[i] == 2) continue;
        cout << ans[i]  << ' ';

    }
    cout << endl;




    return 0;
}