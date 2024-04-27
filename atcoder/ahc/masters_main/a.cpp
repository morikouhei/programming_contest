#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <chrono>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <filesystem>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define srep(i, s, t) for (int i = s; i < t; ++i)
#define drep(i, n) for (int i = (n) - 1; i >= 0; --i)
using namespace std;
typedef long long int ll;
typedef pair<int, int> P;

namespace /* 乱数ライブラリ */
{
static uint32_t randxor() {
  static uint32_t x = 123456789;
  static uint32_t y = 362436069;
  static uint32_t z = 521288629;
  static uint32_t w = 88675123;
  uint32_t t;

  t = x ^ (x << 11);
  x = y;
  y = z;
  z = w;
  return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
}

// 0以上1未満の小数をとる乱数
static double rand01() { return (randxor() + 0.5) * (1.0 / UINT_MAX); }
}  // namespace

#include <iostream>

struct Point {
  double x;
  double y;
};

struct LineSegment {
  Point start;
  Point end;
};

/**
   @brief 線分と点の距離を計算する。
   @param line 線分
   @param point 点
   @return ユークリッド距離
 */
double calc_dist(const LineSegment& line, const Point& point) {
  double x0 = point.x, y0 = point.y;
  double x1 = line.start.x, y1 = line.start.y;
  double x2 = line.end.x, y2 = line.end.y;

  double a = x2 - x1;
  double b = y2 - y1;
  double a2 = a * a;
  double b2 = b * b;
  double r2 = a2 + b2;
  double tt = -(a * (x1 - x0) + b * (y1 - y0));

  if (tt < 0)
    return sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0));
  else if (tt > r2)
    return sqrt((x2 - x0) * (x2 - x0) + (y2 - y0) * (y2 - y0));

  double f1 = a * (y1 - y0) - b * (x1 - x0);
  return sqrt((f1 * f1) / r2);
}

// 配列シャッフル
std::random_device seed_gen;
std::mt19937 engine(seed_gen());
// std::shuffle(v.begin(), v.end(), engine);

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, -1, 0, 1};

double TL = 1.8;
int mode;
const int MAX_T = 5000;

int n, m;
double eps, sigma;
int sx, sy;
int p[15][2];
int l[15][2], r[15][2];
int c[5500], h[5500], q[5500][15];

double alpha[5500];
int f[5500][2];

// 複数ケース回すときに内部状態を初期値に戻す
void SetUp() {}

// 入力受け取り
void Input(int problemNum) {
  string fileNameIfs = "./in/";
  string strNum;
  rep(i, 4) {
    strNum += (char)(problemNum % 10 + '0');
    problemNum /= 10;
  }
  reverse(strNum.begin(), strNum.end());
  fileNameIfs += strNum + ".txt";

  ifstream ifs(fileNameIfs);

  // 標準入力する
  if (!ifs.is_open()) {
    cin >> n >> m >> eps >> sigma;
    cin >> sx >> sy;
    rep(i, n) { cin >> p[i][0] >> p[i][1]; }
    rep(i, m) { cin >> l[i][0] >> l[i][1] >> r[i][0] >> r[i][1]; }
  }
  // ファイル入力する
  else {
    ifs >> n >> m >> eps >> sigma;
    ifs >> sx >> sy;
    rep(i, n) { ifs >> p[i][0] >> p[i][1]; }
    rep(i, m) { ifs >> l[i][0] >> l[i][1] >> r[i][0] >> r[i][1]; }
    rep(i, MAX_T) { ifs >> alpha[i]; }
    rep(i, MAX_T) { ifs >> f[i][0] >> f[i][1]; }
  }
}

// 出力ファイルストリームオープン
void OpenOfs(int probNum, ofstream& ofs) {
  if (mode != 0) {
    string fileNameOfs = "./out/";
    string strNum;
    rep(i, 4) {
      strNum += (char)(probNum % 10 + '0');
      probNum /= 10;
    }
    reverse(strNum.begin(), strNum.end());
    fileNameOfs += strNum + ".txt";

    ofs.open(fileNameOfs);
  }
}

// スコア計算
ll CalcScore() {
  ll res = 0;
  return res;
}

