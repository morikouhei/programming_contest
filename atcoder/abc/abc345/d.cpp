#include <bits/stdc++.h>
using namespace std;

int n,h,w;

pair<int,int> fill(vector<vector<int>>&s, int a, int b){

    for (int x = 0; x < h; x++){
        for (int y = 0; y < w; y++){
            if (s[x][y]) continue;
            return {x,y};
        }
    }

    return {-1,-1};

}
bool check(vector<int>& permutation, int bi, vector<int>&A, vector<int>&B){
    vector<vector<int>> s(h,vector<int>(w,0));
    for (int i = 0; i < n; i++){
        int a = A[permutation[i]],b = B[permutation[i]];
        if (bi >> i & 1) swap(a,b);
        auto [x,y] = fill(s,a,b);

        if (x == -1) return true;
        if (x+a > h || y+b > w) return false;
        for (int nx = 0; nx < a; nx++){
            for (int ny = 0; ny < b; ny++){
                if (s[x+nx][y+ny] == 1) return false;
                s[x+nx][y+ny] = 1;
            }
        }

    }

    for (int x = 0; x < h; x++){
        for (int y = 0; y < w; y++){
            if (s[x][y] == 0) return false;
        }
    }

    return true;

}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> h >> w;
    vector<int> A(n),B(n);
    for (int i = 0; i < n; i++){
        cin >> A[i] >> B[i];
    }

    vector<int> permutation(n);
    for (int i = 0; i < n; i++){
        permutation[i] = i;
    }

    do {
        for (int bi = 0; bi < 1<<n; bi++){
            if (check(permutation,bi,A,B)){
                cout << "Yes" << endl;
                return 0;
            }
        }

    } while (next_permutation(permutation.begin(),permutation.end()));

    cout << "No" << endl;
    return 0;
}
