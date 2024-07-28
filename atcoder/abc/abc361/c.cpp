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

    int n,k;
    cin >> n >> k;
    k = n-k;
    vector<int> A(n);
    for (auto &a : A) cin >> a;
    sort(A.begin(),A.end());

    int ans = 1e9;
    for (int i = 0; i < n-k+1; i++){
        ans = min(ans,A[i+k-1]-A[i]);
    }
    cout << ans << endl;
    
    
    return 0;

}