#include <iostream>
using namespace std;

void outsideFunc(){
    cout << "outsideFunc" << endl;
}

void anotherFunc(){
    cout << __func__ << endl;
}

class SavingsAccount{
public:
    unsigned accountNumber;
    double balance;

    void outsideFunc(){
        cout << "SavingsAccount::outsideFunc" << endl;
        cout << __func__ << endl;
    }

    void showOutside(){
        ::outsideFunc();
        anotherFunc();
        outsideFunc();
        cout << this->balance << endl;
        cout << accountNumber << endl;
    }

    void outsideDefinedFunc();
};

// cannot define in same file
// void SavingsAccount::outsideDefinedFunc(){
//     cout << __func__ << endl;
// }

// int main(int argc, char const *argv[])
// {
//     SavingsAccount colinAccount;
//     colinAccount.accountNumber = 123;
//     colinAccount.balance = 0.0;
//     // cout << colinAccount << endl;

//     colinAccount.showOutside();
//     colinAccount.outsideDefinedFunc();
//     return 0;
// }

