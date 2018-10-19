#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    /* code */
    const auto a = 1;
    cout << a << "\n";
    cout << typeid(a).name() << "\n";
    // cout << (typeid(a).name() == "i") << "\n";
    return 0;
}