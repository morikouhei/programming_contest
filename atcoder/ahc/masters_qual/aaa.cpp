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
#define drep(i, n) for (int i = (n)-1; i >= 0; --i)
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

// 配列シャッフル
std::random_device seed_gen;
std::mt19937 engine(seed_gen());
// std::shuffle(v.begin(), v.end(), engine);

const int dx[5] = {-1, 0, 1, 0, 0};
const int dy[5] = {0, -1, 0, 1, 0};

double TL = 1.8;
int mode;
const ll INF = 1001001001001001001;
clock_t startTime, endTime;

int t, n;
int v[110][110];
int h[110][110];
int a[110][110];
int initA[110][110];
int ansA[110][110];

int anspi, anspj, ansqi, ansqj;
ll minScore = INF;
int ansS[50000], ansD[50000], ansE[50000];

bool IsNG(int x, int y, int z) {
  int nx = x + dx[z];
  int ny = y + dy[z];
  if (nx < 0 || n <= nx || ny < 0 || n <= ny) return true;
  if (z == 0) {
    if (h[nx][ny]) return true;
  }
  if (z == 1) {
    if (v[nx][ny]) return true;
  }
  if (z == 2) {
    if (h[x][y]) return true;
  }
  if (z == 3) {
    if (v[x][y]) return true;
  }

  return false;
}

// 複数ケース回すときに内部状態を初期値に戻す
void SetUp() { minScore = INF; }

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
  if (mode == 0 || !ifs.is_open()) {
    cin >> t >> n;
    rep(i, n) {
      string str;
      cin >> str;
      rep(j, n - 1) { v[i][j] = str[j] - '0'; }
    }
    rep(i, n - 1) {
      string str;
      cin >> str;
      rep(j, n) { h[i][j] = str[j] - '0'; }
    }
    rep(i, n) {
      rep(j, n) { cin >> a[i][j]; }
    }
  }
  // ファイル入力する
  else {
    ifs >> t >> n;
    rep(i, n) {
      string str;
      ifs >> str;
      rep(j, n - 1) { v[i][j] = str[j] - '0'; }
    }
    rep(i, n - 1) {
      string str;
      ifs >> str;
      rep(j, n) { h[i][j] = str[j] - '0'; }
    }
    rep(i, n) {
      rep(j, n) { ifs >> a[i][j]; }
    }
  }

  rep(i, n) {
    rep(j, n) { initA[i][j] = a[i][j]; }
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
  rep(i, n) {
    rep(j, n) {
      srep(k, 2, 4) {
        if (IsNG(i, j, k)) continue;
        int ni = i + dx[k];
        int nj = j + dy[k];
        res += (a[i][j] - a[ni][nj]) * (a[i][j] - a[ni][nj]);
      }
    }
  }
  return res;
}

int visitedDFS[110][110];
void InnerDFS(int x, int y, vector<int>& vec, int travelMethod = 0) {
  if (travelMethod == 0) {
    rep(i, 4) {
      if (IsNG(x, y, i)) continue;
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (visitedDFS[nx][ny]) continue;
      vec.push_back(i);
      visitedDFS[nx][ny] = 1;
      InnerDFS(nx, ny, vec);
      vec.push_back((i + 2) % 4);
    }
  } else if (travelMethod == 1) {
    drep(i, 4) {
      if (IsNG(x, y, i)) continue;
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (visitedDFS[nx][ny]) continue;
      vec.push_back(i);
      visitedDFS[nx][ny] = 1;
      InnerDFS(nx, ny, vec);
      vec.push_back((i + 2) % 4);
    }
  }
}

vector<int> DFS(int sx, int sy, int travelMethod = 0) {
  rep(i, n) rep(j, n) visitedDFS[i][j] = 0;
  vector<int> res;
  visitedDFS[sx][sy] = 1;
  InnerDFS(sx, sy, res);
  return res;
}

int CalcTwoPositionScore(int x1, int y1, int x2, int y2) {
  int res = 0;
  rep(i, 4) {
    if (IsNG(x1, y1, i)) continue;
    int nx = x1 + dx[i];
    int ny = y1 + dy[i];
    res += (a[x1][y1] - a[nx][ny]) * (a[x1][y1] - a[nx][ny]);
  }
  rep(i, 4) {
    if (IsNG(x2, y2, i)) continue;
    int nx = x2 + dx[i];
    int ny = y2 + dy[i];
    res += (a[x2][y2] - a[nx][ny]) * (a[x2][y2] - a[nx][ny]);
  }
  return res;
}

