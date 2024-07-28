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

    int n,q;
    cin >> n >> q;
    vector<int> A(n);
    for (auto &a: A) cin >> a;
    sort(A.begin(),A.end());

    auto solve = [&](int b, int k){
        int l = -1, r = 3e8;
        int pos = lower_bound(A.begin(),A.end(),b) - A.begin();
        while (r - l > 1){
            int m = (l+r)/2;
            
            int cnt = 0;
            cnt += lower_bound(A.begin(),A.end(),b) - lower_bound(A.begin(),A.end(),b-m);
            cnt += upper_bound(A.begin(),A.end(),b+m) - lower_bound(A.begin(),A.end(),b);

            if (cnt < k){
                l = m;
            } else {
                r = m;
            }
           
            
        }
        return r;
    };

    for (int t = 0; t < q; t++){
        int b,k;
        cin >> b >> k;
        cout << solve(b,k) << endl;

    }
    
    return 0;

}