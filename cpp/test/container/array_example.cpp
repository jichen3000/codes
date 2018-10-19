// http://www.cplusplus.com/doc/tutorial/arrays/
// http://www.cplusplus.com/reference/array/array/

#include <iostream>
using namespace std;

void show_array_fun(int arg[])

int main(int argc, char const *argv[])
{
    /* code */
    const int arr1 [5] = {1,2,3,4,5};
    for(int item : arr1){
        cout << item <<"\n";       
    }
    cout << "show max size" << "\n";
    int arr2 [5] = {1,2,3};
    arr2[4] = 10;
    for(int item : arr2){
        cout << item <<"\n";       
    }
    cout << "show auto size" << "\n";
    const int arr3 [] = {1,2,3};
    for(int item : arr2){
        cout << item <<"\n";       
    }
    cout << "two mensions" << "\n";
    int m = 3, n = 4;
    int arr4 [m][n];
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            arr4[i][j] = i * n + j;
        }
    }
    // for(int item [] : arr4){
    //     cout << item << "\n";
    // }
    return 0;
}