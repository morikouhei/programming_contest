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

    vector<tuple<int,int,int>> AC(n);
    for (int i = 0; i < n; i++){
        int a,c;
        cin >> a >> c;
        AC[i] = {-a,c,i};
    }
    vector<int> ans;

    sort(AC.begin(),AC.end());
    int last = 1e9+5;

    for (auto [a,c,ind]: AC){
        if (last < c) continue;
        last = c;
        ans.push_back(ind);
    }
    sort(ans.begin(),ans.end());

    cout << ans.size() << endl;
    for (auto a: ans){
        cout << a+1 << " ";
    }
    cout << endl;

    
    return 0;

}