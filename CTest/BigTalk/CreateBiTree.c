#include<stdio.h>
typedef char String[24];
String str;
typedef char TElemType;
int index = 1;
typedef struct BiTNode{
    int data;
    struct BiNode * lchild,*rchild;
}BiNode,* BiTree;
void CreateBiTree(struct BiTNode* T){
    char ch;
    scanf("%c",&ch);
    ch = str[index++];
    if(ch == '#'){
        T = NULL;
    }else{
        T = (BiTree)malloc(sizeof(BiNode));
        if(!T){
            exit(-1);
        }
        T->data = ch;
        CreateBiTree(->)
        

    }
}