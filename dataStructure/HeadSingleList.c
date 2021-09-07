#include<stdio.h>
#include<malloc.h>
#include<stdbool.h>
typedef int ElemType;
typedef struct LNode LNode;
typedef struct LNode* LinkList;
struct LNode{
    ElemType data;
    struct LNode *next;
};

bool ListInsert(LinkList L,int i,ElemType e){
    if(i < 1){
        return false;
    };
    LNode *p;
    int j = 0;
    p = L;
    while(p!=NULL && j<i-1){
        p = p->next;
        j++;
    };
    if(p == NULL){
        return false;
    };
    LNode *s = (LNode *)malloc(sizeof(LNode));
    s->data = e;
    s->next = p->next;
    p->next = s;
    return true;
};
void main(){
    // 定义头指针
    LNode A,B;
    LinkList L;
    LNode Head = {0,&A};
    L = &Head;
    A.data= 1;
    A.next = &B;



}