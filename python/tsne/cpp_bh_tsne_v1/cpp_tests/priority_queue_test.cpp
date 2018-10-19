#include <cstdio>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <functional>

template< class T >
void pq(std::priority_queue<T> the_array){
    std::cout << "data: ";
    for (size_t i = 0; i < the_array.size(); i++) {
        std::cout << the_array[i]<<", ";
    }
    std::cout << std::endl;
}

template< class T1 >
void p(const T1 msg1){
    std::cout  << msg1 << std::endl;
}
template< class T1, class T2>
void p(const T1 msg1, const T2 msg2){
    std::cout  << msg1 << " " << msg2 << std::endl;
}
template< class T1, class T2, class T3>
void p(const T1 msg1, const T2 msg2, const T3 msg3){
    std::cout  << msg1 << " " << msg2 << " " << msg3 << std::endl;
}
template< class T1, class T2, class T3, class T4>
void p(const T1 msg1, const T2 msg2, const T3 msg3, const T4 msg4){
    std::cout  << msg1 << " " << msg2 << " " << msg3 << " " << msg4 << std::endl;
}

template<typename T> void print_queue(T& q) {
    while(!q.empty()) {
        std::cout << q.top() << " ";
        q.pop();
    }
    std::cout << '\n';
}

// An item on the intermediate result queue
struct HeapItem {
    HeapItem( int index, double dist) :
    index(index), dist(dist) {}
    int index;
    double dist;
    bool operator<(const HeapItem& o) const {
        return dist < o.dist;
    }
};

std::ostream& operator<<(std::ostream &the_out, const HeapItem& self) {
    the_out << "HeapItem("<<
            "index=" << self.index << ", "
            "dist=" << self.dist  << ")";
    return the_out;
}

int main(){
    std::priority_queue<int> heap;

    heap.push(1);
    heap.push(8);
    heap.push(5);
    heap.push(6);
    p("heap.size(): ",heap.size());
    p("heap.top(): ", heap.top());
    p("before pop heap.size(): ",heap.size());
    heap.pop();
    p("after pop heap.size(): ",heap.size());
    heap.push(100);
    p("heap.size(): ",heap.size());
    p("heap.top(): ", heap.top());
    p("heap.size(): ",heap.size());
    print_queue(heap);
    p("heap.size(): ",heap.size());

    p("with comparator");
    std::priority_queue<HeapItem> heap2;
    heap2.push(HeapItem(6,13.4));
    heap2.push(HeapItem(5,4.4));
    heap2.push(HeapItem(1,2.2));
    heap2.push(HeapItem(0,0.0));
    heap2.push(HeapItem(9,20.1));
    print_queue(heap2);

}
