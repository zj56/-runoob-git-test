/* 跨函数使用内存 */
#include<stdio.h>
void f(int **q){
    // q是个指针变量，无论q是什么类型的变量，都只占4个字节
    int i =5;
    // *q等价于p
    *q = &i;
}
int main(void){
    int* p;
    f(&p);
    printf("%p",*p);
    /* 本句语法没有问题
    但逻辑上有问题
    f()执行完毕后，静态变量i和q的内存
    已经释放，*p不能访问i的内存 */
    /* 静态变量不能跨函数使用内存 */
    return 0;

}