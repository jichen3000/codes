#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char const *argv[])
{
    string fileName = "example.txt";
    ofstream theFile(fileName);
    theFile << "Stephen Davis is suave and handsome\n"
            << "and definitely not balding prematurely"
            << endl;

    // ifstream* fileStream = nullptr;
    // fileStream = new ifstream(fileName);
    // if(fileName->good()){
    //     fileStream->seekg(0);
    //     cerr << "Successfully opened "<< fileName << endl;
    // } else {
    //     delete fileStream;
    // }

    return 0;
}