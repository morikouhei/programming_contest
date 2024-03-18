#include <iostream>
#include <vector>
#include <atcoder/segtree>
using namespace std;
using namespace atcoder;

// セグメントの値を管理するための構造体

struct top2{
    int n1,n1_num;
    int n2,n2_num;
};
// セグメント同士のマージ関数
top2 op(top2 a, top2 b) {

    int top = max(a.n1,b.n1);

    int second = max(a.n2,b.n2);

    if (a.n1 != b.n1){
        second = max(second,a.n1+b.n1-top);
    }

    vector<top2> temp{a,b};

    int top_num = 0;
    int second_num = 0;
    for (top2& now : {a,b}){
        if (now.n1 == top){
            top_num += now.n1_num;
        }

        if (now.n2 == second){
            second_num += now.n2_num;
        }

        if (now.n1 == second){
            second_num += now.n1_num;
        }
        
        
    }

    return top2{top,top_num,second,second_num};
    
}

// セグメントツリーの初期値
top2 e() {
    return top2{0,0,0,0}; // 最小値で初期化
}

// 配列A[i]の値を更新するための関数
top2 target(int x) {
    return top2{x,1,0,0}; // 更新値として最大値を設定し、次に大きい値は最小値
}

int main() {
    int n, q;
    cin >> n >> q;
    vector<top2> A(n);
    for(int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        A[i] = target(x);
    }

    segtree<top2, op, e> seg(A);

    for(int i = 0; i < q; ++i) {
        int type;
        cin >> type;
        if(type == 1) {
            int idx, x;
            cin >> idx >> x;
            --idx; // 0-indexed
            seg.set(idx, target(x));
        } else if(type == 2) {
            int l, r;
            cin >> l >> r;
            --l; // 0-indexed
            top2 res = seg.prod(l, r);
            cout << res.n2_num << "\n";
        }
    }
}
