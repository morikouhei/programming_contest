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

    string s,t;
    cin >> s >> t;
    for (int w = 1; w < s.size(); w++){
        
        for (int c = 1;c <= w; c++){
            string u = "";
            for (int i = 0; i < s.size(); i++){
                if (i % w == c-1){
                    u += s[i];
                }
            }
            if (u == t){
                cout << "Yes" << endl;
                return 0;
            }
        }
    }
    
    cout << "No" << endl;
    
    return 0;

}