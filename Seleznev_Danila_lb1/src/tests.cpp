#include <gtest/gtest.h>
#include "backtrack.h"

class BacktrackTest : public ::testing::Test {
protected:
    void SetUp() override {
        resetState();
    }
    
    void runTest(int n) {
        N = n;
        if (N % 2 == 0) {
            min_count = 4;
        } else {
            empty_count = N * N;
            backtrack();
        }
    }
};

TEST_F(BacktrackTest, MinimalSize) {
    runTest(2);
    EXPECT_EQ(min_count, 4);
}

TEST_F(BacktrackTest, MinimalOdd) {
    runTest(3);
    EXPECT_EQ(min_count, 6);
}

TEST_F(BacktrackTest, EvenN) {
    runTest(10);
    EXPECT_EQ(min_count, 4);
}

TEST_F(BacktrackTest, OddN) {
    runTest(7);
    EXPECT_EQ(min_count, 9);
}

TEST_F(BacktrackTest, MaxEven) {
    runTest(20);
    EXPECT_EQ(min_count, 4);
}

TEST_F(BacktrackTest, MaxOdd) {
    runTest(19);
    EXPECT_EQ(min_count, 13);
}

TEST_F(BacktrackTest, SolutionValidity) {
    runTest(5);
    
    ASSERT_GT(best_result.size(), 0);
    
    for (const auto& sq : best_result) {
        EXPECT_GE(sq.x, 0);
        EXPECT_GE(sq.y, 0);
        EXPECT_LT(sq.x + sq.size, N + 1);
        EXPECT_LT(sq.y + sq.size, N + 1);
        EXPECT_GT(sq.size, 0);
        EXPECT_LT(sq.size, N);
    }
}
