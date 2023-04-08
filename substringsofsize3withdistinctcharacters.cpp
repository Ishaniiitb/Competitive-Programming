#include<iostream>;
#include<string>;
using namespace std;

class Solution {
public:
    int countGoodSubstrings(string s) {
        int count=0;
        if (s.size()>=3){
            for(int i=0;i<s.size()-2;i++){
                if(s[i]!=s[i+1] && s[i+1]!=s[i+2] &&s[i]!=s[i+2]){
                    count=count+1;
                }
            }
        }
        else{
            return 0;
        }
        return count;
    }
};