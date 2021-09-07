#include <stdio.h>
#define MaxSize 10
typedef struct{
    int data[MaxSize]; //ElemType
    int length;
}SqList;
//基本操作——初始化一个顺序表
void InitList(SqList &L){
    for(int i = 0;i < MaxSize;i++){
        L.data[i] = 0;

    }
    L.length = 0;

}
int main(){
    SqList L;
    InitList(L);
    return 0;
}