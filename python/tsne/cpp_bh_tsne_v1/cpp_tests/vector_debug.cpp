#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>




template< class T >
void print_vector(std::vector<T> the_array){
    for (size_t i = 0; i < the_array.size(); i++) {
        std::cout << i << " : " << the_array[i] << std::endl;
    }
    std::cout <<"vector finished!"<< std::endl;
}


void vector_swap(){
    size_t size = 5;
    int the_array[10] = {0,1,2,3,4};

    std::vector<int> the_v(the_array,the_array+5);
    print_vector(the_v);
    std::swap(the_v[1], the_v[3]);
    print_vector(the_v);

}


int main(){
    // simple_array();
    // simple_vector();
    // vector_constructor_with_array();
    // vector_swap();
    vector_swap();
}
