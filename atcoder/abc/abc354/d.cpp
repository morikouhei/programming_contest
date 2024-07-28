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


long long calc(long long x, long long y){
    vector<int> x1 = {0,2,3,3,4};
    vector<int> x2 = {0,3,6,7,8};
    vector<vector<int>> area(3,vector<int>(5));
    area[1] = x1;
    area[2] = x2;

    long long ans = (x/4) * (y/2) * area[2][4];
    ans += (y/2) * area[2][x%4];
    ans += (x/4) * area[y%2][4];
    ans += area[y%2][x%4];

    return ans;

    
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long long a,b,c,d;
    cin >> a >> b >> c >> d;
    long long inf = 1e9;
    a += inf;
    b += inf;
    c += inf;
    d += inf;

    long long ans = calc(c,d) + calc(a,b) - calc(c,b) - calc(a,d);
    cout << ans << endl; 

    return 0;
}