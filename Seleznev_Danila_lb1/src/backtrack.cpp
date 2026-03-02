#include "backtrack.h"

int N;
unsigned int board[20] = {0};
int empty_count;
vector<Square> result;
vector<Square> best_result;
int min_count = 1e9;

bool canPlace(int x, int y, int size) {
    if (x + size > N || y + size > N) return false;
    unsigned int mask = ((1U << size) - 1) << y;
    for (int i = x; i < x + size; i++) {
        if (board[i] & mask) return false;
    }
    return true;
}

void placeSquare(int x, int y, int size, int mark) {
    unsigned int mask = ((1U << size) - 1) << y;
    for (int i = x; i < x + size; i++) {
        if (mark == 1) {
            unsigned int changed = (~board[i]) & mask;
            empty_count -= __builtin_popcount(changed);
            board[i] |= mask;
        } else {
            unsigned int changed = board[i] & mask;
            empty_count += __builtin_popcount(changed);
            board[i] &= ~mask;
        }
    }
}

pair<int, int> findNextEmpty() {
    for (int i = 0; i < N; i++) {
        if (board[i] != ((1U << N) - 1)) {
            for (int j = 0; j < N; j++) {
                if (!(board[i] & (1U << j))) {
                    return {i, j};
                }
            }
        }
    }
    return {-1, -1};
}

void backtrack() {
    if (result.size() >= min_count) return;

    if (empty_count > 0) {
        int maxSquareArea = (N - 1) * (N - 1);
        int minNeeded = (empty_count + maxSquareArea - 1) / maxSquareArea;
        if (result.size() + minNeeded >= min_count) return;
    }
    
    auto [x, y] = findNextEmpty();
    
    if (x == -1) {
        if (result.size() < min_count) {
            min_count = result.size();
            best_result = result;
        }
        return;
    }

    int maxSize = 0;
    while (maxSize + 1 < N && canPlace(x, y, maxSize + 1)) {
        maxSize++;
    }

    for (int size = maxSize; size >= 1; size--) {
        placeSquare(x, y, size, 1);
        result.push_back({x, y, size});
        
        backtrack();
        
        result.pop_back();
        placeSquare(x, y, size, 0);
    }
}

void resetState() {
    for (int i = 0; i < 20; i++) {
        board[i] = 0;
    }
    result.clear();
    best_result.clear();
    min_count = 1e9;
}
