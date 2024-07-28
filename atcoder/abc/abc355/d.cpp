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
    vector<pair<int,int>> event;
    for (int i = 0; i < n; i++){
        int l,r;
        cin >> l >> r;
        event.emplace_back(l,1);
        event.emplace_back(r+1,-1);
    }
    sort(event.begin(),event.end());
    long long ans = 0;
    int count = 0;
    for (auto [x,p] : event){
        if (p == 1)ans += count;
        count += p;
    }
    cout << ans << endl;
    return 0;

}