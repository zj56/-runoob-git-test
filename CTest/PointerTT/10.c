/* 
指针变量的运算，不能相乘，相加，也不能相除
只能相减
 如果两个指针变量指向的是同一块连续空间的
 不同存储单元
 则这两个指针变量才可以相减*/
 #include<stdio.h>
 int main(void){
     int i = 5;
     int j = 10;
     int *p = &i;
     int *q = &j;
     int a[5];
     p = & a[1];
     q = & a[4];
    printf("p和q所指向的单元相隔%d个单元\n",q-p);
    
 }