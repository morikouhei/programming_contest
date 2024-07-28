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
    
    int n,t,p;
    cin >> n >> t >> p;
    vector<int> L(n);
    for (auto &l : L) cin >> l;

    for (int i = 0; i < 200; i++){
        int count = 0;
        for (int j = 0; j < n; j++){
            if (L[j] >= t) count++;
        }
        if (count >= p){
            cout << i << endl;
            return 0;
        }
        for (int j = 0; j < n; j++){
            L[j] += 1;
        }
    }
    
    
    return 0;

}