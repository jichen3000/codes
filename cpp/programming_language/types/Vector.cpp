#include "Vector.h" // get the interface
#include <stdexcept>
using namespace std;

Vector::Vector(int s)
:elem{new double[s]}, sz{s}{ 
}

// Vector::Vector(std::initializer_list<double> lst) // initialize with a list 
//     :elem{new double[lst.size()]}, sz{lst.size()}
// {
//     copy(lst.begin(),lst.end(),elem); // copy from lst into elem
// }


double& Vector::operator[](int i) {
    if (i<0 || size()<=i) throw out_of_range{"Vector::operator[]"};
    return elem[i]; 
}

int Vector::size() {
    return sz; 
} 