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
    int M = 2e6+5;
    vector<int> count(M);
    for (int i = 0; i < n; i++){
        int a;
        cin >> a;
        count[a]++;
    }
    for (int i = 0; i < M-1; i++){
        count[i+1] += count[i];
    }
    long long ans = 0;

    for (int i = 1; i <= 1e6; i++){
        long long num = count[i]-count[i-1];

        if (num == 0) continue;

        ans -= num * (num+1)/2;

        for (int j = 2*i; j < M; j+= i){
            long long nex = count[j-1] - count[j-i-1];
            ans += nex * num * ((j-1)/i);

        }

    }
    cout << ans << endl;

    return 0;
}
