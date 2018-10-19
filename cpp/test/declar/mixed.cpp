#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
    /* code */
    int i = 1;
    cout << (i+1.0) << endl;
    cout << (1.0+1.0) << endl;

    double d1 = 2.3;
    double d2 {2.3};
    cout << d2 << endl;

    auto d3 {2.3};
    cout << d3 << endl;

    const auto d4 {2.3};
    cout << d4 << endl;

    constexpr double sum(const vector<double>&); 
    vector<double> v {1.2, 3.4, 4.5}; 
    const double s1 = sum(v);
    // constexpr double s2 = sum(v);
    cout << s1 << endl;
    return 0;
}