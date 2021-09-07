#include<stdio.h>
#include <string.h>
struct Student{
    int age;
    char sex;
    char name[100];
};//分号不能省略
void  InputStudent(struct Student * ps){
//ps只占4个字节，因为指针只指向第一个字节的编号
// 一个字节一个地址 8位一个编号
    ps->age = 10;
    strcpy(ps->name,"张三");
};
// 发送地址还是发送内容
/* 指针的优点之一：
        快速的传递数据
        耗用内存小
        执行速度快 */
// 为了减少内存的损耗
// 也为了减少执行时间
// 发送指针
void OutputStudent(struct Student *pst){
    printf("%d %c %s\n",pst->age,pst->sex,pst->name);
};
int main(void){
    struct Student st;
    struct Student * ps;
    ps = &st;
    InputStudent(ps);
    OutputStudent(ps);
    // printf("age=%d name=%s",st.age,st.name);
    return 0;
}
