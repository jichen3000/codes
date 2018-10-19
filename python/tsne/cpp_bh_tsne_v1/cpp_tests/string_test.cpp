#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <queue>
#include <limits>
#include <cmath>
#include <iostream>

size_t layers = 2;
template< class T >
void p(const T msg){
    std::cout << __PRETTY_FUNCTION__ << std::string(layers, ' ') << msg << std::endl;
}

template< class T, class T2>
void p(const T msg, const T2 msg2){
    std::cout  << std::string(layers, ' ') << msg << msg2 << std::endl;
}

template< class T, class T2, class T3>
void p(const T msg, const T2 msg2, const T3 msg3){
    std::cout  << std::string(layers, ' ') << msg << msg2 << msg3 << std::endl;
}


int main(){
    p("mm");
    layers += 2;
    p("ok");
    p(2);
    p(3, ": mm");
}
