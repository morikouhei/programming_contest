#include <iostream>
#include <vector>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n, m;
    std::cin >> n >> m;

    std::vector<std::vector<std::vector<int>>> cross(n+1, std::vector<std::vector<int>>(n + 1, std::vector<int>(n + 1, 0)));
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(n + 1, 0));

    for (int i = 0; i < m; ++i) {
        int l, r;
        std::cin >> l >> r;
        l -= 1;
        for (int j = l; j < r; ++j) {
            cross[j][l][r] = 1;
        }
    }

    for (int le = 1; le <= n; ++le) {
        for (int l = 0; l < n; ++l) {
            int r = l + le;
            if (r > n) {
                break;
            }

            for (int i = l; i < r; ++i) {
                if (l >= 0) {
                    cross[i][l - 1][r] |= cross[i][l][r];
                }
                if (r + 1 <= n) {
                    cross[i][l][r + 1] |= cross[i][l][r];
                }
            }

            int ma = 0;
            for (int i = l; i < r; ++i) {
                ma = std::max(ma, dp[l][i] + dp[i + 1][r] + cross[i][l][r]);
            }

            dp[l][r] = ma;
        }
    }

    std::cout << dp[0][n] << std::endl;

    return 0;
}
