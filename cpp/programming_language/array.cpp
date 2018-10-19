#include <iostream>
using namespace std;

void basic_array() {
    int v[] = {1,2,3,4}; // array cannot be auto
    for (auto x : v) {
        cout << x << "\n";
    }
    for (auto& i : v) {
        cout << i << "\n";
    }
}

int count_x(char* p, char x) {
    if (p==nullptr) return 0;
    int count = 0;
    for (; *p != 0; ++p)
        if (*p == x)
            ++count;
    return count;
}

int main() {
    basic_array();
}