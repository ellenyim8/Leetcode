// 22) Generate Parentheses
#include <vector>
#include <string>
#include <iostream>
using namespace std; 

class Solution {
public:
    vector<string> res; 
    vector<string> generateParenthesis(int n) {    
        int open = 1, close = 0; 
        string s = "(";

        createParen(open, close, s, n);
        return res; 
    }

    void createParen(int open, int close, string s, int n) {
        if (s.length() == 2 * n ) {
            res.push_back(s);
            return;
        }

        if (open < n) {
            createParen(open+1, close, s+'(', n);
        }
        if (close < open) {
            createParen(open, close+1, s+')', n);
        }
    }
};
