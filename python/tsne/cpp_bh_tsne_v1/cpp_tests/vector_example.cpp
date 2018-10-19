// http://www.codeguru.com/cpp/cpp/cpp_mfc/stl/article.php/c4027/C-Tutorial-A-Beginners-Guide-to-stdvector-Part-1.htm
#include <cstdio>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>

// never using this directive on any header file.
// it would bloat the entire namespace std into each cpp file.
// using namespace std;

void print_int_array(int *the_array, size_t size){
    for (size_t i = 0; i < size; i++) {
        std::cout << the_array[i] << "\t";
    }
    std::cout << std::endl;
}

template< class T >
void print_array(T& the_array, size_t size){
    for (size_t i = 0; i < size; i++) {
        std::cout << the_array[i] << "\t";
    }
    std::cout << std::endl;
}

template< class T >
void print_vector(std::vector<T> the_array){
    for (size_t i = 0; i < the_array.size(); i++) {
        // printf("%i\t",the_array[i]);
        std::cout << i << " : " << the_array[i] << std::endl;
    }
    std::cout <<"vector finished!"<< std::endl;
    // printf("\n");
}

void simple_array(){
    size_t size = 10;
    int sarray[10];
    int *darray = new int[size];
    for (size_t i = 0; i < size; i++) {
        sarray[i]=i;
        darray[i]=i*10;
    }
    print_int_array(sarray,size);
    print_int_array(darray,size);
    delete[] darray;
}

void simple_vector(){
    size_t size = 10;
    std::vector<int> the_v(size);
    size_t v_capacity = the_v.capacity();
    for (size_t i = 0; i < v_capacity; i++) {
        the_v[i]=i*10;
        // the_v.push_back(i*10);
    }
    print_vector(the_v);
    print_int_array(&the_v[0],size);
    std::cout << the_v.size() << std::endl;
    std::cout << the_v.capacity() << std::endl;

    // no need to delete
}

void vector_constructor_with_array(){
    size_t size = 10;
    int the_array[10];
    for (size_t i = 0; i < size; i++) {
        the_array[i]=i;
    }
    print_array(the_array, size);

    std::vector<int> the_v(the_array,the_array+5);
    // print_array(&the_v[0],the_v.size());
    print_vector(the_v);

}

void vector_swap(){
    size_t size = 5;
    int the_array[10] = {0,1,2,3,4};
    print_array(the_array, size);

    std::vector<int> the_v(the_array,the_array+5);
    print_vector(the_v);
    std::swap(the_v[1], the_v[3]);
    print_vector(the_v);

}

bool int_compare (int i,int j) { return (i<j); }

// STL中的nth_element()方法的使用 通过调用nth_element(start, start+n, end)
// 方法可以使第n大元素处于第n位置（从0开始,其位置是下标为 n的元素），
// 并且比这个元素小的元素都排在这个元素之前，比这个元素大的元素都排在这个元素之后，
// 但不能保证他们是有序的
// Rearranges the elements in the range [first,last), in such a way that the element
// at the nth position is the element that would be in that position in a sorted sequence.

// The other elements are left without any specific order,
// except that none of the elements preceding nth are greater than it,
// and none of the elements following it are less.

// The elements are compared using operator< for the first version, and comp for the second.
void vector_nth () {
    std::vector<int> the_v;

    // set some values:
    for (int i=1; i<10; i++) the_v.push_back(i);   //1 2 3 4 5 6 7 8 9
    print_vector(the_v);

    std::random_shuffle(the_v.begin(), the_v.end());
    std::cout << "random_shuffle" << std::endl;
    print_vector(the_v);

    // using default comparison (operator <):
    // n = 5, but since index start from 0, so the n+1 element is 6
    std::nth_element (the_v.begin(), the_v.begin()+5, the_v.end());
    std::cout << "nth_element1" << std::endl;
    print_vector(the_v);

    // using function as comp
    std::nth_element (the_v.begin(), the_v.begin()+5, the_v.end());
    // std::nth_element (the_v.begin(), the_v.begin()+5, the_v.end(),int_compare);
    std::cout << "nth_element2" << std::endl;
    print_vector(the_v);

    std::nth_element (the_v.begin(), the_v.begin()+5, the_v.end());
    // std::nth_element (the_v.begin(), the_v.begin()+5, the_v.end(),int_compare);
    std::cout << "nth_element3" << std::endl;
    print_vector(the_v);

    std::nth_element (the_v.begin(), the_v.begin()+5, the_v.end());
    // std::nth_element (the_v.begin(), the_v.begin()+5, the_v.end(),int_compare);
    std::cout << "nth_element4" << std::endl;
    print_vector(the_v);

}

void vector_nth_partially () {
    // size_t size = 10;
    // std::vector<int> the_v;

    // set some values:
    // int the_array[10] = {0,1,6,3,1,2,2,5,4,3};
    int the_array[10] = {4,5,7,3,6,0,1,2,9,8};
    print_array(the_array, 10);

    std::vector<int> the_v(the_array,the_array+10);
    print_vector(the_v);

    std::nth_element (the_v.begin()+0, the_v.begin()+5, the_v.begin()+10);
    std::cout << "nth_element1" << std::endl;
    print_vector(the_v);
}
int main(){
    // simple_array();
    // simple_vector();
    // vector_constructor_with_array();
    // vector_swap();
    // vector_nth();
    vector_nth_partially();
}
