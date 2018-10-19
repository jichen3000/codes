#include <iostream>
#include <vector>
#include <deque>
#include <sstream>
#include <string>
using namespace std;

template <template<class, class> class V, class T, class A>
string list_to_str(V<T, A> vec){
    std::ostringstream oss;
    if (!vec.empty()){
        // Convert all but the last element to avoid a trailing ","
        std::copy(vec.begin(), vec.end()-1,
                std::ostream_iterator<T>(oss, ","));

        // Now add the last element with no delimiter
        oss << vec.back();
    }  
    return oss.str();  
}

template <typename A, typename T>
string list_to_str1(T vec){
    std::ostringstream oss;
    if (!vec.empty()){
        // Convert all but the last element to avoid a trailing ","
        std::copy(vec.begin(), vec.end()-1,
                std::ostream_iterator<A>(oss, ","));

        // Now add the last element with no delimiter
        oss << vec.back();
    }  
    return oss.str();  
}


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

int main(int argc, char const *argv[])
{
    cout << vector_str(vector<int> {0,1,2,3}) << endl;
    vector<int> v {0,1,2,3};
    cout << list_to_str1<int>(v) << endl;
    cout << list_to_str(v) << endl;
    cout << list_to_str(deque<int> {0,1,2,3}) << endl;
    cout << list_to_str(deque<string> {"a","b"}) << endl;
    // assert(get_lps("aaaa")=={0,1,2,3});
    return 0;
}