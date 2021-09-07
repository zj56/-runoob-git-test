#include "SeqList.h"
void SeqListInit(SL* ps){
    // s.size = 0;
    // s.a = NULL;
    // s.capacity = 0;   
    ps->a = (SLDataType*)malloc(sizeof(SLDataType)*4);
    if (ps ->a == NULL){
        printf("申请内存失败");
        exit(-1);
    }
    ps->size = 0;
    ps->capacity =4;
}
void SeqListPushBack(SL* ps,SLDataType x){
    if(ps->size >=ps->capacity){
        ps->capacity*=2;
        ps->a = (SLDataType*)realloc(ps->a,sizeof(SLDataType)*ps->capacity);
    }
    if(ps->a == NULL){
        printf("扩容失败\n");
        exut(-1);
    }
    assert(ps);
    ps->a[ps->size-1] = x;
    ps->size++;
};
void SeqListPrint(SL* ps){
    assert(ps);
    for(int i =0;i < ps->size;i++){
        printf("%d",ps->a[i]);
    }
    printf("\n");
}
//尾删
void SeqListPopBack(SL* ps){
    assert(ps);
    ps->a[ps->size-1] = 0;
    ps->size--;
};
void SeqListPushFont(SL* ps,SLDataType x){
    
    int end = ps->size -1;
    while(end>=0){
        ps->a[end+1] = ps->a[end];
        --end;
    }
    ps->a[0]=x;
    ps->size++;
}
void SeqListPopFront(SL* ps,SLDataType x);