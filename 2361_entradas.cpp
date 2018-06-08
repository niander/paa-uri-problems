#include <iostream>

using namespace std;

int main() {
    unsigned N;
    unsigned K;
    while (true) {
        cin >> N >> K;
        if (N == 0 && K == 0) break;

        auto j = N;
        for(unsigned i = 1; i <= N; i++) {
            if (i < K) {
                if (i == 1)
                    cout << i;
                else
                    cout << " " << i;
            } else {
                if (i == 1)
                    cout << j;
                else
                    cout << " " << j;
                j = j - 1;
            }
        }
        cout << endl;
    }
    return 0;
}