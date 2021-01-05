#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> s(n);
    for (int q = 0; q < n; ++q) {
        cin >> s[q];
    }
    sort(s.begin(), s.end());
    int val[n];
    for (int i = 0; i < s.size(); ++i) {
        val[i] = 0;
        for (int j = 0; j < s[i].size(); ++j) {
            val[i] += (s[i][j] - 'A' + 1);
        }
        val[i] *= (i + 1);
    }
    int t;
    cin >> t;
    string ss;
    for (int z = 0; z < t; ++z) {
        cin >> ss;
        for (int i = 0; i < s.size(); ++i) {
            if (ss == s[i]) {
                cout << val[i] << "\n";
                break;
            }   
        }
    }
    return 0;
}
