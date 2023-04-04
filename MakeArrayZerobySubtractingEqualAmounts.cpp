//https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

#include<vector>;
#include<unordered_set>;
#include<algorithm>;
using namespace std;
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_set <int>s;
        for(int i=0;i<nums.size();i++){
            if (nums[i]>0){
                s.insert(nums[i]);
            }
        }
        return s.size();
    }
};