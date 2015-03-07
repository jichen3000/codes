#include <iostream>
using namespace std;

int add(int n1, int n2=0){
    return n1 + n2;
}

int main(int argc, char const *argv[])
{
    /* code */
    cout << "add: " << add(1) << endl;
    cout << "add: " << add(1, 3) << endl;
    return 0;
}