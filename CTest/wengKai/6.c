#include<stdio.h>
void minmax(int a[],int len,int *max,int *min);
int main(void){
    int a[] = {1,2,3,4,5,6,7,8,9,10};
    int min,max;
    // printf("min=%d\n",min);
    // printf("max=%d\n",max);
    printf("main sizeof(a)=%lu\n",sizeof(a));
    printf("main &a=%p\n",a);
    printf("main &a[0]=%p\n",&a[0]);
    printf("main &a[1]=%p\n",&a[1]);
    minmax(a,sizeof(a)/sizeof(a[0]),&min,&max);
    printf("min=%d,max=%d\n",min,max);
    printf("a[0]=%d\n",a[0]);
    // printf("*a=%d\n",*a);
    // min = 9;
    // int *p = &min;
    // printf("*p=%d\n",*p);
    // printf("p[0]=%d\n",p[0]);
    // printf("p[4]=%d\n",p[4]);
    // printf("p[5]=%d\n",p[5]);
    printf("*a=%d\n",*a);
    return 0; 
}
void minmax(int *a,int len,int *min,int *max){
    int i;
    printf("&a=%p\n",a);
    a[0]=1000;
    printf(" sizeof(a)=%lu\n",sizeof(a));
    for( i = 1;i < len;i++){
        if( a[i] < *min){
            *min = a[i];
        }
        if( a[i] > *max){
            *max = a[i];
        }
    }    
}
//函数参数表中的数组实际上是指针
//sizeof(a)=sizeof(int*)
//但是可以用数组的运算符【】进行运算
//数组变量是特殊的指针
//数组变量本身表达地址
// 所以 int a【10】；int *p = a 无需用&取地址
// 但是数组单元表达的是变量，需要用&去地址
// 【】运算符可以对数组做，也可以用指针做
// p【0】<==>a[0]
//int b[] = a操作不行，只能遍历
//int *q = a可以
// int b【】 --》 int * const b 常量指针
// 