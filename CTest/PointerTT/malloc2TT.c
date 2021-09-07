#include<stdio.h>
#include<malloc.h>
void f(int* p){
    *p = 200;
    free(p);
}
int main(void){
    int * p = (int *)malloc(sizeof(int));
    *p = 10;
    printf("%d\n",*p);//10
    f(p);
    printf("%d\n",*p);    //200
    return 0;
}