#include <iostream>

#include <string>
#include <list>
using namespace std;

string compose(const string& name, const string& domain){
    return name + '@' + domain;
}

void simple_set(string s){
    cout << s << endl;
    string s1 = s;
    s1 += "bb";
    cout << s << endl;
    cout << s1 << endl;
}

void find_test(){
    string s = "123456";
    string f = "345";
    string n = "745";
    size_t i1 = s.find(f);
    cout << i1 << endl;
    size_t i2 = s.find(n);
    cout << i2 << endl;
    cout << (i1 == string::npos) << endl;
    cout << (i2 == string::npos) << endl;
}

int main(int argc, char const *argv[])
{
    /* code */
    string s {"something, important"};
    cout << s.length() << endl;
    cout << s.size() << endl;
    cout << s << endl;
    string s1(2, '.');
    cout << s1 << endl;

    cout << compose("cheng","com") << endl;

    simple_set("mm");

    find_test();

    cout << s[0] << endl;
    return 0;
}