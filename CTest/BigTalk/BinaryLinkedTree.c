#include<stdio.h>
/* 二叉树的顺序存储（数组）
如果存放不平衡二叉树，浪费空间 */
typedef struct BiTNode{
    int data;
    struct BiNode * lchild,*rchild;
}BiNode,* BiTree;
/* 二叉树的前序递归遍历算法 */
void PreOrderTraverse(BiTree T){//传入一个地址
    if(T==NULL){
        return;
    }
    printf("%c",T->data);
    PreOrderTraverse(T->lchild);
    PreOrderTraverse(T->rchild);

} 
/* 二叉树的中序递归遍历算法 */
void InOrderTraverse(BiTree T){//传入一个地址
    if(T==NULL){
        return;
    }
    InOrderTraverse(T->lchild);
    printf("%c",T->data);
    InOrderTraverse(T->rchild);

} 