// https://leetcode.com/problems/add-two-numbers/

#include <math.h>
#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* ans = (struct ListNode*) malloc(sizeof(struct ListNode));

    struct ListNode* t1 = (struct ListNode*) malloc(sizeof(struct ListNode));
    struct ListNode* t2 = (struct ListNode*) malloc(sizeof(struct ListNode));
    struct ListNode* th = (struct ListNode*) malloc(sizeof(struct ListNode));

    ans->val = 0;
    ans->next = th;

    t1 = l1;
    t2 = l2;

    int n1 = 0;
    int n2 = 0;

    int c1 = 0;
    int c2 = 0;

    while(t1->next != NULL){
        n1 += t1->val * pow(10, c1);
        c1++;
        t1 = t1->next;
    }

    while(t2->next != NULL){
        n2 += t2->val * pow(10, c2);
        c2++;
        t2 = t2->next;
    }

    n1 += n2;

    ans->val = n1 % 10;
    ans->next = th;

    n1 = n1 / 10;

    while ((n1 / 10) != 0){
        struct ListNode* thead = (struct ListNode*) malloc(sizeof(struct ListNode));

        th->val = n1 % 10;
        n1 = n1 / 10;
        th->next = thead;
        th = th->next;
    }

    return th;
};
