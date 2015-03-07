#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int start;
    bool b;
    char c;
    int n;
    long l;
    long long ll;
    float f;
    double d;
    long double ld;
    int end;



    cout <<  "--- = " << &start << endl;
    cout << "&b =" << &b << endl;
    cout << "&c =" << &c << endl;
    cout << "&n =" << &n << endl;
    cout << "&l =" << &l << endl;
    cout << "&ll=" << &ll << endl;
    cout << "&f =" << &f << endl;
    cout << "&d =" << &d << endl;
    cout << "&ld=" << &ld << endl;
    cout << "---=" << &end << endl;

    cout << "show size: " << endl;
    cout << "sizeof a bool = " << sizeof b <<endl;
    cout << "sizeof a char = " << sizeof c <<endl;
    cout << "sizeof an int = " << sizeof n <<endl;
    cout << "sizeof a long = " << sizeof l <<endl;
    cout << "sizeof a long long  = " << sizeof ll <<endl;
    cout << "sizeof a float = " << sizeof f <<endl;
    cout << "sizeof a double = " << sizeof d <<endl;
    cout << "sizeof a long double = " << sizeof ld <<endl;
    cout << "end." << endl;
    return 0;
}