void Method1() {
  int loop = 0;
  while (true) {
    endTime = clock();
    if ((double)(endTime - startTime) / CLOCKS_PER_SEC > TL / 10) {
      break;
    }
    rep(i, n) {
      rep(j, n) { a[i][j] = initA[i][j]; }
    }
    loop++;
    int pi = randxor() % n;
    int qi = randxor() % n;
    int pj = randxor() % n;
    int qj = randxor() % n;
    vector<int> moveP, moveQ;
    int travelMethod = 0;
    while (moveP.size() < n * n * 4) {
      auto vec = DFS(pi, pj, travelMethod);
      travelMethod = 1;
      for (auto mo : vec) {
        moveP.push_back(mo);
      }
    }
    travelMethod = 0;
    while (moveQ.size() < n * n * 4) {
      auto vec = DFS(qi, qj, travelMethod);
      travelMethod = 1;
      for (auto mo : vec) {
        moveQ.push_back(mo);
      }
    }
    vector<int> doSwapVec(n * n * 4);
    int nowPx = pi;
    int nowPy = pj;
    int nowQx = qi;
    int nowQy = qj;
    rep(turn, n * n * 4) {
      int beforeScore = CalcTwoPositionScore(nowPx, nowPy, nowQx, nowQy);
      swap(a[nowPx][nowPy], a[nowQx][nowQy]);
      int afterScore = CalcTwoPositionScore(nowPx, nowPy, nowQx, nowQy);
      if (afterScore <= beforeScore) {
        doSwapVec[turn] = 1;
      } else {
        doSwapVec[turn] = 0;
        swap(a[nowPx][nowPy], a[nowQx][nowQy]);
      }
      nowPx = nowPx + dx[moveP[turn]];
      nowPy = nowPy + dy[moveP[turn]];
      nowQx = nowQx + dx[moveQ[turn]];
      nowQy = nowQy + dy[moveQ[turn]];
    }

    ll tmpScore = CalcScore();
    if (tmpScore < minScore) {
      minScore = tmpScore;
      anspi = pi;
      anspj = pj;
      ansqi = qi;
      ansqj = qj;
      rep(i, n * n * 4) {
        ansS[i] = doSwapVec[i];
        ansD[i] = moveP[i];
        ansE[i] = moveQ[i];
      }
      rep(i, n) {
        rep(j, n) { ansA[i][j] = a[i][j]; }
      }
    }
  }

  if (mode != 0) {
    // cout << "loop = " << loop << endl;
  }

  loop = 0;
  int saitaku = 0;
  while (true) {
    endTime = clock();
    if ((double)(endTime - startTime) / CLOCKS_PER_SEC > TL) {
      break;
    }
    loop++;
    rep(i, n) {
      rep(j, n) { a[i][j] = initA[i][j]; }
    }

    int turn = randxor() % (n * n * 4);
    ansS[turn] = 1 - ansS[turn];
    int nowPx = anspi;
    int nowPy = anspj;
    int nowQx = ansqi;
    int nowQy = ansqj;
    rep(i, n * n * 4) {
      if (ansS[i] == 1) {
        swap(a[nowPx][nowPy], a[nowQx][nowQy]);
      }

      nowPx = nowPx + dx[ansD[i]];
      nowPy = nowPy + dy[ansD[i]];
      nowQx = nowQx + dx[ansE[i]];
      nowQy = nowQy + dy[ansE[i]];
    }

    ll tmpScore = CalcScore();
    if (tmpScore < minScore) {
      minScore = tmpScore;
      saitaku++;
    } else {
      ansS[turn] = 1 - ansS[turn];
    }
  }

  if (mode != 0) {
    cout << "loop = " << loop << ", saitaku = " << saitaku << endl;
  }
}

