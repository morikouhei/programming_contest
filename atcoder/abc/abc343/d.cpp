#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,t;
    cin >> n >> t;

    multiset<long long> ms;

    vector<long long> score(n,0);
    for (int i = 0; i < n; i++) ms.insert(0);

    int ans = 1;

    for (int i = 0; i < t; i++){
        int a;
        long long b;
        cin >> a >> b;
        a--;

        auto it = ms.find(score[a]);

        // イテレータがマルチセットの終端でない、つまり要素が見つかった場合、その要素を削除
        if (it != ms.end()) {
            ms.erase(it);
        }

        it = ms.find(score[a]);

        // イテレータがマルチセットの終端でない、つまり要素が見つかった場合、その要素を削除
        if (it == ms.end()) {
            ans--;
        }

        score[a] += b;

        it = ms.find(score[a]);

        // イテレータがマルチセットの終端でない、つまり要素が見つかった場合、その要素を削除
        if (it == ms.end()) {
            ans++;
        }
        ms.insert(score[a]);

        cout << ans << endl;




    }


    return 0;
}
