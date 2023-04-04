//https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

#include<vector>;
#include<algorithm>;
using namespace std;
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        sort(nums.begin(),nums.end()); //sorts the array in ascending order
        int length=nums.size();
        return (nums[length-1]-1) *(nums[length-2]-1);
    }
};