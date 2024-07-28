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
    vector<long long> A(n);
    for (auto &a : A) cin >> a;
    long long ans = 0;
    for (auto a : A) ans += a;

    vector<long long> deg(n,2);

    // 最小値を取り出すためのpriority_queue
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> h;
    for (int i = 0; i < n; i++) {
        h.emplace(A[i] * (2*deg[i]-1),i);
    }
    for (int i = 0; i < n-2; i++) {
        auto [val,idx] = h.top();
        h.pop();
        ans += val;
        deg[idx]++;
        h.emplace(A[idx]*(2*deg[idx]-1),idx);
    }
    cout << ans << endl;

    return 0;

}