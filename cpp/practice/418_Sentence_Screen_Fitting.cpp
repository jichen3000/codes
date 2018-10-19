#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

template <template<class, class> class V, class T, class A>
string to_string(V<T,A> c_list) {
    std::ostringstream oss;
    if (!c_list.empty()) {
        std::copy(c_list.begin(), c_list.end()-1,
                std::ostream_iterator<T>(oss, ","));
        oss << c_list.back();
    }
    return oss.str();
}

class Solution{
public:
    int wordsTyping(vector<string>& sentence, int rows, int cols) {
        // cout << to_string(sentence) <<endl;
        int res = 0, k = 0, j=0;
        int all_len = sentence.size();
        for(auto& s : sentence)
            all_len += s.size();
        for(int i=0; i < rows; i++){
            j = cols;
            while (j > 0 && j>=sentence[k].size()){
                if (j >= all_len) {
                    // cout << "b j:" << j;
                    int count = j / all_len;
                    res += count;
                    j -= count * all_len;
                    // cout << " a j:" << j << endl;
                    if (j < sentence[k].size())
                        continue;
                }
                j -= sentence[k].size() + 1;
                k += 1;
                if (k == sentence.size()){
                    k = 0;
                    res += 1;
                    // if(res>=100) return res;
                }
                // cout << "j: " << j << " K:" << k << "  s: " << sentence[k] << sentence[k].size() << (j>=sentence[k].size())<< endl;
            }
        }
        // cout << all_len << endl;
        return res;    
    }
};
int main(int argc, char const *argv[])
{
    Solution s = Solution();
    vector<string> sentence1 {"hello", "world"};
    cout << s.wordsTyping(sentence1, 2, 8) << ":" << 1 << endl;
    vector<string> sentence2 {"f","p","a"};
    cout << s.wordsTyping(sentence2,8,7)<< ":" << 10 << endl;
    // cout << to_string(vector<string> {"hello", "world"}) <<endl;
    // # Solution().wordsTyping(["hello","world"],2,8).must_equal(1)
    // Solution().wordsTyping(["f","p","a"],8,7).must_equal(10)
    // # Solution().wordsTyping(["hello"],10000,1).must_equal(0)
    // # Solution().wordsTyping(["try","to","be","better"],10000,9001).must_equal(5293333)
    // # Solution().wordsTyping(["t"],100,100).must_equal(5000)
    // # Solution().wordsTyping(["aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa","aaaaaaaaaa"],20000,20000).must_equal(363600)
    cout << "end" << endl;
    return 0;
}
// class Solution:
//     def wordsTyping(self, sentence, rows, cols):
//         res, k = 0, 0
//         ls, n = list(map(len, sentence)), len(sentence)
//         all_len = sum(ls) + n
//         # all_len.p()
//         for i in range(rows):
//             j = cols
//             while j >= ls[k]:
//                 if j >= all_len:
//                     count = j // all_len
//                     res += count
//                     j -= count * all_len
//                     if j < ls[k]:
//                         continue
//                     # (n,res,j,k).p()
//                 j -= ls[k] + 1
//                 k += 1
//                 if k == n:
//                     k = 0
//                     res += 1
//         return res
