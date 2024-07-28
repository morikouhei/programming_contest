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
    vector<long long> ans(n);
    vector<long long> L(n),R(n);
    long long sum = 0;
    for (int i = 0; i < n; i++){
        cin >> L[i] >> R[i];
        sum += L[i];
        ans[i] = L[i];
    }

    for (int i = 0; i < n; i++){
        if (sum >= 0) break;

        long long dif = min(R[i] - L[i], -sum);
        ans[i] += dif;
        sum += dif;
    }
    if (sum != 0){
        cout << "No" << endl;
    } else{
        cout << "Yes" << endl;
        for (int i = 0; i < n; i++){
            cout << ans[i] << " ";
        }
        cout << endl;
    }

    
    
    return 0;

}