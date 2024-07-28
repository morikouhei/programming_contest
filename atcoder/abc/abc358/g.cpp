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

    int h,w,k;
    cin >> h >> w >> k;
    int si,sj;
    cin >> si >> sj;
    si--; sj--;
    vector<vector<long long>> A(h,vector<long long>(w));
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            cin >> A[i][j];
        }
    }

    vector<vector<vector<long long>>> dp(min(k+1,h*w+10),vector<vector<long long>>(h,vector<long long>(w,-1)));
    dp[0][si][sj] = 0;
    vector<int> di = {0,1,0,-1,0};
    vector<int> dj = {1,0,-1,0,0};

    int lt = min(k,h*w+5);
    for (int t = 0; t < lt; t++){
        for (int i = 0; i < h; i++){
            for (int j = 0; j < w; j++){
                if (dp[t][i][j] == -1) continue;
                for (int l = 0; l < 5; l++){
                    int ni = i+di[l];
                    int nj = j+dj[l];
                    if (ni < 0 || ni >= h || nj < 0 || nj >= w) continue;
                    
                    dp[t+1][ni][nj] = max(dp[t+1][ni][nj],dp[t][i][j] + A[ni][nj]);
                }
            }
        }
    }

    long long ans = 0;
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            ans = max(ans,dp[lt][i][j] + (k-lt)*A[i][j] );
        }
    }

    cout << ans << endl;
    
    return 0;

}