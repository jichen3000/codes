#include <iostream>
using namespace std;

int add(int n1, int n2=0){
    return n1 + n2;
}

void showDefaultArgument(){
    cout << "add: " << add(1) << endl;
    cout << "add: " << add(1, 3) << endl;
}

void changeArgument(int n){
    n += 2;
}

void showPassByValueNoSideEffect(){
    int m = 0;
    cout << "before function, m is " << m << endl;
    changeArgument(m);
    cout << "after function, m is " << m << endl;

}

void changeArgumentByReference(int& n){
    n += 2;
}

void showPassByReferenceSideEffect(){
    int m = 0;
    cout << "before function, m is " << m << endl;
    changeArgumentByReference(m);
    cout << "after function, m is " << m << endl;
}

int main(int argc, char const *argv[])
{
    /* code */
    showDefaultArgument();
    showPassByValueNoSideEffect();
    showPassByReferenceSideEffect();
    return 0;
}