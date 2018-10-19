#include <iostream>
#include <iterator>
#include <deque>
#include <sstream>
using namespace std;

string to_str(deque<int> vec){
    ostringstream oss;
    if (!vec.empty()){
        // Convert all but the last element to avoid a trailing ","
        copy(vec.begin(), vec.end()-1,
                ostream_iterator<int>(oss, ","));

        // Now add the last element with no delimiter
        oss << vec.back();
    }  
    return oss.str();  
}

void as_queue(){
    deque<int> q {1,2,3};
    q.push_back(4);
    cout << to_str(q) << endl;
    // int a = q[0];
    int a = q.front();
    cout << a << endl;
    q.pop_front();
    cout << to_str(q) << endl;
}

void as_stack(){
    deque<int> q {1,2,3};
    q.push_back(4);
    cout << to_str(q) << endl;
    int a = q.back();
    cout << a << endl;
    q.pop_back();
    cout << to_str(q) << endl;
}



int main(int argc, char const *argv[])
{
    as_queue();
    as_stack();
    return 0;
}