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

   int n,m;
    cin >> n >> m;
    vector<long long> A(n);
    for (auto &a : A) cin >> a;
    vector<vector<pair<int,long long>>> e(n);

    for (int i = 0; i < m; i++){
        int u,v;
        long long b;
        cin >> u >> v >> b;
        u--; v--;
        e[u].push_back({v,b+A[v]});
        e[v].push_back({u,b+A[u]});
    }
    long long inf = 1LL << 60;
    vector<long long> dp(n, inf);
    dp[0] = A[0];
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({A[0], 0});
    while (!pq.empty()){
        auto [d, now] = pq.top();
        pq.pop();
        if (dp[now] != d) continue;
        for (auto [next, cost] : e[now]){
            if (dp[next] > dp[now] + cost){
                dp[next] = dp[now] + cost;
                pq.push({dp[next], next});
            }
        }
    }
    for (int i = 1; i < n; i++){
        cout << dp[i] << endl;
    }
    
    
    return 0;

}