#include <iostream>
using namespace std;

namespace Colin1{
    void some(){
        cout << "in Colin 1" << endl;
    }
}

namespace Colin2{
    void some(){
        cout << "in Colin 2" << endl;
    }
}

int main(int argc, char const *argv[])
{
    Colin1::some();
    Colin2::some();
    return 0;
}
