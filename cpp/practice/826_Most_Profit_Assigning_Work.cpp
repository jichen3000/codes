#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

template <template<class, class> class V, class T, class A>
string to_string(V<T, A> c_list){
    ostringstream oss;
    if (!c_list.empty()){
        std::copy(c_list.begin(), c_list.end()-1,
                ostream_iterator<T>(oss, ","));
        oss << c_list.back();
    }
    return oss.str();
}
struct DP{
    int d;
    int p;
    DP(int td, int tp) : d(td), p(tp) {}
    DP() : d(0), p(0) {}
    // bool operator(DP dp1, DP dp2){
    //     return (dp1.d < dp2.d);
    // }
};

class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        std::vector<DP> dp_v(difficulty.size());
        for (int i=0; i < difficulty.size(); i++){
            // dp_v[i] = DP(difficulty[i], profit[i]);
            // cout << difficulty[i] << " : " << profit[i];
            // DP v = DP(difficulty[i], profit[i]);
        }
        return 0;

    }
};
int main(int argc, char const *argv[])
{
    /* code */
    // vector<string> sentence1 {"hello", "world"};
    // cout << to_string(sentence1) << endl;
    // cout << sentence1[1] << endl;
    std::vector<DP> dp_v(3);
    dp_v[1] = DP(1,2);
    return 0;
}