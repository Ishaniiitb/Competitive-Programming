//https://leetcode.com/problems/array-partition/

#include<vector>;
using namespace std;
#include<algorithm>;
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int a=nums.size();
        int b=a/2;
        vector<int>v;
        for(int i=a-2;i>-1;i=i-2){
            v.push_back(nums[i]);
        }
        int sum=0;
        for(int i=0;i<v.size();i++){
            sum=sum+v[i];
        }
        return sum;
    }
};