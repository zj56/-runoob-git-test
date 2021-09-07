#include<stdio.h>
// 第一种方式
// 这只是定义了一个新的数据类型，并没有定义变量
struct Student{
    int age;
    float score;
    char sex;
};

int main(void){
    /* 定义的同时可以整体赋值
    定义完之后只能单个赋值 */

    struct Student st = {80,66.6,'F'};
    // struct Student st2;
    // st2.age = 10;
    // st2.score = 88;
    // st2.sex = 'F';
    // printf("%d %f %c\n",st.age,st.score,st.sex);
    // printf("%d %f %c\n",st2.age,st2.score,st2.sex);
    /* 
        结构体变量名.变量名
        指针变量名->成员名
     */
    struct Student * pst = &st;
    pst->age = 88;
    pst->score = 55.4;
    pst->sex = 'F';
    // pst->age会被转换成（*pst）.age
    //所以pst->age等价于（*pst）.age也等价于st.age
    // pst->sge
    // 等价于pst所指向的那个结构体中age的这个成员


    return 0;
}
// 直接用第一种
// 第二、三种推荐不使用
/* 
怎样使用结构体变量
 赋值和初始化
 如何取出结构体变量中的每一个成员
 结构体变量的运算
 结构体变量和结构体变量指针作为函数参数传递的问题
 动态构造存放 学生信息的结构体数组
 */