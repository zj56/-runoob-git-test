/* 
sizeof(数据类型)
功能：返回值就是该数据类型所占的字节数
例子：sizeof（char） = 1
例子：sizeof（int） = 4
例子：sizeof（double） = 8



一个指针变量到底占几个字节
假设p指向char类型变量（1B） 
假设q指向int类型变量（4B）
假设r指向double类型变量（8B）
p q r本身所占的字节数是否一样 

一个字节（8bit）一个编号，则doble类型有8个编号
以首元，即第一个字节的编号作为指针的地址
*/
#include<stdio.h>
int main(void){
    char ch = 'A';
    int i = 99;
    double x = 66.6;
    char *p = &ch;
    int * q = &i;
    double *r = &x;
    printf("%d %d %d\n",sizeof(p),sizeof(q),sizeof(r));
    return 0;
}