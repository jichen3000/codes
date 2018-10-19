#include <iostream>
#include <string>
#include <vector>
#include <sstream>
// #include "mini_test.h"
using namespace std;

vector<int> get_lps(string s){
    vector<int> lps {};
    if (s.length()==0) return lps;
    lps.push_back(0);
    int i = 0, j = 1;
    while (j < s.length()){
        if (s[i] == s[j]){
            lps.push_back(j);
            i++, j++;
        } else {
            if (j>0) {
                j = lps[j-1];
            } else {
                i++;
                lps.push_back(0);
            }
        }
    }
    return lps;
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
    vector<int> expect {0,1,2,3};
    vector<int> actual = get_lps("aaaa");
    cout << vector_str(expect) << endl;
    cout << vector_str(actual) << endl;
    // assert(get_lps("aaaa")=={0,1,2,3});
    return 0;
}