#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

  unsigned N;
  while (!cin.eof()) {
    vector<unsigned long> values;
    cin >> N;
    if (cin.eof()) return 0;
    unsigned long sum_max = 0;
    for (size_t i = 0; i < N; i++) {
      unsigned k;
      cin >> k;
      values.push_back(k);
      sum_max += k;
    }
    sort(values.begin(), values.end());

    bool mat[N + 1][sum_max + 1];

    for (size_t i = 0; i <= N; i++) {
      mat[i][0] = true;
    }
    for (size_t j = 1; j <= sum_max; j++) {
      mat[0][j] = false;
    }


    for (size_t i = 1; i <= N; i++) {
      for (size_t j = 1; j <= sum_max; j++) {
        auto v = values[i - 1];
        if (v <= j) {
          mat[i][j] = mat[i - 1][j] || mat[i - 1][j - v];
        } else {
          mat[i][j] = mat[i - 1][j];
        }
      }
    }

    unsigned long best_split = sum_max / 2;
    while (!mat[N][best_split]) best_split--;

    cout << (sum_max - 2*best_split) << endl;
  }

  return 0;
}