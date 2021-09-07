#include<stdio.h>
bool InitList(LinkList &L){
    L = null;
    return true;
}
void main(){
    typedef struct LNode{
    int data;
    struct LNode *next;
}LNode,*LinkList;

    LinkList L;
    InitList(L);

}
