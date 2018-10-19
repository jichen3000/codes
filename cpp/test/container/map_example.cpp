#include <iostream>
#include <map>
#include <unordered_map>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
    /* code */
    // red black tree
    map<int, string> names {
        {1, "cheng"},
        {2, "evan"}
    };
    cout << names.size() << endl;
    for(auto it: names){
        cout << it.first << " : " << it.second << endl;
    }

    unordered_map<int, string> names2 {
        {1, "cheng"},
        {2, "evan"}
    };
    cout << names2.size() << endl;

    for(auto it: names2){
        cout << it.first << " : " << it.second << endl;
    }
    return 0;
}