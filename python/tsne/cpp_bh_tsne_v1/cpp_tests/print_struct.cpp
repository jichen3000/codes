#include <stdlib.h>
#include <stdio.h>
#include <iostream>

// An item on the intermediate result queue
struct HeapItem {
    HeapItem( int index, double dist) :
    index(index), dist(dist) {}
    int index;
    double dist;
    // bool operator<(const HeapItem& o) const {
    //     return dist < o.dist;
    // }
};

std::ostream& operator<<(std::ostream &the_out, const HeapItem& self) {
    the_out << "HeapItem("<<
            "index=" << self.index << ", "
            "dist=" << self.dist  << ")";
    return the_out;
}

int main(){
    HeapItem item=HeapItem(0,3.0);
    std::cout << item << std::endl;
}
