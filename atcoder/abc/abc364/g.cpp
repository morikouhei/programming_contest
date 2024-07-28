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

    int n,m,k;
    cin >> n >> m >> k;
    vector<vector<pair<int,long long>>> e(n);
    for(int i = 0; i < m; i++)
    {
        int u,v;
        long long w;
        cin >> u >> v >> w;
        u--,v--;
        e[u].push_back({v,w});
        e[v].push_back({u,w});
    }
    k--;
    vector<vector<long long>> dp(1<<k,vector<long long>(n,1e18));
    for (int i = 0; i < k; i++)
    {
        dp[1<<i][i] = 0;
    }

    for (int bi = 1; bi < (1<<k); bi++)
    {
        for (int s = bi; s > 0; s = (s-1)&bi)
        {
            for (int i = 0; i < n; i++){
                dp[bi][i] = min(dp[bi][i],dp[s][i]+dp[bi^s][i]);
            }
        }
        priority_queue<pair<long long,int>,vector<pair<long long,int>>,greater<pair<long long,int>>> h;
        for (int i = 0; i < n; i++)
        {
            h.push({dp[bi][i],i});
        }
        while(!h.empty())
        {
            auto [d,u] = h.top();
            h.pop();
            if(d != dp[bi][u]) continue;
            for(auto [v,w]:e[u])
            {
                if(dp[bi][v] > dp[bi][u]+w)
                {
                    dp[bi][v] = dp[bi][u]+w;
                    h.push({dp[bi][v],v});
                }
            }
        }
    }
    for (int i = k; i < n; i++)
    {
        cout << dp[(1<<k)-1][i] << '\n';
    }

    
    
    return 0;

}