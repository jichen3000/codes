#include <iostream>
#include <vector>
using namespace std;
//A = "abcd" and B = "cdabcdab"


class Solution {
public:
    int repeatedStringMatch(string str1, string str2) {
        
    }
};


void pv(vector<int>& v){
    for(auto i : v){
        cout << i << ",";
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    /* code */
    Solution s {Solution()};
    // vector<int> digits {1,2,3};
    vector<int> digits {9};
    vector<int> res = s.plusOne(digits);
    pv(res);
    return 0;
}