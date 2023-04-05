#include<stdlib.h>;
#include<stdio.h>;
struct ListNode {
    int val;
    struct ListNode *next;
 };
 
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode*temp=head;
    struct ListNode*temp1=head;
    struct ListNode*temp2=head;
    int count=1;
    while(temp->next!=NULL){
        temp=temp->next;
        count=count+1;
    }
    if(count==1){
        head=NULL;
    }
    else{
        int req=count-n;
        for(int i=0;i<req-1;i++){
            temp1=temp1->next;
        }
        if (req<1){
            head=head->next;
        }
        else{
            temp2=temp1->next;
            temp1->next=temp2->next;
            free (temp2);
        }
        printf("%d",temp1->val);
    }
    return head;
}