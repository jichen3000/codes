#include "Simple.h"

void SavingsAccount::outsideDefinedFunc(){
    cout << __func__ << endl;
}

int main(int argc, char const *argv[])
{
    SavingsAccount colinAccount;
    colinAccount.accountNumber = 123;
    colinAccount.balance = 0.0;
    // cout << colinAccount << endl;

    colinAccount.showOutside();
    colinAccount.outsideDefinedFunc();

    cout << "array of class" << endl;

    SavingsAccount savingsArray[10];
    savingsArray[4].accountNumber = 345;
    cout << savingsArray[4].accountNumber << endl;

    SavingsAccount* saveingsPointer = &savingsArray[4];
    cout << saveingsPointer->accountNumber << endl;
    // (this doesn't work), because it equals *(saveingsPointer.accountNumber)
    // *saveingsPointer.accountNumber = 3;
    cout << (*saveingsPointer).accountNumber << endl;
    return 0;
}