void Method2() {
  int loop = 0;
  while (true) {
    endTime = clock();
    if ((double)(endTime - startTime) / CLOCKS_PER_SEC > TL / 10) {
      break;
    }
    rep(i, n) {
      rep(j, n) { a[i][j] = initA[i][j]; }
    }
    loop++;
    int pi = randxor() % n;
    int qi = randxor() % n;
    int pj = randxor() % n;
    int qj = randxor() % n;
    vector<int> moveP, moveQ;
    int travelMethod = 0;
    while (moveP.size() < n * n * 4) {
      auto vec = DFS(pi, pj, travelMethod);
      travelMethod = 1;
      for (auto mo : vec) {
        moveP.push_back(mo);
      }
    }
    travelMethod = 0;
    while (moveQ.size() < n * n * 4) {
      auto vec = DFS(qi, qj, travelMethod);
      travelMethod = 1;
      for (auto mo : vec) {
        moveQ.push_back(mo);
      }
    }

    vector<int> doSwapVec(n * n * 4);
    int nowPx = pi;
    int nowPy = pj;
    int nowQx = qi;
    int nowQy = qj;
    rep(turn, n * n * 4) {
      int swa = 0;
      if (a[nowPx][nowPy] < a[nowQx][nowQy]) {
        if (nowPx > nowPy) {
          swa = 1;
        }
      }
      if (a[nowPx][nowPy] > a[nowQx][nowQy]) {
        if (nowPx < nowPy) {
          swa = 1;
        }
      }
      if (swa) {
        doSwapVec[turn] = 1;
        swap(a[nowPx][nowPy], a[nowQx][nowQy]);
      }
      nowPx = nowPx + dx[moveP[turn]];
      nowPy = nowPy + dy[moveP[turn]];
      nowQx = nowQx + dx[moveQ[turn]];
      nowQy = nowQy + dy[moveQ[turn]];
    }

    rep(i, n) {
      rep(j, n) { a[i][j] = initA[i][j]; }
    }
    nowPx = pi;
    nowPy = pj;
    nowQx = qi;
    nowQy = qj;
    rep(turn, n * n * 4) {
      if (doSwapVec[turn]) {
        swap(a[nowPx][nowPy], a[nowQx][nowQy]);
      }
      int beforeScore = CalcTwoPositionScore(nowPx, nowPy, nowQx, nowQy);
      swap(a[nowPx][nowPy], a[nowQx][nowQy]);
      int afterScore = CalcTwoPositionScore(nowPx, nowPy, nowQx, nowQy);
      if (afterScore <= beforeScore) {
        doSwapVec[turn] = 1 - doSwapVec[turn];
      } else {
        swap(a[nowPx][nowPy], a[nowQx][nowQy]);
      }
      nowPx = nowPx + dx[moveP[turn]];
      nowPy = nowPy + dy[moveP[turn]];
      nowQx = nowQx + dx[moveQ[turn]];
      nowQy = nowQy + dy[moveQ[turn]];
    }

    ll tmpScore = CalcScore();
    if (tmpScore < minScore) {
      minScore = tmpScore;
      anspi = pi;
      anspj = pj;
      ansqi = qi;
      ansqj = qj;
      rep(i, n * n * 4) {
        ansS[i] = doSwapVec[i];
        ansD[i] = moveP[i];
        ansE[i] = moveQ[i];
      }
      rep(i, n) {
        rep(j, n) { ansA[i][j] = a[i][j]; }
      }
    }
  }

  if (mode != 0) {
    // cout << "loop = " << loop << endl;
  }

  loop = 0;
  int saitaku = 0;
  while (true) {
    endTime = clock();
    if ((double)(endTime - startTime) / CLOCKS_PER_SEC > TL) {
      break;
    }
    loop++;
    rep(i, n) {
      rep(j, n) { a[i][j] = initA[i][j]; }
    }

    int turn = randxor() % (n * n * 4);
    ansS[turn] = 1 - ansS[turn];
    int nowPx = anspi;
    int nowPy = anspj;
    int nowQx = ansqi;
    int nowQy = ansqj;
    rep(i, n * n * 4) {
      if (ansS[i] == 1) {
        swap(a[nowPx][nowPy], a[nowQx][nowQy]);
      }

      nowPx = nowPx + dx[ansD[i]];
      nowPy = nowPy + dy[ansD[i]];
      nowQx = nowQx + dx[ansE[i]];
      nowQy = nowQy + dy[ansE[i]];
    }

    ll tmpScore = CalcScore();
    if (tmpScore < minScore) {
      minScore = tmpScore;
      saitaku++;
    } else {
      ansS[turn] = 1 - ansS[turn];
    }
  }

  if (mode != 0) {
    cout << "loop = " << loop << ", saitaku = " << saitaku << endl;
  }
}

