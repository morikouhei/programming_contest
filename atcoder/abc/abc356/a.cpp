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

    int n,l,r;
    cin >> n >> l >> r;
    vector<int> ans(n);
    for (int i = 0 ; i < n; i++){
        ans[i] = i+1;
    }
    reverse(ans.begin()+l-1,ans.begin()+r);
    for (auto a: ans){
        cout << a << " ";
    }
    cout << endl;

    return 0;
}
