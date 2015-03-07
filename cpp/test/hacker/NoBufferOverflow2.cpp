// NoBufferOverflow2 - this program avoids being hacked by 
// using a variable-size buffer 
#include <cstdio>
#include <cstdlib>
#include <fstream> 
#include <iostream> 
#include <cstring> 
#include <string> 
#include <vector>
using namespace std;

// getString - read a string of input from the user prompt 
// and return it to the caller
char* getString(istream& cin)
{
    // create a variable-size buffer with an initial
    // length of 64 characters; however, this buffer can 
    // grow if there are more than 64 characters in the 
    // input file
    vector<char> buffer;
    buffer.reserve(64);
    // now input a string from the file 
    for(;;)
    {
        // read the next character
        char c = cin.get();
        // exit the loop if we read a NULL or EOF 
        if ((c == 0) || cin.eof()) break;
        // add the character to the buffer and grow the 
        // buffer if necessary to accommodate 
        buffer.push_back(c);
    }
    // make sure that the buffer is null terminated 
    buffer.push_back('\0');
    // return a copy of the string to the caller 
    char* pB = new char[buffer.size()];
    if (pB != nullptr) strcpy(pB, buffer.data()); 

    return pB; 
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
    char* pB = getString(c);
    // output what we got
    cout << "\nWe successfully read in:\n" << pB << endl;
    return 0;
}