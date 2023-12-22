// 20) Valid Parentheses
#include <string>
#include <stack>
#include <iostream>
using namespace std; 

#include <stack>
class Solution {
public:
    bool isValid(string s) {
        /* 
        init a stack using #include<stack> [] 
        check if string elements are '(', '{', and '[' (remember order) & store in list
        if elements are ')', '}', ']' pop the last element of list and 
        
        */
        stack<char> st; 
        char ch; 
        
        for (int i=0; i<s.length(); i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                st.push(s[i]); 
                continue; 
            }
            
            if (st.empty()) return false; 
            
            switch (s[i]) {
                case ')':
                    ch = st.top(); 
                    st.pop();
                    if (ch == '[' || ch == '{') {
                        return false; 
                    }
                    break; 
                case ']':
                    ch = st.top(); 
                    st.pop();
                    if (ch == '(' || ch == '{') {
                        return false; 
                    }
                    break; 
                case '}':
                    ch = st.top();
                    st.pop();
                    if (ch == '(' || ch == '[') {
                        return false; 
                    }
                    break; 
                    
            }
            
        }
        
        return st.empty(); 
    }
};
