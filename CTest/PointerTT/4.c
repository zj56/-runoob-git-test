#include<stdio.h>
int main(void){
    int i = 5;
    int *p;
    int *q;
    p = &i;
    // *q = p;//*q为int型 p为int*型
    // *q = *p; 
    p = q;//q是垃圾值，q付给p，p也变成垃圾值
    // q的空间是本程序的，所以本程序可以读写q的内容，
    // 但是如果q内部是垃圾值，则本程序不能读取*q的内容
    // 因为*q所代表的内存单元的控制权限并没有分配给本程序
    // 
    // printf("%p\n",q);
    // printf("%d\n",*p);
    printf("%d\n",*q); //
    return 0;
}