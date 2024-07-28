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
    cin >> n;
    vector<vector<int>> e(n);
    for (int i = 0; i < n-1; i++){
        int u,v;
        cin >> u >> v;
        u--; v--;
        e[u].push_back(v);
        e[v].push_back(u);
    }

    // 木の重心を求める
    vector<int> subtree_size(n);
    auto dfs = [&](auto dfs,int now, int pre) -> void{
        subtree_size[now] = 1;
        for (auto next : e[now]){
            if (next == pre) continue;
            dfs(dfs,next, now);
            subtree_size[now] += subtree_size[next];
        }
    };
    dfs(dfs,0, -1);

    int centroid = 0;
    int min_size = n;
    auto search_centroid = [&](auto search_centroid ,int now, int pre) -> void{
        int max_size = n - subtree_size[now];
        for (auto next : e[now]){
            if (next == pre) continue;
            max_size = max(max_size, subtree_size[next]);
            search_centroid(search_centroid,next, now);
        }
        if (max_size < min_size){
            min_size = max_size;
            centroid = now;
        }
    };

    search_centroid(search_centroid,0, -1);

    // 重心からトポロジカル順序の頂点列を求める
    vector<int> order;
    vector<bool> used(n);
    auto dfs2 = [&](auto dfs2, int now) -> void{
        order.push_back(now);
        used[now] = true;
        for (auto next : e[now]){
            if (used[next]) continue;
            dfs2(dfs2,next);
        }
    };
    dfs2(dfs2,centroid);
    order.push_back(centroid);
    for (int i = 1; i <= n/2; i++){
        cout << order[i]+1 << " " << order[i+n/2]+1 << endl;
    }

    
    
    return 0;

}