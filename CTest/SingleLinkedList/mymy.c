#include<stdio.h>
#include <stdbool.h>
#include <stdlib.h>
typedef int c;
typedef struct LNode{
    ElemType data;
    struct LNode *next;
}LNode;
// 定义头指针
LNode *LinkList;
//在第i个位置插入元素e（带头节点）
bool ListInsert(LNode *L ,int i,ElemType e){
    //头节点是第0个节点
    if(i < 1){
        return false;
    }
    // 指针p指向当前扫描到的节点
    LNode *p;
    // 当前p指向的是第几个节点
    //头节点是第0个节点
    int j = 0;
    p = L;
    // 循环找到第i-1个节点
    // i- 1=0
    while(p!=NULL && j < i-1){
        p = p->next;
        j++;
    }
    if(p == NULL){
        return false;
    }
    LNode *s = (LNode *)malloc(sizeof(LNode));
    s->data = e;
    s->next = p->next;
    p->next = s;
    return true;
}
// 后插操作，在p节点之后插入元素e
bool InsertNextNode(LNode *p,ElemType e){
    if(p == NULL){
        return false;
    }
    LNode *s = (LNode *)malloc(sizeof(LNode));
    // 内存可能分配失败（如内存不足）
    if(s == NULL){
        return false;
    }
    s->data = e;
    s->next = p->next;
    p->next = s;
    return true;

}
// 前插操作
// bool InsertPriorNode(LNode LinkList,LNode *p,){

// }
void main(){
    ListInsert(LinkList,1,2);
    // printf(LinkList);
    

}