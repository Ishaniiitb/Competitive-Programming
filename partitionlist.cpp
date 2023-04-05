//https://leetcode.com/problems/partition-list/description/

#include<iostream>;
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* left=new ListNode();
        ListNode* right= new ListNode();
        ListNode* ptr=right;
        ListNode* ptr1=left;
        ListNode*curr=head;
        while(curr){
            if(curr->val>=x){
                ptr->next=new ListNode(curr->val);
                ptr=ptr->next;
            }
            else{
                ptr1->next=new ListNode(curr->val);
                ptr1=ptr1->next;
            }
            curr=curr->next;
        }
        ptr1->next=right->next;
        
        return left->next;
    }
};