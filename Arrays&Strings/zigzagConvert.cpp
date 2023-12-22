// 6) Zigzag conversion

#include <string>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {

        if (s.empty()) return ""; 
        if (numRows <= 1) return s; 

        int k=0, c=1; 
        vector<string> zigzag(numRows); 

        for (int i=0; i<s.size(); i++) {
            zigzag[k].push_back(s[i]);
            if (k == numRows - 1) {
                c = -1; 
            } else if (k == 0) {
                c = 1; 
            }
            k += c; 
        }

        string res; 
        for (auto& z : zigzag) 
            res += z; 
        return res; 
    }
};
