#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<long long> A(9);
    for (auto& a: A) cin >> a;

    vector<string> winner = {"Takahashi","Aoki"};

    vector<long long> points(1<<9);
    for (int i = 0; i < 1<<9; i++){
        for (int j = 0; j < 9; j++){
            if (i >> j & 1) points[i] += A[j];
        }
    }
    vector<int> bingo;
    for (int i = 0; i < 3; i++){
        int num = 0;
        for (int j = 0; j < 3; j++){
            num += 1<<(i+3*j);
        }
        bingo.push_back(num);

        num = 0;
        for (int j = 0; j < 3; j++){
            num += 1<<(j+3*i);
        }
        bingo.push_back(num);

    }

    bingo.push_back((1<<0) + (1<<4) + (1<<8));
    bingo.push_back((1<<2) + (1<<4) + (1<<6));

    auto bingo_check = [&](int num){
        for (auto b: bingo){
            if ((b & num) == b) return true; 
        }
        return false;
    };

    auto dfs = [&](auto dfs, int turn, int tak, int aok) -> int {

        if (bingo_check(tak)) return 0;
        if (bingo_check(aok)) return 1;
        
        if (turn == 9){
            return (points[tak] > points[aok] ? 0 : 1);
        }

        for (int i = 0; i < 9; i++){
            if (tak >> i & 1 || aok >> i & 1) continue;
            if (turn%2 == 0){
                if (dfs(dfs,turn+1,tak|1<<i,aok) == 0) return 0; 
            } else{
                if (dfs(dfs,turn+1,tak,aok|1<<i) == 1) return 1; 
            }
        }
            
        return (turn&1)^1;
    };
    if (dfs(dfs,0,0,0) == 0){
        cout << winner[0] << endl;
    } else{
        cout << winner[1] << endl;
    }


    return 0;
}