void Method3() {
  int loop = 0;
  while (true) {
    endTime = clock();
    if ((double)(endTime - startTime) / CLOCKS_PER_SEC > TL / 10) {
      break;
    }
    rep(i, n) {
      rep(j, n) { a[i][j] = initA[i][j]; }
    }
    loop++;
    int pi = randxor() % n;
    int qi = randxor() % n;
    int pj = randxor() % n;
    int qj = randxor() % n;
    vector<int> moveP, moveQ;
    int travelMethod = 0;
    while (moveP.size() < n * n * 4) {
      auto vec = DFS(pi, pj, travelMethod);
      travelMethod = 1;
      for (auto mo : vec) {
        moveP.push_back(mo);
      }
    }
    travelMethod = 0;
    while (moveQ.size() < n * n * 4) {
      auto vec = DFS(qi, qj, travelMethod);
      travelMethod = 1;
      for (auto mo : vec) {
        moveQ.push_back(mo);
      }
      moveQ.push_back(4);
    }

    vector<P> pPosVec;
    vector<P> qPosVec;
    {
      pPosVec.push_back(P(pi, pj));
      qPosVec.push_back(P(qi, qj));
      int nowPx = pi;
      int nowPy = pj;
      int nowQx = qi;
      int nowQy = qj;
      rep(turn, n * n * 4) {
        nowPx = nowPx + dx[moveP[turn]];
        nowPy = nowPy + dy[moveP[turn]];
        nowQx = nowQx + dx[moveQ[turn]];
        nowQy = nowQy + dy[moveQ[turn]];
        pPosVec.push_back(P(nowPx, nowPy));
        qPosVec.push_back(P(nowQx, nowQy));
      }
    }

    vector<int> doSwapVec(n * n * 4);
    int nowPx = pi;
    int nowPy = pj;
    int nowQx = qi;
    int nowQy = qj;
    rep(turn, n * n * 4) {
      ll bestScore = INF;
      int swa = 0;

      const int depth = 1;
      rep(i, 1 << depth) {
        ll tmpScore = 0;
        bitset<depth> f(i);
        rep(j, depth) {
          int now2Px = pPosVec[turn + j].first;
          int now2Py = pPosVec[turn + j].second;
          int now2Qx = qPosVec[turn + j].first;
          int now2Qy = qPosVec[turn + j].second;
          if (turn + j >= n * n * 4) break;
          int beforeScore =
              CalcTwoPositionScore(now2Px, now2Py, now2Qx, now2Qy);
          if (f[j]) {
            swap(a[now2Px][now2Py], a[now2Qx][now2Qy]);
          }
          int afterScore = CalcTwoPositionScore(now2Px, now2Py, now2Qx, now2Qy);
          tmpScore += afterScore - beforeScore;
        }
        if (tmpScore < bestScore) {
          bestScore = tmpScore;
          swa = f[0];
        }
        drep(j, depth) {
          if (turn + j >= n * n * 4) continue;
          int now2Px = pPosVec[turn + j].first;
          int now2Py = pPosVec[turn + j].second;
          int now2Qx = qPosVec[turn + j].first;
          int now2Qy = qPosVec[turn + j].second;
          if (f[j]) {
            swap(a[now2Px][now2Py], a[now2Qx][now2Qy]);
          }
        }
      }
      if (swa) {
        doSwapVec[turn] = 1;
        swap(a[nowPx][nowPy], a[nowQx][nowQy]);
      }

      nowPx = nowPx + dx[moveP[turn]];
      nowPy = nowPy + dy[moveP[turn]];
      nowQx = nowQx + dx[moveQ[turn]];
      nowQy = nowQy + dy[moveQ[turn]];
    }

    ll tmpScore = CalcScore();
    if (tmpScore < minScore) {
      minScore = tmpScore;
      anspi = pi;
      anspj = pj;
      ansqi = qi;
      ansqj = qj;
      rep(i, n * n * 4) {
        ansS[i] = doSwapVec[i];
        ansD[i] = moveP[i];
        ansE[i] = moveQ[i];
      }
      rep(i, n) {
        rep(j, n) { ansA[i][j] = a[i][j]; }
      }
    }
  }

  if (mode != 0) {
    cout << "loop = " << loop << endl;
  }

  loop = 0;
  int saitaku = 0;
  while (true) {
    endTime = clock();
    if ((double)(endTime - startTime) / CLOCKS_PER_SEC > TL) {
      break;
    }
    loop++;
    rep(i, n) {
      rep(j, n) { a[i][j] = initA[i][j]; }
    }

    int turn = randxor() % (n * n * 4);
    ansS[turn] = 1 - ansS[turn];
    int nowPx = anspi;
    int nowPy = anspj;
    int nowQx = ansqi;
    int nowQy = ansqj;
    rep(i, n * n * 4) {
      if (ansS[i] == 1) {
        swap(a[nowPx][nowPy], a[nowQx][nowQy]);
      }

      nowPx = nowPx + dx[ansD[i]];
      nowPy = nowPy + dy[ansD[i]];
      nowQx = nowQx + dx[ansE[i]];
      nowQy = nowQy + dy[ansE[i]];
    }

    ll tmpScore = CalcScore();
    if (tmpScore < minScore) {
      minScore = tmpScore;
      saitaku++;
    } else {
      ansS[turn] = 1 - ansS[turn];
    }
  }

  if (mode != 0) {
    cout << "loop = " << loop << ", saitaku = " << saitaku << endl;
  }
}

