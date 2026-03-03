#include <iostream>
#include <fstream>
#include <chrono>
#include <iomanip>
#include "backtrack.h"

using namespace std;
using namespace chrono;

long long benchmark(int n) {
    N = n;
    resetState();
    
    auto start = high_resolution_clock::now();
    
    if (N % 2 == 0) {
        min_count = 4;
        int k = N / 2;
        (void)k;
    } else {
        empty_count = N * N;
        backtrack();
    }
    
    auto end = high_resolution_clock::now();
    return duration_cast<nanoseconds>(end - start).count();
}

void run_benchmark() {
    cout << "Бенчмарк: Время выполнения от размера N\n";
    cout << "========================================\n\n";
    cout << setw(5) << "N" 
         << setw(20) << "Время (нс)" 
         << setw(15) << "Квадратов" << endl;
    cout << string(40, '-') << endl;
    
    ofstream csv("benchmark_data.csv");
    csv << "N,Time_ns,Squares\n";
    
    for (int n = 2; n <= 20; n++) {
        long long time_ns = benchmark(n);
        
        cout << setw(5) << n 
             << setw(20) << time_ns
             << setw(15) << min_count << endl;
        
        csv << n << "," << time_ns << "," << min_count << "\n";
    }
    
    csv.close();
    cout << "\n========================================\n";
}

int main() {
    run_benchmark();
    return 0;
}
