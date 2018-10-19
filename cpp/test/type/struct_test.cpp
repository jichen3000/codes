#include <iostream>
using namespace std;

struct NodeValues {
    int val;
    int count;
    NodeValues(int x) : val(x), count(0) {}
};

int main(int argc, char const *argv[])
{
    NodeValues nv = NodeValues(3);
    cout << nv.val << ";" << nv.count << endl;
    return 0;
}

