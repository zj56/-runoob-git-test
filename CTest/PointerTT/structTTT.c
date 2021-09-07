#include<stdio.h>
// 第一种方式
struct Student{
    int age;
    float score;
    char sex;
};
// 第二种方式
struct Student2{
    int age;
    float score;
    char sex;
}st2;
// 第三种方式
struct{
    int age;
    float score;
    char sex;
} st3;
int main(void){
    struct Student st = {80,66.6,'F'};
}
// 直接用第一种
// 第二、三种推荐不使用
/* 
怎样使用结构体变量
 赋值和初始化
 如何去除结构体变量中的每一个成员
 结构体变量的运算
 结构体变量和结构体变量指针作为函数参数传递的问题
 动态构造存放 学生信息的结构体数组
 */