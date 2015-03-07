// TemplateVector - implement a vector that uses a // template type
#include <cstdlib>
#include <cstdio>
#include <iostream> 
#include "TemplateVector.h" 
using namespace std;
// intFn() - manipulate a collection of integers 
void intFn()
{
    // create a vector of integers 
    TemplateVector<int> integers(10);

    // add values to the vector
    for(int i = 0 ; i < 5; i++)
    {
        integers.add(i); 
    }
    cout << "\nHere are the numbers you entered:" << endl; 
    for(int i = 0; i < integers.size(); i++)
    {
        cout << i << ":" << integers.get() << endl;
    } 
}

// Names - create and manipulate a vector of names 
class Name
{
public:
    Name() = default;
    Name(string s) : name(s) {}
    const string& display() { return name; }
protected:
     string name;
};

void nameFn()
{
    // create a vector of Name objects 
    TemplateVector<Name> names(20);

    // add values to the vector
    for(int i = 0 ; i < 5; i++)
    {
        string s="name"+to_string(i);
        names.add(Name(s));
    }
    cout << "\nHere are the names you entered" << endl; 
    for(int i = 0; i < names.size(); i++)
    {
        Name& name = names.get();
        cout << i << ":" << name.display() << endl; 
    }
}

int main(int argc, char const *argv[])
{
    intFn();
    nameFn();
    return 0;
}