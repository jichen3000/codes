#include <iostream>

using namespace std;

void pointer_arithmetic(){
    int a = 5;
    int b = 6;
    int* p = &a;

    cout << "p  : " << p <<endl;
    cout << "p+1: " << p+1 <<endl;
    cout << "size of int: " << sizeof(int) << endl;
    cout << "value of p    : " << *p <<endl;
    cout << "value of p + 1: " << *(p+1) <<endl;

}

int main(int argc, char const *argv[])
{
    int a;
    int *p;
    cout << "p: " << p <<endl;
    // cout << "value of p: " << *p <<endl;

    p = &a;
    cout << "p: " << p <<endl;
    cout << "address of a: " << &a <<endl;
    cout << "value of p: " << *p <<endl;
    cout << "value of a: " << a <<endl;

    *p = 12; // derefrencing
    cout << "value of p: " << *p <<endl;
    cout << "value of a: " << a <<endl;

    int b = 20;
    *p = b;
    cout << "p: " << p <<endl;
    cout << "value of p: " << *p <<endl;
    cout << "value of a: " << a <<endl;
    cout << "address of b: " << &b <<endl;

    int a1 = 5;
    int* p1 = &a1; // better to understand

    pointer_arithmetic();
    return 0;
}