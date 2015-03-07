#include <iostream>
#include <typeinfo>
using namespace std;

void showSomeTypes() {
    int t = 10;
    int* p = &t;
    int* m = &t;
    int& r = t;
    cout << typeid(p).name() << endl;
    cout << typeid(m).name() << endl;
    cout << typeid(t).name() << endl;
    cout << typeid(r).name() << endl;    
}

void showInt(string name, int value){
    cout << name << " : " << value << endl;
}

void showReference() {
    int t = 10;
    int* p = &t;
    int& r = t;

    showInt("t", t);
    showInt("*p", *p);
    showInt("r", r);

    t =4;
    showInt("t", t);
    showInt("*p", *p);
    showInt("r", r);

    *p =5;
    showInt("t", t);
    showInt("*p", *p);
    showInt("r", r);

    r = 6;
    showInt("t", t);
    showInt("*p", *p);
    showInt("r", r);




}

int main(int argc, char const *argv[])
{   
    showReference();
    return 0;
}