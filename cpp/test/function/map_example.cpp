#include <functional>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <iostream>
 
int main()
{
    std::vector<std::string> v = {"once", "upon", "a", "time"};
    std::transform(v.begin(), v.end(),
                   std::ostream_iterator<std::size_t>(std::cout, " "),
                   std::mem_fun_ref(&std::string::size));
}