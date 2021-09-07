#include<stdio.h>
int main(void){
    int i = 10;
    int * p = &i;
    // （int）* p存放int类型地址
    int **q = &p;
    // (int*)*q q存放(int*)类型的地址
    int *** r = &q;
    // *r =q **r = p ***r=i
    f(&p);
    // p是int * 类型，&p是int**类型

}
void g(){
    int i = 10;
    int * p =&i;
    f(&p);

}