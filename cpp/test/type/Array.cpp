#include <iostream>
using namespace std;

void showArrayInitialValues(){
    int nArray[5]; // no initialize, could be any value;
    for (int item : nArray){
        cout << item << endl;
    }
    int nArray2[5] = {}; // initialize array to all 0's
    for (int item : nArray2){
        cout << item << endl;
    }
    for (int& item : nArray2){
        cout << item << endl;
    }
}

void show2DArray(){
    int intMatrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
    // for (auto row: intMatrix){
    //     for (auto cell: row){

    //         cout << cell;
    //     }
    //     cout << endl;
    // }
    for (int i = 0; i<2; i++){
        for (int j = 0; j<3; j++){
            cout << intMatrix[i][j];
        }
    }
    cout << endl;
}

void displayArray(int intArray[], int nSize) {
    cout << "The value of the array is:\n";
    // initialize the pointer pArray with the 
    // the address of the array intArray
    int* pArray = intArray;
    for(int n = 0; n < nSize; n++, pArray++) {
        cout << n << ": " << *pArray << endl;
     }
    cout << endl;
}

void showRightWayLoop(){
    int array[] = {4, 3, 2, 1}; 
    displayArray(array, 4);
}

void showString(){
    const char* szString = "colin";
    cout << "szString is: " << szString << endl;
    const char* pointString = szString;
    while(*pointString){
        // cout << *pointString;
        // pointString++;
        cout << *pointString++;
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    showArrayInitialValues();
    show2DArray();
    showRightWayLoop();
    showString();
    return 0;
}