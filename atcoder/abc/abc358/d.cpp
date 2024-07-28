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
    vector<int> A(n),B(m);
    for (auto &a: A) cin >> a;
    for (auto &b: B) cin >> b;

    sort(A.begin(),A.end());
    sort(B.begin(),B.end());
    
    long long ans = 0;
    int now = 0;
    for (auto b: B){
        while (now < n && A[now] < b){
            now++;
        }
        if (now == n){
            cout << -1 << endl;
            return 0;
        }
        ans += A[now];
        now++;
    }

    cout << ans << endl;

    
    return 0;

}