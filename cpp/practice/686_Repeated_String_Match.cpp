#include <iostream>
#include <vector>
#include <string>
using namespace std;
//A = "abcd" and B = "cdabcdab"

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

class Solution {
public:
    int repeatedStringMatch_slow(string s1, string s2) {
        string new_s = s1;
        int res = 1;
        while (new_s.length() < s2.length()){
            new_s += s1;
            res += 1;
        }
        int i = 0;
        while (i < 3 and new_s.find(s2)==string::npos){
            new_s += s1;
            i += 1;
        }
        // cout << i << endl;
        if (i == 3)
            return -1;
        return res + i;
    }
    int repeatedStringMatch(string s1, string s2) {
        vector<int> lps = get_lps(s2);
        string new_s = s1;
        int i = 0, j = 0, res = 1;
        while (j<s2.length()) {
            if (i == new_s.length()){
                new_s += s1;
                res++;
                // cout << j << "," <<res << endl;
                if (res > (s2.length()/s1.length() + 2)){
                    return -1;
                }
            }
            if (new_s[i]==s2[j]){
                i++,j++;
            } else {
                if (j>0){
                    j = lps[j-1];
                } else {
                    i++;
                }
            }

        }
        return res;
    }
};


int main(int argc, char const *argv[])
{
    /* code */
    Solution s {Solution()};
    // vector<int> digits {1,2,3};
    string a = "abcd";
    string b = "cdabcdab";
    cout << s.repeatedStringMatch(a, b) << endl;
    return 0;
}