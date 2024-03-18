#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    string S;
    cin >> S;

    vector<vector<int>> pos(26);
    for (int i = 0; i < 26; i++){
        pos[i].push_back(i);
    }
    int q;
    cin >> q;
    for (int i = 0; i < q; i++){
        char c,d;
        cin >> c >> d;
        int cind = c - 'a';
        int dind = d - 'a';
        if (cind == dind) continue;

        while (!pos[cind].empty()){
            int x = pos[cind].back();
            pos[cind].pop_back();
            pos[dind].push_back(x);
        }
    }

    vector<int> aft(26);

    for (int i = 0; i < 26; i++){
        for (auto ind: pos[i]){
            aft[ind] = i;
        }
    }

    for (auto s: S){
        int ind = s - 'a';

        char ns = 'a' + aft[ind];
        cout << ns;
    }
    cout << endl;


    return 0;
}
