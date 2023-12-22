// 380) Insert Delete GetRandom O(1) 

#include <map>
#include <vector>
#include <iostream>
using namespace std;

class RandomizedSet {
    map<int, int> randomizedSet;
    vector<int> v; 
public:
    RandomizedSet() {

    }
    
    bool insert(int val) {
        if (randomizedSet.find(val) == randomizedSet.end()) {
            v.push_back(val);
            randomizedSet[val] = v.size() - 1;
            return true;
        }
        return false;
    }
    
    bool remove(int val) {
        if (randomizedSet.find(val) == randomizedSet.end()) {
            return false;
        }else {
            int idx = randomizedSet[val];
            swap(v[idx], v[v.size() - 1]);
            v.pop_back();
            randomizedSet[v[idx]] = idx;
            randomizedSet.erase(val);
            return true;
        }
    }
    
    int getRandom() {
        if (v.size() == 0) return 0;
        int ran = rand()%v.size();
        return v[ran];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
