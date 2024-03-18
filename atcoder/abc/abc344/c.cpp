#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    map<int,int> count;
    vector<vector<int>> ABC(3);
    for (int i = 0; i < 3; i++){
        int x;
        cin >> x;
        for (int j = 0; j < x; j++){
            int num;
            cin >> num;
            ABC[i].push_back(num);
        }
    }

    for (int n = 0; n < ABC[0].size(); n++){
        for (int m = 0; m < ABC[1].size(); m++){
            for (int l = 0; l < ABC[2].size(); l++){
                count[ABC[0][n]+ABC[1][m]+ABC[2][l]]++;
            }
        }
    }

    int q;
    cin >> q;
    for (int i = 0; i < q; i++){
        int x;
        cin >> x;
        if (count[x] > 0){
            cout << "Yes" << endl;
        } else{
            cout << "No" << endl;
        }
    }
    return 0;
}
