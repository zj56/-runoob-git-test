#include <stdio.h>
int main(void){
    int* p;//p是变量的名字，
    // int*表示p变量存放的是int
    // 类型变量的地址
    // double* p表示p只能存放
    int i = 3;
    // p = i;
    // 错误，p只能存放int类型变量的地址，不能存放int类型的值
    p = 55;
    return 0;
}