const int INF = 1001001001;
double dist[12][12];
double dp[1 << 12][12];
int dp2[1 << 12][12];
void InitDist() {
  rep(i, n + 1) {
    rep(j, n + 1) {
      if (i == j) {
        dist[i][j] = 0;
      } else {
        if (i == n) {
          dist[i][j] = sqrt((double)(sx - p[j][0]) * (sx - p[j][0]) +
                            (sy - p[j][1]) * (sy - p[j][1]));
        } else if (j == n) {
          dist[i][j] = sqrt((double)(p[i][0] - sx) * (p[i][0] - sx) +
                            (p[i][1] - sy) * (p[i][1] - sy));
        } else {
          dist[i][j] = sqrt((double)(p[i][0] - p[j][0]) * (p[i][0] - p[j][0]) +
                            (p[i][1] - p[j][1]) * (p[i][1] - p[j][1]));
        }
      }
    }
  }
}
vector<int> BitDP() {
  InitDist();
  rep(i, 1 << n) {
    rep(j, 12) {
      dp[i][j] = INF;
      dp2[i][j] = -1;
    }
  }
  dp[0][n] = 0;
  rep(iii, n) {
    rep(i, 1 << n) {
      if (__builtin_popcountll(i) != iii) continue;
      bitset<20> bi(i);
      rep(j, n + 1) {
        if (dp[i][j] == INF) continue;
        rep(k, n) {
          if (bi[k] == 0) {
            double tmp = dp[i][j] + dist[j][k];
            if (tmp < dp[i | (1 << k)][k]) {
              dp[i | (1 << k)][k] = tmp;
              dp2[i | (1 << k)][k] = j;
            }
          }
        }
      }
    }
  }

  double minScore = INF;
  int goal = -1;
  rep(j, n) {
    if (dp[(1 << n) - 1][j] < minScore) {
      minScore = dp[(1 << n) - 1][j];
      goal = j;
    }
  }
  vector<int> ret;
  int now = (1 << n) - 1;
  while (goal != n) {
    ret.push_back(goal);

    int newgoal = dp2[now][goal];
    now -= (1 << goal);
    goal = newgoal;
  }

  reverse(ret.begin(), ret.end());
  return ret;
}

// 初期解生成
int X[5500], Y[5500];
int VX[5500], VY[5500];
int AX[5500], AY[5500];
int realX[5500], realY[5500];
int realVX[5500], realVY[5500];
int query[5500];

int realVisited[12];
vector<int> CalcPoint(int t) {
  vector<int> res;
  rep(i, n) {
    if (realVisited[i]) continue;
    Point point1 = {p[i][0], p[i][1]};
    LineSegment line1 = {{realX[t - 1], realY[t - 1]}, {realX[t], realY[t]}};
    double dist = calc_dist(line1, point1);
    if (dist <= 1000) {
      res.push_back(i);
    }
  }
  return res;
}

int CalcReal(int t, vector<int>& q) {
  int res = 0;
  realVX[t] = realVX[t - 1] + AX[t] + f[t - 1][0];
  realVY[t] = realVY[t - 1] + AY[t] + f[t - 1][1];
  realX[t] = realX[t - 1] + realVX[t];
  realY[t] = realY[t - 1] + realVY[t];
  if (realX[t] < -100000 || 100000 < realX[t] || realY[t] < -100000 ||
      100000 < realY[t]) {
    res = 1;
    realVX[t] = 0;
    realVY[t] = 0;
    realX[t] = realX[t - 1];
    realY[t] = realY[t - 1];
    q.clear();
  }

  q = CalcPoint(t);
  return res;
}

int GetKeisoku(int t, int dirX) {
  if (dirX == 1) {
    return round((double)(100000 - realX[t - 1]) * alpha[t - 1]);
  } else {
    return round((double)(100000 - realY[t - 1]) * alpha[t - 1]);
  }
}

