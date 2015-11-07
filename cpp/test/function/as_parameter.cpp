#include <iostream>
using namespace std;

typedef void (* vFunctionCall)(int int_arg);

void AcceptVoidFunction(const int int_arg, const vFunctionCall print_int){
    cout << "in AcceptVoidFunction" << endl;
    print_int(int_arg);
}

void PrintInt(int int_arg){
    cout << "the int is: " << int_arg << endl;
}

int main(int argc, char const *argv[]){
    AcceptVoidFunction(2, PrintInt);
    AcceptVoidFunction(3, PrintInt);
    return 0;
}