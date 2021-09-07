#include<stdio.h>

int main(void){
    int a[5];
    int b[5];
    //a = b error 因为a为常量
    // 一维数组名是个指针常量，他存放的是
    // 以为数组第一个元素的地址
    printf("%p\n",&a[0]);
    printf("%p",&a);
}
/* 
下标和指针的关系
如果p是个指针变量，则p[i]永远等价于*(p+i) 
*/