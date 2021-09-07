//顺序表，有效数据在数组中必须是连续的
//静态顺序表设计（不能按需索取，静态指固定大小）
// typedef int SlDataType ;
// #define N 10
// struct SeqList
// {
//     SlDataType _a[N];
//     SlDataType size;//记录存的有效数据
//     /* data */
// };
// void SeqListPushBack(struct SeqList* ps,SlDataType x);
// void SeqListPopBack(struct SeqList* ps,SlDataType x);
// void SeqListPushFrom(struct SeqList* ps,SlDataType x);


//动态数据表设置
#pragma once
#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
typedef int SLDataType;
typedef struct  SeqList
{
    SLDataType* a;//数组的指针，指向动态开辟的数组
    int size; //有效数据的个数
    int capacity; //容量空间的大小
    /* data */
}SL,SeqList;
void SeqListPrint(SL* ps);
void SeqListInit(SL* ps);
void SeqListPushBack(SL* ps,SLDataType x);
void SeqListPopBack(SL* ps);
void SeqListPushFont(SL* ps,SLDataType x);
void SeqListPopFront(SL* ps,SLDataType x);


