#include <iostream>
#include <vector>

using namespace std;

template <template<class, class> class V, class T, class A>
void f(V<T, A> &v) {
    // This can be "typename V<T, A>::value_type",
    // but we are pretending we don't have it

    T temp = v.back();
    v.pop_back();
    // Do some work on temp

    std::cout << temp << std::endl;
}

template <class Cont>
void f1(Cont v) {

    auto temp = v.back();
    v.pop_back();
    // Do some work on temp

    std::cout << temp << std::endl;
}

template <class T> T maximum(T t1, T t2){
    return (t1 > t2) ? t1 : t2;
}

int main(int argc, char const *argv[])
{
    cout << maximum(1,2) << endl;
    cout << maximum(1.15,2.5) << endl;

    vector<int> v {1,2,3};
    f(v);
    f<std::vector, int>(v);
    f1(v);
    f1(vector<int> {1,2,3,4});
    // report error
    // cout << maximum(1,2.5) << endl;
    return 0;
}