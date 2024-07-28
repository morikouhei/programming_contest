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
    
    long long n;
    cin >> n;

    for (int i = 1; i <= 35; i++){

        // i 桁の 回文の数を数える
        long long count = 0;
        int left = i / 2;

        if (i == 1){
            count = 10;
        } else {
             // 1000 - 9999 のように 先頭が 0 でない場合の数
            // 10**(left) - 10**(left-1) が i 桁の回文の数
            long long ten = pow(10, left) - pow(10, left - 1);

            if (i%2){
                ten *= 10;
            }
            count += ten;
        }
        if (count < n){
            n -= count;
            continue;
        }

        

        // i 桁の回文の数の中で n 番目のものを求める
        long long num = pow(10, left - 1);
        if (i%2){
            num *= 10;
        }

        num += n - 1;

        string s = to_string(num);
        string t = s;
        if (i%2){
            t.pop_back();
        }
        reverse(t.begin(), t.end());

        cout << s + t << endl;
        break;
    }
    return 0;

}