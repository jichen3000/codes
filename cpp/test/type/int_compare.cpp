#include <iostream>
#include <string>
#include <vector>
#include <sstream>
// #include "mini_test.h"
using namespace std;

int main(int argc, char const *argv[])
{
    int a = -1;
    string b = "123";
    cout << (a >= 0) << endl;
    cout << b.size() << endl;
    cout << (a >= 3) << endl;
    cout << (a >= b.size()) << endl;
    return 0;
}