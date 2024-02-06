#include <bits/stdc++.h>

using namespace std;

int main() {

    int N;
    cin >> N;

    vector<long long> Repunit;

    for (int i = 1;i < 13;i++){

        long long rep = 0;

        long long ten = 1;
        for (int j = 0;j<i;j++){
            rep += ten;
            ten *= 10;
        }
        Repunit.emplace_back(rep);
    }

    vector<long long> cand;
    for (int i=0;i<12;i++){
        for (int j=0;j<12;j++){
            for (int k=0;k<12;k++){
                long long num = Repunit[i]+Repunit[j]+Repunit[k];
                cand.emplace_back(num);
            }
        }
    }
    sort(cand.begin(),cand.end());

    unique(cand.begin(),cand.end());

    cout << cand[N-1] << endl;

    return 0;
}