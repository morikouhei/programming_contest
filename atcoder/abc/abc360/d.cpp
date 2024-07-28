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
    long long t;
    cin >> n >> t;
    string s;
    cin >> s;
    vector<long long> X(n);
    for (auto &x : X) cin >> x;
    
    vector<long long> L,R;
    for (int i = 0; i < n; i++){
        if (s[i] == '0') L.push_back(X[i]);
        else R.push_back(X[i]);
    }
    sort(L.begin(), L.end());
    sort(R.begin(), R.end());

    long long ans = 0;
    for (auto r: R){
        long long count = upper_bound(L.begin(), L.end(), r+2*t) - lower_bound(L.begin(), L.end(), r);
        ans += count;
    }
    cout << ans << endl;


}