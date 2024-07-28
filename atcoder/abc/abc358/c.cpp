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
    vector<int> S(n);
    for (int i = 0; i < n; i++){
        int s = 0;
        for (int j = 0; j < m; j++){
            char a;
            cin >> a;
            s += (a == 'o') * 1 << (j);
        }
        S[i] = s;
    }
    vector<int> dp(1<<m, 1e9);
    dp[0] = 0;
    for (auto s: S){
        for (int i = 0; i < 1<<m; i++){
            dp[i|s] = min(dp[i|s], dp[i]+1);
        }
    }
    cout << dp[(1<<m)-1] << endl;

    
    return 0;

}