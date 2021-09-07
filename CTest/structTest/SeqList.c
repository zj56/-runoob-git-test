#include<stdio.h>
#include<stdlib.h>
typedef int SLDataType;
struct SeqList{
    SLDataType *a;//数组的指针
    int size; //有效数据的个数
    int capacity;//容量
};
typedef struct SeqList SL;
typedef struct SeqList SeqList;
void SeqListPrint(SL* ps);
void SeqListInit(SL* ps);
void SeqListPushBack(SL* ps,SLDataType x);
void SeqListPopBack(SL* ps);
void SeqListPushFont(SL* ps,SLDataType x);
void SeqListPopFront(SL* ps,SLDataType x);
void SeqListInit(SL* ps){
/*     s.size = 0;
    s.a = NULL;
    s.capacity = 0; */
    ps->a = (SLDataType*)malloc(sizeof(SLDataType)*4);
    if(ps->a == NULL){
        printf("申请内存失败\n");
        exit(-1);
    }
    ps->size = 0;
    ps->capacity = 4;
};
void SeqListPushBack(SL* ps,SLDataType x){
    ps->a[ps->size] = x;
    ps->size++;
};
void main(){
    SeqList s;
    SeqListInit(&s);
    SeqListPushBack(&s,1);
    SeqListPushBack(&s,2);
    SeqListPushBack(&s,3);
}

