//https://leetcode.com/problems/top-k-frequent-elements/

// #include<iostream>;
// #include<vector>;
// #include<unordered_map>;
// #include<priority_queue>;
// using namespace std;

// class Solution {
// public:
//     vector<int> topKFrequent(vector<int>& nums, int k) {
//         priority_queue<pair<int,int>>pq;
//         unordered_map<int,int>map;
//         vector<int>v;
//         for(auto it:nums){
//             map[it]++;
//         }
//         for (auto it:map){
//             pq.push({it.second,it.first});
//         }
//         while(k>0 && !pq.empty()){
//             v.push_back(pq.top().second);
//             pq.pop();
//             k--;
//         }
//         return v;
//     }
// };