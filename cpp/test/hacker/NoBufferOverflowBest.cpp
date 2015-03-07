// NoBufferOverflow3 - this program avoids being hacked by 
// using the string class
#include <cstdio>
#include <cstdlib>
#include <fstream> 
#include <iostream> 
#include <string>
using namespace std;
// getString - read a string of input from the user prompt 
// and return it to the caller. Terminate the 
// string at a null or the end-of-file
string getString(istream& cin)
{
    string s;
    getline(cin, s, '\0');
    return s; 
}

int main(int argc, char const *argv[])
{
    // get the name of the file to read
    cout <<"This program reads input from an input file\n"
    "Enter the name of the file:"; 
    string sName;
    cin >> sName;
    // open the file
    ifstream c(sName.c_str());
    if (!c)
    {
        cout << "\nError opening input file" << endl;
        exit(-1); 
    }
    // read the file's content into a string 
    string pB = getString(c);
    // output what we got
    cout << "\nWe successfully read in:\n" << pB << endl;
    return 0;
}