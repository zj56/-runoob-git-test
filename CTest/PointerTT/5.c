#include <stdio.h>
void swap(int* p,int* q){
    int m;//如果要互换p和q的值，
    // 则t必须是int*，不能是int类型
    // 地址不能互换，地址是死的
    m = *p;
    *p = *q;
    *q = m;
}
int main(void){
    int a = 3;
    int b =5;
    int* p = &a;
    int* q = &b;
    swap(p,q);
    printf("a = %d,b = %d\n",a,b);
    return 0;
}
// *号的三种含义
/* 

    1、乘法 
    2、定义指针变量
      int *p
      //定义了一个名字叫p的变量 int*只能存放地址
      3、指针运算符号
       *p 取指针p指向地址的值 */
