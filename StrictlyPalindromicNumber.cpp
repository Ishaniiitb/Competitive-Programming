//https://leetcode.com/problems/strictly-palindromic-number/

#include <iostream>;
#include <vector>;
using namespace std;


class Solution {
public:
    bool isStrictlyPalindromic(int n) {
        vector <int> v1;
        vector <int> v2;
        int a;
        for(int i=2;i<=n-2;i++){
            a=n;
            while(a!=(a%i)){
                v1.push_back(a%i);
                v2.push_back(a%i);
                a=a-(a%i);
                a=a/i;
            }
            v1.push_back(a);
            v2.push_back(a);
            if (palindrome(v1,v2)==0){
                return false;
            }
            for(int i=0;i<v1.size();i++){
                cout << v1[i]<<" ";
            }
            cout <<endl;
            v1.clear();
            v2.clear();
        }
        return true;
    }
    int palindrome(vector <int> v1,vector<int>v2){
        reverse(v2.begin(),v2.end());
        for(int i=0;i<v1.size();i++){
            if (v1[i]!=v2[i]){
                return 0;
            }
        }
        return 1;
    }
};