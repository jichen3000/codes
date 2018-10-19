#include <iostream>
#include <string>
#include <vector>
// #include <assert.h>
#define CATCH_CONFIG_MAIN
#include "catch.hpp"

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

TEST_CASE( "lps", "[factorial]" ) {
    vector<int> a {0,1,2,3};
    REQUIRE( get_lps("aaaa") == a );
}
// void pv(vector<int> v){
//     for(auto i : v){
//         cout << i << ",";
//     }
//     cout << endl;
// }

// int main(int argc, char const *argv[])
// {
//     vector<int> a {0,1,2,3};
//     assert(get_lps("aaaa")==a);
//     a = {0,0,1,2};
//     // cout << get_lps("abab") <<endl;
//     assert(get_lps("abab")==a);
    
//     // assert(get_lps("aaaa")=={0,1,2,3});
//     return 0;
// }