#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cmath>
#include <complex>
#include <deque>
#include <forward_list>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <optional>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string S,T;
    cin >> n >> S >> T;

    int size = 1;
    for (int i = 0; i < n+2; i++)size *= 3;

    vector<int> dist(size, 1e9);

    auto encode = [&](string s){
        int res = 0;
        for (int i = 0; i < n+2; i++){
            res *= 3;
            if (i < s.length()){
                if (s[i] == 'B') res++;
                else if (s[i] == 'W') res += 2;
            }
        }
        return res;
    };

    auto decode = [&](int v){
        string res(n+2, '.');
        for (int i = n+1; i >= 0; i--){
            if (v % 3 == 1) res[i] = 'B';
            else if (v % 3 == 2) res[i] = 'W';
            v /= 3;
        }
        return res;
    };

    auto empty_pos = [&](string s){
        for (int i = 0; i < n+2; i++){
            if (s[i] == '.') return i;
        }
        return -1;
    };

    dist[encode(S)] = 0;
    // bfs
    queue<int> q;
    q.push(encode(S));
    while (!q.empty()){
        int v = q.front(); q.pop();
        
        string s = decode(v);
        
        int p = empty_pos(s);
        if (p == -1) continue;

        for (int i = 0; i < n+1; i++){
            if (i == p) continue;
            if (s[i] == '.' || s[i+1] == '.') continue;
            string t = s;
            t[p] = s[i];
            t[p+1] = s[i+1];
            t[i] = t[i+1] = '.';
            int u = encode(t);
            if (dist[u] > dist[v]+1){
                dist[u] = dist[v]+1;
                q.push(u);
            }
        }
    }
    
    cout << (dist[encode(T)] == 1e9 ? -1 : dist[encode(T)]) << endl;
    
    return 0;

}