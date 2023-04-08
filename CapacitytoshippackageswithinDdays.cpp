//https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

#include<iostream>;
#include<vector>;
#include<algorithm>;
#include<numeric>;
using namespace std;

class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int b=*max_element(weights.begin(),weights.end());
        int c=std::accumulate(weights.begin(),weights.end(),0);
        while(b<c){
            int m=(c+b)/2;
            if(func(weights,m,days)){
                c=m;
            }
            else{
                b=m+1;
            }
        }
        return b;
    }
    int func(vector<int>&weights,int cap,int days){
        int count=0;
        int i=0;
        int a=0;
        while(i<weights.size()){
            a=a+weights[i];
            if (a>cap){
                a=0;
                count=count+1;
            }
            else if (a==cap){
                a=0;
                count=count+1;
                i++;
            }
            else if (a<cap && i!=weights.size()-1){
                i++;
            }
            else{
                i++;
                count=count+1;
            }
        }
        if (count<=days){
            return 1;
        }
        return 0;
    }
};