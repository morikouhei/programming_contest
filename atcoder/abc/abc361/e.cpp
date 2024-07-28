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
    long long ans = 0;
    cin >> n;
    vector<vector<pair<int,long long>>> edge(n);
    for (int i = 0; i < n-1; i++){
        int a,b;
        long long c;
        cin >> a >> b >> c;
        a--; b--;
        ans += c*2;

        edge[a].push_back({b,c});
        edge[b].push_back({a,c});
    }

    // 木の直径を求める
    auto bfs = [&](int start){
        vector<long long> dist(n,-1);
        queue<int> q;
        q.push(start);
        dist[start] = 0;
        int max_idx = start;
        long long max_dist = 0;
        while (!q.empty()){
            int now = q.front();
            q.pop();
            for (auto [next, cost]: edge[now]){
                if (dist[next] != -1) continue;
                dist[next] = dist[now] + cost;
                if (max_dist < dist[next]){
                    max_dist = dist[next];
                    max_idx = next;
                }
                q.push(next);
            }
        }
        return make_pair(max_idx, max_dist);
    };

    auto [idx1, _] = bfs(0);
    auto [idx2, dist] = bfs(idx1);

    ans -= dist;

    cout << ans << endl;

    return 0;

}