#include <iostream>
#include <vector>
#include <iterator>
#include <sstream>
using namespace std;

//https://www.codeguru.com/cpp/cpp/cpp_mfc/stl/article.php/c4027/C-Tutorial-A-Beginners-Guide-to-stdvector-Part-1.htm
// consider vector first than array

string vector_str(vector<int> vec){
    std::ostringstream oss;
    if (!vec.empty()){
        // Convert all but the last element to avoid a trailing ","
        std::copy(vec.begin(), vec.end()-1,
                std::ostream_iterator<int>(oss, ","));

        // Now add the last element with no delimiter
        oss << vec.back();
    }  
    return oss.str();  
}

void static_size(){
    cout << "static_size\n";
    size_t size = 10;
    vector<int> v(size);
    for (int i = 0; i < size; ++i){
        v[i] = i+1;
    }
    cout << "size: " << v.size() << endl;
}

void at_will_check(){
    cout << "at_will_check\n";
    vector<int> v;
    try{
        v.at(1000) = 0;
    } catch(out_of_range o) {
        cout <<"Error: " << o.what() << endl;
    }
}

// template <typename T> 
// void print_vector(vector<T>  & the_v){
//     for (vector<T>::iterator i = the_v.begin(); i != the_v.end(); ++i){
//         cout << *i << endl;
//     }
// }

void dynamic_size(){
    vector<int> v;
    size_t count = 10;
    for (int i = 0; i < count; ++i){
        v.push_back(i);
    }
    for (std::vector<int>::iterator i = v.begin(); i != v.end(); ++i){
        cout << *i <<endl;
    }
    cout << "size: " << v.size() << endl;    
}

void reserve(){
    std::vector<int> array;
    int i = 999;          // some integer value
    array.reserve(10);    // make room for 10 elements
    array.push_back(i);
    std::cout<<array.capacity()<<std::endl;
    std::cout<<array.size()<<std::endl;    
    std::cout<<array.max_size()<<std::endl;    
}
int main(int argc, char const *argv[]){
    /* code */
    // typedef std::vector<int> int_vec_t; 
    // not using
    // #define int_vec_t std::vector<int> ;    // very poor style!
    // static_size();
    // at_will_check();
    // dynamic_size();
    dynamic_size();
    return 0;
}