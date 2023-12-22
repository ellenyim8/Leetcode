// 12) Integer to Roman

#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    const int val[13] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}; 
    const string roman[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}; 
    string intToRoman(int num) {
        string out = "";

        for (int i=0; num; i++) {
            while (num >= val[i]) out += roman[i], num -= val[i]; 
        }

        return out;
    }
};

/*  
// base cases: 
num = 1 return "I"
num = 5 return "V"
num = 10 return "X"
num = 50 return "L"
num = 100 return "C"
num = 500 return "D"
num = 1000 return "M"

1001 => return "IM"
*/
