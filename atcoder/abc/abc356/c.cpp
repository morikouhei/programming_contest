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
    vector<tuple<int,int>> AR;
    for (int i = 0; i < m; i++){
        int c;
        cin >> c;
        int a = 0;
        for (int j = 0; j < c; j++){
            int x;
            cin >> x;
            x--;
            a |= 1<<x;
        }
        char r;
        cin >> r;
        AR.emplace_back(a,r=='o');
        
    }

    int ans = 0;

    for (int bi = 0; bi < 1<<n; bi++){
        bool ok = true;
        for (auto [a,r]: AR){
            int judge = __builtin_popcount(a&bi) >= k;
            if (judge != r) ok = false;
        }
        if (ok) ans++;
    }

    cout << ans << endl;

    return 0;
}
