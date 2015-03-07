#include <iostream>
using namespace std;

// int* returnLocalVariable(void){
//     int localInt;
//     return &localInt;
// }

// void showPointScape(){
//     int* nPointer;
//     nPointer = returnLocalVariable();
//     // warning: address of stack memory associated with local variable 'localInt' returned
//     *nPointer = 10;
// }

int* returnLocalVarialFromHeap(){
    // allocate heap memory for it.
    int* localInt = new int;
    return localInt;
}

void showRightWayUsingHeap(){
    int* nPointer;
    nPointer = returnLocalVarialFromHeap();
    *nPointer = 10;
    // make sure to delete it.
    delete nPointer;

    int* nArray = new int[10]; 
    nArray[0] = 0;
    delete[] nArray;
}

int main(int argc, char const *argv[])
{
    // showPointScape();
    showRightWayUsingHeap();
    return 0;

}