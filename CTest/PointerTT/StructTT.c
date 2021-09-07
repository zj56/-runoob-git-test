#include<stdio.h>
/* 结构体 */
struct Student{
    int age;
    float score;
    char sex;
};
int main(void){
    struct Student st = {80,66.6,'F'};
    // struct Student为一个数据类型
    return 0;
}