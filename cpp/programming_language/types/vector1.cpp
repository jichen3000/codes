#include <iostream>
using namespace std;

struct VectorStruct {
    int size; // number of elements
    double* elem; // pointer to elements 
};

void vector_struct_init(VectorStruct& v, int size) {
    v.elem = new double[size]; // allocate an array of size doubles
    v.size = size; 
}

class Vector { 
public:
    Vector(int s) :elem{new double[s]}, sz{s} { } // construct a Vector
    double& operator[](int i) { return elem[i]; } // element access: subscripting
    int size() { return sz; }
private:
    double* elem; // pointer to the elements 
    int sz; // the number of elements
};

double read_and_sum(int s) {
    Vector v(s); // make a vector of s elements 
    for (int i=0; i!=v.size(); ++i)
        cin>>v[i]; // read into elements

    double sum = 0;
    for (int i=0; i!=v.size(); ++i)
        sum+=v[i]; // take the sum of the elements 
    return sum;
}


int main(){
    // cout << read_and_sum(6) << "\n";

    enum class Color { red, blue, green };
    enum class TrafficLight { green, yellow, red };

    Color col = Color::red;
    TrafficLight light = TrafficLight::red;

    cout << int(col) << "\n";
    cout << int(light) << "\n";
}