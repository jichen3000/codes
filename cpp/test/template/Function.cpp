#include <iostream>
using namespace std;

template <class T> T maximum(T t1, T t2){
    return (t1 > t2) ? t1 : t2;
}

int main(int argc, char const *argv[])
{
    cout << maximum(1,2) << endl;
    cout << maximum(1.15,2.5) << endl;
    // report error
    // cout << maximum(1,2.5) << endl;
    return 0;
}