#pragma once

#include <vector>
using namespace std;

struct Square {
    int x, y, size;
};

extern int N;
extern unsigned int board[20];
extern int empty_count;
extern vector<Square> result;
extern vector<Square> best_result;
extern int min_count;

bool canPlace(int x, int y, int size);
void placeSquare(int x, int y, int size, int mark);
pair<int, int> findNextEmpty();
void backtrack();
void resetState();

