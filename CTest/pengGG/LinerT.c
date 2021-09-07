#include <stdio.h>
// #define N 10
// typedef int ElemType;
typedef int SLDataType;
struct Seqlist{
    // ElemType a[N];
    SLDataType *array;//数组的指针
    int size;//有效数据的个数
    int capacity;//容量空间的大小
}L;
void S