#include<stdio.h>
int mai(void){
    int *p;
    int i = 5;
    *p = i;//调用其他空间， *p为int类型 i也为int类型
    printf("%d\n",*p);
    return 0;
}