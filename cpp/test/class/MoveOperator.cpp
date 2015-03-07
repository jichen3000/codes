#include <iostream>
using namespace std;

class MyContainer
{
public:
    MyContainer(int nS, const char* pS) : nSize(nS)
    {
        cout << "MyContainer constructor" << endl;
        pString = new char[nSize];
        strcpy(pString, pS); 
    }
    ~MyContainer()
    {
        delete pString;
        pString = nullptr; 
    }
    //copy constructor 
    MyContainer(const MyContainer& s)
    {
        copyIt(*this, s);
    }

    MyContainer& operator=(MyContainer& s)
    {
        delete pString;
        copyIt(*this, s);
        return *this;
    }
    // move constructor 
    MyContainer(MyContainer&& s)
    {
        moveIt(*this, s);
    }
    MyContainer& operator=(MyContainer&& s)
    {
        delete pString;
        moveIt(*this, s);
        return *this;
    }
protected:
    static void moveIt(MyContainer& tgt, MyContainer& src)
    {
        cout << "Moving " << src.pString << endl; 
        tgt.nSize = src.nSize;
        tgt.pString = src.pString; 
        src.nSize = 0;
        src.pString = nullptr;
    }

    static void copyIt( MyContainer& tgt, const MyContainer& src)
    {
        cout << "Copying " << src.pString << endl; 
        delete tgt.pString;
        tgt.nSize = src.nSize;
        tgt.pString = new char[tgt.nSize]; 
        strncpy(tgt.pString, src.pString, tgt.nSize);
    }
    int nSize;
    char* pString;
};

MyContainer fn(int n, const char* pString)
{
    // this is move step one
    // compiler will create a temporary copy.
    MyContainer b(n, pString);
    return b; 
}

int main(int argc, char const *argv[])
{
    MyContainer mc(100, "Original");
    // this is move step tow
    // using move, compiler will give mc that temporary copy
    // if don't use move, compiler will create a copy again.
    mc = fn(100, "Created in fn()");    
    return 0;
}