// 解答出力
void Output(ofstream& ofs) {
  if (mode == 0) {
    cout << anspi << ' ' << anspj << ' ' << ansqi << ' ' << ansqj << endl;
    rep(i, n * n * 4) {
      cout << ansS[i] << ' ';
      if (ansD[i] == 0)
        cout << 'U';
      else if (ansD[i] == 1)
        cout << 'L';
      else if (ansD[i] == 2)
        cout << 'D';
      else if (ansD[i] == 3)
        cout << 'R';
      else
        cout << '.';
      cout << ' ';
      if (ansE[i] == 0)
        cout << 'U';
      else if (ansE[i] == 1)
        cout << 'L';
      else if (ansE[i] == 2)
        cout << 'D';
      else if (ansE[i] == 3)
        cout << 'R';
      else
        cout << '.';
      cout << endl;
    }
  } else {
    ofs << anspi << ' ' << anspj << ' ' << ansqi << ' ' << ansqj << endl;
    rep(i, n * n * 4) {
      ofs << ansS[i] << ' ';
      if (ansD[i] == 0)
        ofs << 'U';
      else if (ansD[i] == 1)
        ofs << 'L';
      else if (ansD[i] == 2)
        ofs << 'D';
      else if (ansD[i] == 3)
        ofs << 'R';
      else
        ofs << '.';
      ofs << ' ';
      if (ansE[i] == 0)
        ofs << 'U';
      else if (ansE[i] == 1)
        ofs << 'L';
      else if (ansE[i] == 2)
        ofs << 'D';
      else if (ansE[i] == 3)
        ofs << 'R';
      else
        ofs << '.';
      ofs << endl;
    }
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

  ll beforeScore = 0;
  if (mode != 0) {
    // rep(i, n) {
    //   rep(j, n) { cout << setw(4) << a[i][j] << ' '; }
    //   cout << endl;
    // }
    // cout << endl;
    beforeScore = CalcScore();
  }
  startTime = clock();
  endTime = clock();
  Method3();
  // Method2();

  rep(i, n) {
    rep(j, n) { a[i][j] = initA[i][j]; }
  }

  // 解答を出力
  Output(ofs);

  if (ofs.is_open()) {
    ofs.close();
  }

  ll score = 0;
  if (mode != 0) {
    rep(i, n) {
      rep(j, n) { cout << setw(4) << ansA[i][j] << ' '; }
      cout << endl;
    }
    cout << endl;

    ll afterScore = minScore;
    cout << beforeScore << ' ' << afterScore << endl;
    score =
        max(1LL, (ll)round(1000000LL * log2((double)beforeScore / afterScore)));
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
    srep(i, 0, 20) {
      ll score = Solve(i);
      sum += score;
      cout << "num = " << i << ", ";
      cout << "score = " << score << ", ";
      cout << "sum = " << sum << endl;
    }
  }

  return 0;
}
