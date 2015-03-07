#include "Vector.h" 
#include <cmath> 
#include <iostream>
using namespace std;


int main(){
    int int_arr[] = {1,2,3};
    Vector v(3); // make a vector of s elements 
    for (int i = 0; i < 3; i++){
        cout << int_arr[i];
    }
    try {
        cout << v[4];
    } catch (out_of_range){
        cout << "out_of_range\n";
    }
    // cout << v << "\n";

}