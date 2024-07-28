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

    int a,b;
    cin >> a >> b;
    set<int> s;
    s.insert(a);
    s.insert(b);

    if (s.size() != 2){
        cout << -1 << endl;
    } else{
        for (int i = 1; i <= 3; i++){
            if (s.count(i) == 0){
                cout << i << endl;
            }
        }
    }
    
    return 0;

}