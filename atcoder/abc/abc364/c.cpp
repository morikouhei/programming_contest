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
    long long x,y;
    cin >> n >> x >> y;
    vector<long long> A(n),B(n);
    for (auto &a: A) cin >> a;
    for (auto &b: B) cin >> b;
    sort(A.rbegin(),A.rend());
    sort(B.rbegin(),B.rend());
    int ans = n;
    
    long long cum = 0;
    for (int i = 0; i < n; i++){
        cum += A[i];
        if (cum > x){
            ans = i+1;
            break;
        }
    }
    cum = 0;
    for (int i = 0; i < n; i++){
        cum += B[i];
        if (cum > y){
            ans = min(ans,i+1);
            break;
        }
    }
    cout << ans << endl;
    
    return 0;

}