#include<stdio.h>
#include<malloc.h>
typedef int ElemType;
struct LNode{
    ElemType data;
    struct LNode *next;
};
typedef struct LNode LNode;
typedef struct LNode* LinkList;
LNode* GetElem(LinkList L,int i){
    int j = 1;
    struct LNode* p = (struct LNode*)malloc(sizeof(struct LNode));
    LNode *p = L->next;
    if(i == 0){
        return L;
    }
    if(i < 1){
        return NULL;
    }
    while(p!=NULL && j < i){
        p = p->next;
        j++;
    }
    return p;

}
void main(){
    LinkList L;
    
}
