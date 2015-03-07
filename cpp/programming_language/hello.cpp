#include <iostream>
using namespace std;

double square(double x) {
    return x * x;
}

void p(int item) {
    cout << item << endl;
}
void p(double item) {
    cout << item << endl;
}

int main() {
    double x = 5;
    cout << "the square of " << x << " is " << square(x) << endl;
    cout << "size of int: " << sizeof(int) << "\n";
    auto ch = "x";
    auto i = 5;
    cout << "ch: " << ch << "\n";
    cout << "i: " << i << "\n";
    float fValue = 5.5;
    cout << sizeof(fValue) << endl;
    double dValue = 5.5;
    cout << sizeof(dValue) << endl;

    wchar_t* wideString = L"this is a wide string";
    cout << *wideString << endl;

    auto var2 = 2.0;
    cout << var2
}