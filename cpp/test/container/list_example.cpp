#include <iostream>
#include <list>
#include <string>

using namespace std;



int main(int argc, char const *argv[])
{
    /* code */
    list<string> l {"1", "2", "3"};
    cout << l.size() << endl;
    for (auto s : l){
        cout << s << endl;
    }
    return 0;
}