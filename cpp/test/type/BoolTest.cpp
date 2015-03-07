#include <iostream>
using namespace std;

int main(int argsSize, char* args[]) {
    // set output format for bool variables 
    // to true and false instead
    // of 1 and 0 
    cout.setf(cout.boolalpha);

    int n1 = 2;
    int n2 = 3;
    bool b;
    b = n1 == n2;

    cout    << "The statement, " << n1 
            << " equals " << n2
            << " is " << b
            << endl;


    // wait until user is ready before terminating program 
    // to allow the user to see the program results
    // cout << "Press Enter to continue..." << endl; 
    // cin.ignore(10, '\n');
    // cin.get();
    return 0;    
            
}