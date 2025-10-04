#include <unordered_set>

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        std::unordered_set<int> found;
        for (int i=0; i<nums.size()+1; i++){
            found.insert(i);
        }

        for (int i=0; i<nums.size(); i++){
            found.erase(nums[i]);
        }
        for (int x : found) { 
            return x ;
            }
        return -1;
    }
};