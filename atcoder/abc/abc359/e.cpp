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
    vector<long long> H(n);
    for (auto &h : H) cin >> h;

    vector<pair<long long,int>> q;
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        int w = 1;
        while (!q.empty() && q.back().first <= H[i]) {
            ans -= q.back().first * q.back().second;
            w += q.back().second;
            q.pop_back();
        }
        ans += H[i] * w;
        q.emplace_back(H[i],w);
        cout << ans+1 << endl;
    }

    return 0;

}