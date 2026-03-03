#include <iostream>
#include "backtrack.h"

using namespace std;

int main() {
    cin >> N;

    if (N % 2 == 0) {
        int k = N / 2;
        cout << 4 << endl;
        cout << "1 1 " << k << endl;
        cout << (k+1) << " 1 " << k << endl;
        cout << "1 " << (k+1) << " " << k << endl;
        cout << (k+1) << " " << (k+1) << " " << k << endl;
        return 0;
    }
    
    empty_count = N * N;
    
    backtrack();
    
    cout << min_count << endl;
    for (const auto& sq : best_result) {
        cout << sq.x + 1 << " " << sq.y + 1 << " " << sq.size << endl;
    }
    
    return 0;
}