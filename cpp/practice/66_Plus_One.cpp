#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // vector<int> plusOne(vector<int>& digits) {
    //     for(int i = digits.size()-1; i>=0; --i){
    //         if(digits[i]==9){
    //             digits[i] = 0;
    //         } else {
    //             digits[i]++;
    //             return digits;
    //         }
    //     }
    //     digits[0] = 1;
    //     digits.push_back(0);
    //     return digits;
    // }
    vector<int> plusOne(vector<int>& digits) {
        // i-- will exe before the block
        // digits[i] = 0 will exe after the block
        for (int i=digits.size(); i--; digits[i] = 0)
            if (digits[i]++ < 9)
                return digits;
        digits[0]++;
        digits.push_back(0);
        return digits;
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
    vector<int> digits {1,2,3};
    for(int i = digits.size(); i; --i){
        cout << i << endl;
    }
    // vector<int> digits {9};
    vector<int> res = s.plusOne(digits);
    pv(res);
    return 0;
}