#include <iostream>
#include <string>
#include <initializer_list>

template <typename T>;
void func(T t){
    std::cout << t << std::endl;
}

// recursive variadic function
template<typename T, typename... Args>;
void func(T t, Args... args) {
    std::cout << t <<std::endl;

    func(args...);
}

template <class T>;
void func2(std::initializer_list<T> the_list){
    for( auto elem : the_list )
    {
        std::cout << elem << std::endl;
    }
}

int main(){
    std::string
        str1( "Hello" ),
        str2( "world" );

    func(1,2.5,'a',str1);

    // func2({10, 20, 30, 40});
    // func2({str1, str2});
}
