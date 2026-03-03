CXX = g++
CXXFLAGS = -O3 -std=c++17 -Wall

GTEST_INCLUDE = ./googletest/include
GTEST_LIB = ./googletest/build/lib
GTEST_FLAGS = -I$(GTEST_INCLUDE) -L$(GTEST_LIB) -lgtest -lgtest_main -pthread

all: main benchmark tests

main: main.cpp backtrack.cpp backtrack.h
	$(CXX) $(CXXFLAGS) main.cpp backtrack.cpp -o main

benchmark: benchmark.cpp backtrack.cpp backtrack.h
	$(CXX) $(CXXFLAGS) benchmark.cpp backtrack.cpp -o benchmark

tests: tests.cpp backtrack.cpp backtrack.h
	$(CXX) $(CXXFLAGS) tests.cpp backtrack.cpp $(GTEST_FLAGS) -o tests

graphs:
	python plot_benchmark.py

run: main
	./main

bench: benchmark
	./benchmark

test: tests
	./tests

clean:
	del /Q *.o *.exe main benchmark tests *.csv 2>nul || echo Cleaned

.PHONY: all clean run bench test graphs