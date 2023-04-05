#include<vector>;
#include<iostream>;
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        vector<int>v;
        for(int i=0;i<10;i++){
            cout << n << ' ';
            int a;
            a=next(n);
            n=a;
            //auto it=find(v.begin(),v.end(),a);
            if(a==1){
                return true;
            }
            else{
                v.push_back(a);
            }
        }
        return false;
    }
    int next(int n){
        vector<int>v;
        int a=n;
        int b=10;
        while(a!=(a%b)){
            v.push_back(a%b);
            a=a-(a%10);
            a=a/10;
        }
        v.push_back(a);
        int sum=0;
        for(int i=0;i<v.size();i++){
            //cout << v[i] <<' ';
        }
        //cout << endl;
        for(int i=0;i<v.size();i++){
            sum=sum+(v[i]*v[i]);
        }
        return sum;
    }
};