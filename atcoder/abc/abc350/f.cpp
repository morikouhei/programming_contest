#include <bits/stdc++.h>
using namespace std;


char flip(char c, int nest){
    if (nest%2 == 0) return c;
    if (isupper(c)) return tolower(c);
    return toupper(c);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    cin >> S;
    int n = S.length();
    vector<int> nest;
    vector<int> pat(n,-1);
    vector<char> ans(n);
    for (int i = 0; i < n; i++){
        char s = S[i];
        ans[i] = s;
        if (s == '('){
            nest.push_back(i);
            continue;
        }
        if (s == ')'){
            int p = nest.back();
            nest.pop_back();
            pat[p] = i;
            pat[i] = p;
            continue;
        }
        ans[i] = flip(s,nest.size());
    }

    auto dfs = [&](auto dfs, int l, int r, int t) -> void{

        if (t == 0){
            for (int i = l; i < r; i++){
                if (ans[i] == '('){
                    dfs(dfs,i+1,pat[i],t^1);
                    i = pat[i];
                } else if (ans[i] == ')'){
                    assert (false);
                } else{
                    cout << ans[i];
                }
            }
        } else{
            for (int i = r-1; i >= l; i--){
                if (ans[i] == ')'){
                    dfs(dfs,pat[i]+1,i,t^1);
                    i = pat[i];
                } else if (ans[i] == '('){
                    assert (false);
                } else{
                    cout << ans[i];
                }
            }

        }
    };

    dfs(dfs,0,n,0);
    cout << endl;
    

    return 0;
}
