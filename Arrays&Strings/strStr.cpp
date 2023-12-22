// 28) Find the Index of the First Occurrence in a String

#include <string>
using namespace std;
#include <iostream>

class Solution {
public:
    int strStr(string haystack, string needle) {
        auto index = haystack.find(needle);
        return (int)index; 
    }
};

