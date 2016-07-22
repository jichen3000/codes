#include <iostream>
#include <ctime>
#include <chrono>
#include <thread>
using namespace std;

int main() {
    // const clock_t begin_time = clock();
    time_t begin_time;
    time(&begin_time);
    const auto x = 1;
    this_thread::sleep_for(chrono::seconds(x));
    // const clock_t end_time = clock();
    time_t end_time;
    time(&end_time);

    // cout << float( end_time - begin_time ) /  CLOCKS_PER_SEC << "\n";
    cout << difftime(end_time, begin_time) << "\n";
}