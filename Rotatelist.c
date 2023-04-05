//https://leetcode.com/problems/rotate-list/description/

#include<stdio.h>;
#include<stdlib.h>;

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* rotateRight(struct ListNode* head, int k){
    int count=0;
    struct ListNode*temp=head;
    struct ListNode*temp1=head;
    struct ListNode*temp2=head;
    struct ListNode*temp3=head;
    while(temp!=NULL){
        temp=temp->next;
        count=count+1;
    }
    printf("%d",count);
    if (count==0){
        head=NULL;
        return head;
    }
    else if (count==1){
        return head;
    }
    while(temp2->next!=NULL){
        temp2=temp2->next;
    }
    if (count>1){
        if(k==0){
            return head;
        }
        else if (k>0){
            if (k>count){
                k=k%count;
            }
            if (k%count==0){
                return head;
            }
            int rev=count-1-k;
            for(int i=0;i<rev;i++){
                temp1=temp1->next;
            }
            //printf("%d",temp1->val);
            temp3=temp1->next;
            temp1->next=NULL;
            temp2->next=head;
            head=temp3;
        }   
    }
    return head;
}