void Initialize(ofstream& ofs) {
  auto route = BitDP();
  int mokutekichiIndex = 0;
  int visited[12] = {};
  X[0] = sx;
  Y[0] = sy;
  VX[0] = 0;
  VY[0] = 0;
  AX[0] = 0;
  AY[0] = 0;
  query[0] = 0;
  srep(t, 1, MAX_T + 1) {
    int pp = route[mokutekichiIndex];
    while (mokutekichiIndex < n && visited[pp]) {
      mokutekichiIndex++;
      pp = route[mokutekichiIndex];
    }
    if (mokutekichiIndex == n) break;

    query[t] = query[t - 1];
    if (query[t] == 0) {
      if (randxor() % 3 == 0) {
        query[t] = 2;
      }
    } else if (query[t] == 1) {
      query[t] = 0;
    } else if (query[t] == 2) {
      query[t] = 1;
    }

    if (query[t] == 0) {
      double diffX = p[pp][0] - X[t - 1];
      double diffY = p[pp][1] - Y[t - 1];

      double dirX = diffX / sqrt(diffX * diffX + diffY * diffY);
      double dirY = diffY / sqrt(diffX * diffX + diffY * diffY);

      double ax2 = diffX - VX[t - 1] / 1.0;
      double ay2 = diffY - VY[t - 1] / 1.0;
      double dirX2 = ax2 / sqrt(ax2 * ax2 + ay2 * ay2);
      double dirY2 = ay2 / sqrt(ax2 * ax2 + ay2 * ay2);

      int len = 500;
      // AX[t] = dirX * len;
      // AY[t] = dirY * len;
      AX[t] = dirX2 * len;
      AY[t] = dirY2 * len;
      while (AX[t] * AX[t] + AY[t] * AY[t] > 500 * 500) {
        len--;
        // AX[t] = dirX * len;
        // AY[t] = dirY * len;
        AX[t] = dirX2 * len;
        AY[t] = dirY2 * len;
      }

      // int b1 = 0, b2 = 0;
      // double norm = sqrt(VX[t - 1] * VX[t - 1] + VY[t - 1] * VY[t - 1]);
      // if (norm == 0) norm - 1;
      // double dirVX = VX[t - 1] / norm;
      // double dirVY = VY[t - 1] / norm;

      if (mode == 0) {
        cout << "A " << AX[t] << ' ' << AY[t] << endl;
      } else {
        ofs << "A " << AX[t] << ' ' << AY[t] << endl;
      }
      fflush(stdout);

      if (mode == 0) {
        cin >> c[t] >> h[t];
        rep(i, h[t]) {
          cin >> q[t][i];
          visited[q[t][i]] = 1;
        }
      } else {
        vector<int> qq;
        c[t] = CalcReal(t, qq);
        h[t] = qq.size();
        rep(i, qq.size()) {
          q[t][i] = qq[i];
          visited[q[t][i]] = 1;
        }
      }

      if (c[t] == 0) {
        VX[t] = VX[t - 1] + AX[t];
        VY[t] = VY[t - 1] + AY[t];
        X[t] = X[t - 1] + VX[t];
        Y[t] = Y[t - 1] + VY[t];
      } else {
        VX[t] = 0;
        VY[t] = 0;
        X[t] = X[t - 1];
        Y[t] = Y[t - 1];
      }
    } else if (query[t] == 1) {
      if (mode == 0) {
        if (X[t - 1] > 0) {
          cout << "S 1 0" << endl;
        } else {
          cout << "S -1 0" << endl;
        }
        fflush(stdout);
      } else {
        ofs << "S 1 0" << endl;
      }

      int res;

      if (mode == 0) {
        cin >> res;

        cin >> c[t] >> h[t];
        rep(i, h[t]) {
          cin >> q[t][i];
          visited[q[t][i]] = 1;
        }
      } else {
        res = GetKeisoku(t, 1);

        vector<int> qq;
        c[t] = CalcReal(t, qq);
        h[t] = qq.size();
        rep(i, qq.size()) {
          q[t][i] = qq[i];
          visited[q[t][i]] = 1;
        }
      }

      if (X[t - 1] > 0) {
        X[t - 1] = 100000 - res;
      } else {
        X[t - 1] = res - 100000;
      }

      if (c[t] == 0) {
        VX[t] = VX[t - 1] + AX[t];
        VY[t] = VY[t - 1] + AY[t];
        X[t] = X[t - 1] + VX[t];
        Y[t] = Y[t - 1] + VY[t];
      } else {
        VX[t] = 0;
        VY[t] = 0;
        X[t] = X[t - 1];
        Y[t] = Y[t - 1];
      }

    } else if (query[t] == 2) {
      if (mode == 0) {
        if (Y[t - 1] > 0) {
          cout << "S 0 1" << endl;
        } else {
          cout << "S 0 -1" << endl;
        }
        fflush(stdout);
      } else {
        ofs << "S 0 1" << endl;
      }

      int res;
      if (mode == 0) {
        cin >> res;

        cin >> c[t] >> h[t];
        rep(i, h[t]) {
          cin >> q[t][i];
          visited[q[t][i]] = 1;
        }
      } else {
        res = GetKeisoku(t, 0);
        vector<int> qq;
        c[t] = CalcReal(t, qq);
        h[t] = qq.size();
        rep(i, qq.size()) {
          q[t][i] = qq[i];
          visited[q[t][i]] = 1;
        }
      }

      if (Y[t - 1] > 0) {
        Y[t - 1] = 100000 - res;
      } else {
        Y[t - 1] = res - 100000;
      }

      if (c[t] == 0) {
        VX[t] = VX[t - 1] + AX[t];
        VY[t] = VY[t - 1] + AY[t];
        X[t] = X[t - 1] + VX[t];
        Y[t] = Y[t - 1] + VY[t];
      } else {
        VX[t] = 0;
        VY[t] = 0;
        X[t] = X[t - 1];
        Y[t] = Y[t - 1];
      }
    }
  }
}

// 解答出力
void Output(ofstream& ofs) {
  if (mode == 0) {
  } else {
  }
}

ll Solve(int probNum) {
  // 複数ケース回すときに内部状態を初期値に戻す
  SetUp();

  // 入力受け取り
  Input(probNum);

  // 出力ファイルストリームオープン
  ofstream ofs;
  OpenOfs(probNum, ofs);

  // 初期解生成
  Initialize(ofs);

  // 解答を出力
  Output(ofs);

  if (ofs.is_open()) {
    ofs.close();
  }

  ll score = 0;
  if (mode != 0) {
    score = CalcScore();
  }
  return score;
}

int main() {
  srand((unsigned)time(NULL));
  while (rand() % 100) {
    randxor();
  }

  mode = 0;

  if (mode == 0) {
    Solve(0);
  } else if (mode == 1) {
    ll sum = 0;
    srep(i, 0, 100) {
      ll score = Solve(i);
      sum += score;
      cout << "num = " << i << ", ";
      cout << "score = " << score << ", ";
      cout << "sum = " << sum << endl;
    }
  }

  return 0;
}
