#include<stdio.h>
void swap(int *p1,int *p2);
void main()
{
    int a , b , c;
    int *pointer_1,*pointer_2,*pointer_3;
    scanf("%d %d %d",&a,&b,&c);
    // a = 2 ;
    // b = 3;
    pointer_1 = &a;
    pointer_2 = &b;
    pointer_3 = &c;
    if(a < b){
        swap(pointer_1,pointer_2);
    }
    if(*pointer_1 < c){
        swap(pointer_1,pointer_3);
    }
    if(*pointer_2 < *pointer_3){
        swap(pointer_2,pointer_3);
    }
    // printf("\n%d > %d\n",a,b);
    printf("%d>%d>%d",*pointer_1,*pointer_2,*pointer_3);
}
void swap(int *p1,int *p2)
{
    printf("waiting");
    int temp;
    temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}