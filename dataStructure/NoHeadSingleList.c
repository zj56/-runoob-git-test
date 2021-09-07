#include<stdio.h>
#include<malloc.h>
#include<stdbool.h>
typedef int ElemType;
struct LNode{
    ElemType data;
    struct LNode *next;
};
typedef struct LNode LNode;
typedef struct LNode* LinkList;
bool InitList(LinkList L){
    L = NULL;
    return true;
};
void test(){

}
bool Empty(LinkList L){
    if(L == NULL){
        return true;
    }else{
        return false;
    }
}
void main(){
    LinkList L;
    InitList(L);
}